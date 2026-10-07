"""CFR (Code of Federal Regulations) fetcher using eCFR API."""

import re
import time
import requests
from bs4 import BeautifulSoup
from typing import Dict, Any
from .cache import FetchError


def fetch_cfr(title: str, part: str, section: str = None, max_retries: int = 3) -> Dict[str, Any]:
    """
    Fetch CFR text.
    
    Args:
        title: Title number (e.g., "47")
        part: Part number (e.g., "230")
        section: Optional section number
        max_retries: Maximum number of retry attempts
        
    Returns:
        Dict with heading, text, source_url, fetched, cached
    """
    # Build URL for eCFR
    if section:
        url = f"https://www.ecfr.gov/current/title-{title}/part-{part}/section-{part}.{section}"
    else:
        url = f"https://www.ecfr.gov/current/title-{title}/part-{part}"
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract heading
            heading_elem = soup.find('h1', class_='section-heading')
            if not heading_elem:
                heading_elem = soup.find('h1')
            heading = heading_elem.get_text(strip=True) if heading_elem else f"{title} CFR {part}"
            if section:
                heading = f"{title} CFR {part}.{section}"
            
            # Extract text
            content_elem = soup.find('div', class_='content-body')
            if not content_elem:
                content_elem = soup.find('main')
            
            if not content_elem:
                raise FetchError("Could not find regulation content")
            
            text = content_elem.get_text(separator='\n', strip=True)
            
            # Clean up whitespace
            text = re.sub(r'\n\s*\n', '\n\n', text)
            
            return {
                "citation_type": "cfr",
                "title": title,
                "part": part,
                "section": section,
                "heading": heading,
                "text": text,
                "source_url": url,
                "fetched": True,
                "cached": False
            }
            
        except requests.RequestException as e:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue
            raise FetchError(f"Failed to fetch CFR: {str(e)}")
    
    raise FetchError(f"Failed to fetch CFR after {max_retries} attempts")

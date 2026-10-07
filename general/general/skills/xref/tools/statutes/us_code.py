"""US Code fetcher using uscode.house.gov."""

import re
import time
import requests
from bs4 import BeautifulSoup
from typing import Dict, Any
from .cache import FetchError


def fetch_us_code(title: str, section: str, max_retries: int = 3) -> Dict[str, Any]:
    """
    Fetch US Code section text.
    
    Args:
        title: Title number (e.g., "17")
        section: Section number (e.g., "512", "512a")
        max_retries: Maximum number of retry attempts
        
    Returns:
        Dict with heading, text, source_url, fetched, cached
    """
    url = f"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title{title}-section{section}"
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract heading
            heading_elem = soup.find('h2', class_='section-head')
            heading = heading_elem.get_text(strip=True) if heading_elem else f"Title {title}, Section {section}"
            
            # Extract section text
            content_elem = soup.find('div', class_='section-body')
            if not content_elem:
                raise FetchError("Could not find section content")
            
            text = content_elem.get_text(separator='\n', strip=True)
            
            # Clean up whitespace
            text = re.sub(r'\n\s*\n', '\n\n', text)
            
            return {
                "citation_type": "us_code",
                "title": title,
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
            raise FetchError(f"Failed to fetch US Code {title} USC {section}: {str(e)}")
    
    raise FetchError(f"Failed to fetch US Code {title} USC {section} after {max_retries} attempts")

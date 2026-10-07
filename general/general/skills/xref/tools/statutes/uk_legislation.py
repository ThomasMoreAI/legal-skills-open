"""UK Legislation fetcher using legislation.gov.uk API."""

import re
import time
import requests
from bs4 import BeautifulSoup
from typing import Dict, Any
from .cache import FetchError


def fetch_uk_legislation(act_name: str, year: str, section: str = None, max_retries: int = 3) -> Dict[str, Any]:
    """
    Fetch UK legislation text.
    
    Args:
        act_name: Name of the act (e.g., "data-protection-act")
        year: Year (e.g., "2018")
        section: Optional section number
        max_retries: Maximum number of retry attempts
        
    Returns:
        Dict with heading, text, source_url, fetched, cached
    """
    # Convert act name to URL-friendly format
    act_slug = act_name.lower().replace(' ', '-').replace('act', '').strip('-')
    
    if section:
        url = f"https://www.legislation.gov.uk/ukpga/{year}/{act_slug}/section/{section}"
    else:
        url = f"https://www.legislation.gov.uk/ukpga/{year}/{act_slug}"
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract heading
            heading_elem = soup.find('h2', class_='LegSnippetHeading')
            if not heading_elem:
                heading_elem = soup.find('h1')
            heading = heading_elem.get_text(strip=True) if heading_elem else f"{act_name} {year}"
            
            # Extract text
            content_elem = soup.find('div', class_='LegContent')
            if not content_elem:
                content_elem = soup.find('div', class_='content')
            
            if not content_elem:
                raise FetchError("Could not find legislation content")
            
            text = content_elem.get_text(separator='\n', strip=True)
            
            # Clean up whitespace
            text = re.sub(r'\n\s*\n', '\n\n', text)
            
            return {
                "citation_type": "uk_legislation",
                "act_name": act_name,
                "year": year,
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
            raise FetchError(f"Failed to fetch UK legislation: {str(e)}")
    
    raise FetchError(f"Failed to fetch UK legislation after {max_retries} attempts")

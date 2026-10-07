"""EU Regulations fetcher with pre-bundled GDPR support."""

import json
import os
import re
import time
import requests
from bs4 import BeautifulSoup
from typing import Dict, Any
from .cache import FetchError


def get_bundled_gdpr() -> Dict[str, Any]:
    """Load bundled GDPR data."""
    bundled_path = os.path.join(
        os.path.dirname(__file__),
        "..", "templates", "bundled", "gdpr.json"
    )
    
    if not os.path.exists(bundled_path):
        raise FetchError("GDPR bundled data not found")
    
    with open(bundled_path, "r", encoding="utf-8") as f:
        return json.load(f)


def fetch_eu_regulation(regulation: str, article: str, max_retries: int = 3) -> Dict[str, Any]:
    """
    Fetch EU regulation text.
    
    Args:
        regulation: Regulation name (e.g., "GDPR", "2016/679")
        article: Article number
        max_retries: Maximum number of retry attempts
        
    Returns:
        Dict with heading, text, source_url, fetched, cached
    """
    # Check if GDPR and use bundled version
    if regulation.upper() == "GDPR" or regulation == "2016/679":
        try:
            gdpr_data = get_bundled_gdpr()
            article_num = str(article)
            
            if article_num in gdpr_data["articles"]:
                article_data = gdpr_data["articles"][article_num]
                return {
                    "citation_type": "eu_regulation",
                    "regulation": "GDPR",
                    "article": article_num,
                    "heading": article_data["heading"],
                    "text": article_data["text"],
                    "source_url": f"https://gdpr-info.eu/art-{article_num}-gdpr/",
                    "fetched": True,
                    "cached": True,
                    "source": "bundled"
                }
        except (FetchError, KeyError):
            pass
    
    # Fallback to fetching from eur-lex or gdpr-info.eu
    if regulation.upper() == "GDPR" or regulation == "2016/679":
        url = f"https://gdpr-info.eu/art-{article}-gdpr/"
    else:
        url = f"https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:{regulation}"
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract heading and text
            if "gdpr-info.eu" in url:
                heading_elem = soup.find('h1')
                heading = heading_elem.get_text(strip=True) if heading_elem else f"GDPR Article {article}"
                
                content_elem = soup.find('div', class_='article')
                if not content_elem:
                    content_elem = soup.find('main')
            else:
                heading = f"Regulation {regulation}, Article {article}"
                content_elem = soup.find('div', class_='eli-main-content')
            
            if not content_elem:
                raise FetchError("Could not find regulation content")
            
            text = content_elem.get_text(separator='\n', strip=True)
            text = re.sub(r'\n\s*\n', '\n\n', text)
            
            return {
                "citation_type": "eu_regulation",
                "regulation": regulation,
                "article": article,
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
            raise FetchError(f"Failed to fetch EU regulation: {str(e)}")
    
    raise FetchError(f"Failed to fetch EU regulation after {max_retries} attempts")

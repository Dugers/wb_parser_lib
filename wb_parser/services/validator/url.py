import re
from urllib.parse import urlparse

def url_validator(url: str):
    if not isinstance(url, str):
        raise ValueError(f"URL must be a str. You got {type(url)}")
        
    if not url:
        raise ValueError("URL can't be empty")
        
    try:
        parsed = urlparse(url)
    except Exception as e:
        raise ValueError(f"URL parsing exception: {e}") from e
        
    if parsed.scheme not in ("http", "https"):
        raise ValueError(f"URL must start with http:// or https://. You got {url}")
        
    if not parsed.netloc:
        raise ValueError(f"URL must contain a domain. You got {url}")
        
    if url.rstrip().endswith("/"):
        raise ValueError(f"URL musnt not end in /. You got {url}")
        
    domain = parsed.netloc.split(":")[0]
    domain_pattern = r"^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{1,}$"
    if not re.fullmatch(domain_pattern, domain):
        raise ValueError(f"URL has incorrect domain format. You got {url}")
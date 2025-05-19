import pytest
from wb_parser.services.validator.url import url_validator

VALID_URLS = [
    "https://example.com",
    "http://sub.domain.com",
    "https://123-site.org",
    "http://x.y.z",
]

INVALID_URLS = [
    (None),
    (123),
    (""),
    ("ftp://example.com"),
    ("http://"),
    ("https://example.com/"),
    ("https://example..com"),
    ("https://-example.com"),
]

@pytest.mark.parametrize("url", VALID_URLS)
def test_url_validator_accepts_valid_urls(url):
    url_validator(url)

@pytest.mark.parametrize("url", INVALID_URLS)
def test_url_validator_rejects_invalid_urls(url):
    with pytest.raises(ValueError):
        url_validator(url)
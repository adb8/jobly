import requests
from bs4 import BeautifulSoup
from loguru import logger
import string
from api.util.secrets import SCRAPERAPI_API_KEY


class Scraper:
    def __init__(self):
        self.API_URL = "https://api.scraperapi.com/"
        self.API_KEY = SCRAPERAPI_API_KEY
        self.COUNTRY_CODE = "us"
        self.DEVICE_TYPE = "desktop"
        self.KEEP_HEADERS = "true"

    def scrape_data(self, url):
        if not url:
            logger.exepction("No URL provided")
            return None
        try:
            payload = {
                "api_key": self.API_KEY,
                "url": url,
                "country_code": self.COUNTRY_CODE,
                "device_type": self.DEVICE_TYPE,
                "keep_headers": self.KEEP_HEADERS,
            }
            r = requests.get(self.API_URL, params=payload)
            soup = BeautifulSoup(r.text, "html.parser")
            return soup
        except Exception as e:
            logger.exception(e)
            return None

    def get_text(self, soup):
        if not soup or not isinstance(soup, BeautifulSoup):
            logger.exception("Invalid BeautifulSoup object")
            return None
        all_text = soup.get_text()
        trimmed_text = " ".join(all_text.split())
        allowed_chars = string.ascii_letters + string.digits + string.punctuation + " "
        cleaned_text = "".join(char for char in trimmed_text if char in allowed_chars)
        return cleaned_text


def test_scraper():
    scraper = Scraper()
    soup = scraper.scrape_data(
        "https://www.amazon.jobs/en/jobs/2808739/software-development-engineer-internship-2025-us"
    )
    text = scraper.get_text(soup)
    logger.info(text)


if __name__ == "__main__":
    test_scraper()

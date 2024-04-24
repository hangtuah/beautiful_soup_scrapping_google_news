import requests

def fetch_page(url):
    """Fetches a webpage and returns its HTML content."""
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    return response.text

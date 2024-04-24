from bs4 import BeautifulSoup

def parse_html(html_content):
    """Parses HTML content using Beautiful Soup and returns a soup object."""
    return BeautifulSoup(html_content, 'html.parser')

def find_element_by_id(soup, element_id):
    """Finds a single element by its ID."""
    return soup.find(id=element_id)

def find_elements_by_class(soup, class_name):
    """Finds all elements with a given class name."""
    return soup.find(class_=class_name)

def find_all_articles(soup):
    """Finds all article tags."""
    return soup.find_all('article')


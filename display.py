import pprint
import json
from tabulate import tabulate

def print_news_pretty(news_list):
    pp = pprint.PrettyPrinter(indent=4)
    for news in news_list:
        pp.pprint(news)

def print_news_formatted(news_list):
    for news in news_list:
        print(f"Title: {news['Title']}\nURL: {news['URL']}\nAuthor: {news['Author']}\n")

def print_news_json(news_list):
    for news in news_list:
        print(json.dumps(news, indent=4))

def print_news_tabulate(news_list):
    table = [list(news.values()) for news in news_list]
    headers = list(news_list[0].keys()) if news_list else []
    print(tabulate(table, headers=headers, tablefmt='grid'))

def print_news_custom(news_list):
    for news in news_list:
        print("-" * 40)
        print(f"Title: {news['Title']}")
        print(f"URL: {news['URL']}")
        print(f"Author: {news['Author']}")
        print("-" * 40)

# Example usage:
news_data = [
    {'Title': 'Example News Title', 'URL': 'http://example.com', 'Author': 'John Doe'},
    {'Title': 'Another News Title', 'URL': 'http://example.com', 'Author': 'Jane Doe'}
]

# Uncomment one of the following lines to use a specific print function:
# print_news_pretty(news_data)
# print_news_formatted(news_data)
# print_news_json(news_data)
# print_news_tabulate(news_data)
# print_news_custom(news_data)

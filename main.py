from scraper import fetch_page
from parser import parse_html,  find_all_articles
from spacy_model import load_spacy_model
import re
from data_frame_operations import export_dataframe, create_dataframe


def main():
    url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSkwyMHZNRFYwWHpWekVnVmxiaTFIUWlnQVAB?hl=en-MY&gl=MY&ceid=MY%3Aen"
    html_content = fetch_page(url)
    soup = parse_html(html_content)

    # Use parser functions
    articles = find_all_articles(soup)
    print("Number of articles found:", len(articles))

    UTM_news = []
    UTM_title = []

    for article in articles:
        title_objs = article.find_all("a")
        if len(title_objs) > 1:
            title_obj = title_objs[1]  # Ensure that there's at least two 'a' tags
            title = title_obj.text.strip()
            UTM_title.append(title)
            url_ = title_obj['href'].strip()

            # Attempt to find author within the article
            author = ""
            span_obj = article.find_all('span', attrs={"aria-hidden": "true"})
            for span_element in span_obj:
                if span_element.text.strip():
                    author = span_element.text.strip()
                    break

            # Put into key-value dictionary
            temp = {
                "Title": title,
                "URL": url_,
                "Author": author
            }

            UTM_news.append(temp)

    for news in UTM_news:
        # print(print_news_formatted(news))
        print(news)


    # load model
    nlp = load_spacy_model()

    cleaned_title = []
    normalized_title = []

    for title in UTM_title:
        # Tokenization, Lemmatization, POS tagging, Stopword identification
        doc = nlp(title)
        normalized_tokens = [token.lemma_ for token in doc if not token.is_stop]

        # Rejoin all word
        final_text = ' '.join([token for token in normalized_tokens])
        normalized_title.append(final_text)

        # Title text cleaning
        final_text = final_text.lower()
        final_text = re.sub(r'\d', '', final_text)
        final_text = re.sub(r'[^a-zA-Z0-9]', ' ', final_text)
        final_text = re.sub(r'^\s|\s\s', '', final_text)
        cleaned_title.append(final_text)

        # print("Normalized Title:", normalized_title)
        # print("Cleaned Title:", cleaned_title)
        df = create_dataframe(UTM_title)
        export_dataframe(df, 'UTM_NEWS')


if __name__ == "__main__":
    main()

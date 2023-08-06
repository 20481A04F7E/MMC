import requests
from bs4 import BeautifulSoup
import re

def get_imdb_movie_data():
    url = "https://www.imdb.com/chart/top"  # IMDb Top 250 Movies URL
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        movie_data = []
        
        for movie_row in soup.select('tbody.lister-list tr'):
            title = movie_row.find('td', class_='titleColumn').a.text.strip()
            movie_data.append({'title': title})
            
        return movie_data
    else:
        print("Failed to fetch data from IMDb.")
        return []

def get_movie_reviews(title):
    # Here, you can use other sources to get movie reviews, or use an API if available.
    # For this example, we'll use fake reviews for demonstration purposes.
    # Replace this section with actual web scraping or API calls to fetch reviews.
    reviews = [
        "This movie was amazing! I loved every minute of it.",
        "Great performances by the actors, and the story was gripping.",
        "Disappointing movie. The plot was weak, and the acting was subpar.",
        "One of the best movies I've ever seen. Highly recommended.",
    ]
    return reviews

def perform_sentiment_analysis(reviews):
    positive_keywords = ["amazing", "loved", "great", "recommended", "best"]
    negative_keywords = ["disappointing", "weak", "subpar", "bad", "worst"]
    
    sentiment_scores = []
    for review in reviews:
        positive_count = sum(1 for keyword in positive_keywords if keyword in review.lower())
        negative_count = sum(1 for keyword in negative_keywords if keyword in review.lower())
        sentiment_score = positive_count - negative_count
        sentiment_scores.append(sentiment_score)
    
    return sentiment_scores

if __name__ == "__main__":
    movie_data = get_imdb_movie_data()
    
    for movie in movie_data:
        title = movie['title']
        reviews = get_movie_reviews(title)
        sentiment_scores = perform_sentiment_analysis(reviews)
        average_sentiment_score = sum(sentiment_scores) / len(sentiment_scores)
        
        print(f"Movie: {title}")
        print("Reviews:")
        for i, review in enumerate(reviews, 1):
            print(f"{i}. {review}")
        print(f"Average Sentiment Score: {average_sentiment_score}\n")

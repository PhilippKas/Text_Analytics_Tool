import csv
from datetime import datetime

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

from analyze_texts_dashboard.models import Comments

# Get the necessary nltk stuff
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def get_sentiment(comment): 
    pol_score = sia.polarity_scores(comment)
    if pol_score["neg"] <= pol_score["pos"]:
        return "pos"
    else:
        return "neg"

def import_comments(file_path):
    with open(file_path, "r") as file: 
        reader = csv.DictReader(file)
        for row in reader: 
            Comments.objects.create(
                comment = row["comment"],
                tool = row["tool"],
                sentiment = get_sentiment(row["comment"]),
                published_date = datetime.strptime(row['published_date'], '%Y-%m-%d').date()
            )
            

import_comments('comments.csv')
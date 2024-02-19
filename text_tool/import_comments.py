import csv
from datetime import datetime

from analyze_texts_dashboard.models import Comments

def import_comments(file_path):
    with open(file_path, "r") as file: 
        reader = csv.DictReader(file)
        for row in reader: 
            Comments.objects.create(
                comment = row["comment"],
                tool = row["tool"],
                published_date = datetime.strptime(row['published_date'], '%Y-%m-%d').date()
            )
            

import_comments('comments.csv')
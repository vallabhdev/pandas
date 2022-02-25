# Python program to convert xml
# structure into dataframes using beautifulsoup
import pandas as pd
# Import libraries
from bs4 import BeautifulSoup

# Open XML file
file = open("myFile.xml", 'r')

# Read the contents of that file
contents = file.read()

soup = BeautifulSoup(contents)

# Extracting the data
authors = soup.find_all('author')
titles = soup.find_all('title')
prices = soup.find_all('price')
pubdate = soup.find_all('publish_date')
genres = soup.find_all('genre')
des = soup.find_all('description')

data = []

# Loop to store the data in a list named 'data'
for i in range(0, len(authors)):
    rows = [authors[i].get_text(), titles[i].get_text(), genres[i].get_text(),
            prices[i].get_text(), pubdate[i].get_text(), des[i].get_text()]
    data.append(rows)

# Converting the list into dataframe
df = pd.DataFrame(data, columns=['Author',
                                 'Book Title', 'Genre',
                                 'Price', 'Publish Date',
                                 'Description'], dtype=str)
df.to_csv('myFile.csv')

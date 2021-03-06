# pip install beautifulsoup4
# pip install vader-sentiment

import requests
import bs4
from vader_sentiment.vader_sentiment import SentimentIntensityAnalyzer

x = "https://www.flipkart.com/lg-all-in-one-80cm-32-inch-hd-ready-led-smart-tv/product-reviews/itmfhbvzmjgfd6nn?pid=TVSFHBVZASS5XA3H&lid=LSTTVSFHBVZASS5XA3HOB56WL&marketplace=FLIPKART"
response = requests.get(x)
soup = bs4.BeautifulSoup(response.content, 'lxml')
for j in range(5):
    response1 = requests.get(x + '&page=' + str(j))
    soup2 = bs4.BeautifulSoup(response1.content, 'lxml')
    comments = soup2.select('.t-ZTKy > div > div')  # Html class names can change in future so change it accordingly
    for i in comments:
        review = i.getText()
        print(review + '\n')

analyze = SentimentIntensityAnalyzer()
s = analyze.polarity_scores(review)
print(s)

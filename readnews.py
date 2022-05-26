# Read News


import time
import requests
import json
import pyttsx3


def onEnd(name, completed):
    print("End", name, completed)
    time.sleep(1)


# Read the news loudly
def read_news(string):
    tts.say(string)
    tts.runAndWait()


tts = pyttsx3.init()
tts.connect("finished-utterance", onEnd)
api_key = "6e4fd9a26c63430097f8c420733a1c25"

a = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}")
news = json.loads(a.text)

total_articles = news.get("totalResults")
articles = news.get("articles")

read_news(f"There are {total_articles} articles")

for i in range(len(articles)):
    title = articles[i].get("title")
    author = articles[i].get("author")
    description = articles[i].get("description")

    read_news(f"Article number {i + 1}")
    read_news(f"Title {title}")
    read_news(f"Author {author}")
    read_news(f"{description}")

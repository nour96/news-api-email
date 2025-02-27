import requests

api_key = "ad5ff7abc3c04002aeb98b1c5dfd81c1"
url = (
    "https://newsapi.org/v2/everything?q=tesla&"
    "from=2025-01-27&sortBy=publishedAt&apiKey="
    "ad5ff7abc3c04002aeb98b1c5dfd81c1"
)
request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])



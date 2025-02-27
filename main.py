import requests, smtplib, ssl

api_key = "ad5ff7abc3c04002aeb98b1c5dfd81c1"
topic = "tesla"
url = (
    "https://newsapi.org/v2/everything?"
    f"q={topic}&"
    "sortBy=publishedAt&apiKey="
    "ad5ff7abc3c04002aeb98b1c5dfd81c1"
    "&language=en"
)
request = requests.get(url)
content = request.json()

body = " "
for article in content["articles"][:20]:
    if article["title"] and article["description"] is not None:
        body = "Subject: Today's news" \
            +  "\n" + body + article["title"] + "\n" + article["description"]+ "\n" \
            + article["url"] + 2 * "\n"
    

def send_email(message):
    host= "smtp.gmail.com"
    port = 465
    
    username = "nour.ham96@gmail.com"
    password = "ttji euxy nwxd jfaq"

    receiver = "nour.ham96@gmail.com"
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        
body = body.encode("utf-8")
send_email(body)        

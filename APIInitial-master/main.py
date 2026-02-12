import requests

api_key = "7bf324473e9a429db3b362909d6d2e2b"
url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=7bf324473e9a429db3b362909d6d2e2b'

image_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/181px-Cat_August_2010-4.jpg'

request = requests.get(url)
image_request = requests.get(image_url)

#this downloads a image from the web
#wb is write binary mode
with open('image.jpg', "wb") as file:
    file.write(image_request.content)

#get a dictionary with data
content = request.json()

body = ""
for article in content['articles'][0:20]:
    if article['title'] is not None and article['description'] is not None:
        body = body + article['title'] + '\n' \
               + article['description'] + '\n' \
               + article['url'] + 2 * '\n'

print(body)
import PIL
import requests

quote = requests.get("https://api.quotable.io/random")

quote = quote.json()

print(f"{quote["content"]} - {quote["author"]}")
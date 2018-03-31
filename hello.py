
from aylienapiclient import textapi
client = textapi.Client("402c4f5d", "c4ce28551be5a50a9299d5badb825287")
sentiment = client.Sentiment({'text': 'John is a very good football player!'})
print sentiment

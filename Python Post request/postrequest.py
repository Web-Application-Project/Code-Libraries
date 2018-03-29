from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'http://text-processing.com/api/sentiment/' # Set destination URL here
post_fields = {'text': 'This is awesome'}     # Set POST fields here

request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()
print(json)
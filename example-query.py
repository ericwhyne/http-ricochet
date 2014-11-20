#!/usr/bin/python
import urllib2
import random

# A list of places we've deployed ricochet
ricochet_servers = [
"http://127.0.0.1:8080/ricochet/ricochet?url=",
"http://127.0.0.1:8080/ricochet/ricochet?url="
]

# We're identifying ourselves to ourself here, this will show up in the server logs (unless you've disabled them).
headers = { 'User-Agent' : 'Its me!' }

# Pick a random server, build the query, then make the query.
ricochet_server = random.choice(ricochet_servers)
content_type = "&ct=text/html"
url = "http://news.ycombinator.com"
# use urllib2.quote if your url contains parameters, eg:
# url = urllib2.quote("https://news.ycombinator.com/newest?n=31")
query = ricochet_server + url + content_type

print urllib2.urlopen(urllib2.Request(query, None, headers)).read()

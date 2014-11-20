http-ricochet
=============

A simple proxy web service in 19 lines of Python code.

To play with it on a VM:
```
git clone http://github.com/ericwhyne/http-ricochet
vagrant up
vagrant ssh
cd /vagrant
./deploy.sh
```
To deploy somehwere:
```
Deploy an Ubuntu server to the location you'd like to use ricochet from.
Ssh into it.
git clone http://github.com/ericwhyne/http-ricochet
./deploy.sh
```
To use:
```
#!/usr/bin/python
import urllib2
url = http://ricochet-server/ricochet/ricochet?url=http://news.ycombinator.com
print urllib2.urlopen(urllib2.Request(form_data.getvalue('url'), None, headers)).read()
```
Controlling the content type using the ct parameter:
```
http://127.0.0.1:8080/ricochet/ricochet?url=http://news.ycombinator.com&ct=text/plain
http://127.0.0.1:8080/ricochet/ricochet?url=http://upload.wikimedia.org/wikipedia/commons/thumb/2/26/YellowLabradorLooking_new.jpg/220px-YellowLabradorLooking_new.jpg&ct=image/jpeg
```
Getting the result encoded in base64:
```
http://127.0.0.1:8080/ricochet/ricochet?url=http://news.ycombinator.com&contenttype=text/plain&encode=base64
```

Note: If you render the retrieved html in a browser, requests will not go through ricochet. Don't do this if you are trying to hide your location. If you want to gather everything through ricochet use BeautifulSoup to extract all hrefs and convert them into ricochet queries using the idioms in the example-query.py file.

Here is an example snippet to extract all hrefs from raw html.
```
from bs4 import BeautifulSoup
...
soup = BeautifulSoup(raw_html)
page_links = []
for link in soup.find_all('a'):
  page_links.append(link.get('href'))
...
```

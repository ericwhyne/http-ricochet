http-ricochet
=============

A simple text-only proxy web service in 19 lines of Python code.

To test and develop with Vagrant:
'''
    git clone http://github.com/ericwhyne/http-ricochet
    vagrant up
    vagrant ssh
    cd /vagrant
    ./deploy.sh
'''
To deploy:
'''
    Deploy an Ubuntu server somewhere you want to ricochet from.
    Ssh into it.
    git clone http://github.com/ericwhyne/http-ricochet
    ./deploy.sh
'''
To use:
'''
    #!/usr/bin/python
    import urllib2
    url = http://ricochet-server/ricochet/ricochet?url=http://news.ycombinator.com
    print urllib2.urlopen(urllib2.Request(form_data.getvalue('url'), None, headers)).read()
'''

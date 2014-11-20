#!/bin/bash
# This file contains stuff we only want to do once during provisioning.
sudo apt-get update
sudo apt-get -y upgrade

# Install and configure Apache Web Server
sudo apt-get -y install apache2
sudo apt-get -y install libapache2-mod-wsgi # needed to run have Apache run Python

# Copy python source
pydir="/var/www/ricochet/"
sudo mkdir -p "$pydir"
sudo cp -r src/* "$pydir"

# configure apache
sudo cp apache/ricochet-apache.conf /etc/apache2/sites-enabled/
sudo service apache2 restart

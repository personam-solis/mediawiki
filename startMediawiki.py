#!/usr/bin/env python3

import subprocess

"""
Starts the mysql container and starts the mediawiki container with the custom
constraints used to connect both containers to each other.

The only requirements are that the network "medianet" is created and set to
bridge, and that the custom images have already been created.

If the Docker volume is not already created then the run command should create
it for you; otherwise the volumes are "mediawikidb" and "mediawikihtml"
"""

# Start the database container then the mediawiki container. If Docker cant find
# the container then throw an error message.

runmediadb = """
docker container run -d --name mediadb 
--network medianet 
--mount source=mediawikidb,target=/var/lib/mysql
--restart unless-stopped
personamsolis/wikidb:mysql
"""

runmediawiki = """
docker container run --name mediawiki -d -p 8080:80 -p 443:443
--network medianet
--mount type=bind,source=${PWD}/default-ssl.conf,target=/etc/apache2/sites-available/default-ssl.conf
--mount type=bind,source=/etc/pki,target=/etc/pki
--mount source=mediawikihtml,target=/var/www/html
--restart unless-stopped
personamsolis/mywiki:latest 
"""

try:
    subprocess.run(runmediadb.split(), stdout=subprocess.DEVNULL)
    subprocess.run(runmediawiki.split(), stdout=subprocess.DEVNULL)
except KeyboardInterrupt:
    print("User manually stopped the script")

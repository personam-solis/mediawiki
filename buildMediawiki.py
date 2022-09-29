#!/usr/bin/env python3

import subprocess

"""
Builds the MySQL container. Remember to make sure that all files that a frequently
changed are at the END of the file
"""


def image_build(tag, dockerfile):
    subprocess.run(['docker', 'build', '-t', tag, '-f', dockerfile, '.'],
                   stdout=subprocess.DEVNULL)

# Run the build process
image_build('personamsolis/wikidb:mysql', './mysqlDockerfile')
image_build('personamsolis/mywiki:latest', './mediawikiDockerfile')

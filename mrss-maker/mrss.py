import os
import datetime
import hashlib
import argparse

"""
mrss.py http://baseurl/maybe/the/media/folder/ targetfolder/

Given a baseURL and a list of files or a target folder, generate an mrss file for that folder of images.
"""



# Brightsign MRSS Documentation
# http://support.brightsign.biz/hc/en-us/articles/218067267-Supported-Media-RSS-feeds



parser = argparse.ArgumentParser(description='Create a Brightsign MRSS feed from a directory of images')
parser.add_argument("media_folder", help="folder of media assets")
#parser.add_argument("baseURL", "Base URL of media assets on web")
args = parser.parse_args()

for a, b, c in os.walk(args.media_folder):
    print(a,c)
#print(args.baseURL)

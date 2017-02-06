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
parser.add_argument("base_url", help="Default location of MRSS assets when hosted")
parser.add_argument("media_folder", help="folder of media assets")
args = parser.parse_args()

base_directory = args.media_folder

filelist = []
for root,directories, filenames, in os.walk(base_directory):
    for filename in filenames:
        filepath = os.path.join(root, filename)
        name = filepath[len(base_directory):]
        filelist.append((filepath,name))

for fl in filelist:
    print(args.base_url + fl[1])
#print(args.baseURL)

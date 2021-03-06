import os
import datetime
import hashlib
import argparse
from imagemrss import MRImage
from urllib.parse import urljoin
import xml.etree.cElementTree as ET
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")



"""
mrss.py http://baseurl/maybe/the/media/folder/ http://baseurl/maybe/the/feed.xml targetfolder/

Given a baseURL and a list of files or a target folder, generate an mrss file for that folder of images.
"""



# Brightsign MRSS Documentation
# http://support.brightsign.biz/hc/en-us/articles/218067267-Supported-Media-RSS-feeds



parser = argparse.ArgumentParser(description='Create a Brightsign MRSS feed from a directory of images')
parser.add_argument("base_url", help="Default location of MRSS assets when hosted (eg http://...01/content/media/)")
parser.add_argument("feed_url", help="Default location of MRSS feed assets when hosted (eg http://...01/content/feed.xml)")
parser.add_argument("media_folder", help="folder of media assets")
args = parser.parse_args()

base_directory = args.media_folder

filelist = []
for root,directories, filenames, in os.walk(base_directory):
    for filename in filenames:
        if ".DS_Store" in filename:
            pass
        else:
            filepath = os.path.join(root, filename)
            filelist.append(MRImage(filepath, args.base_url))


###############
# Make MRSS   #
###############


rss = ET.Element('rss', attrib={'version':'2.0', 'xmlns:media':'http://search.yahoo.com/mrss/'})
channel = ET.Element('channel')
rss.append(channel)

channelTitle = ET.Element('title')
channelTitle.text="Brightsign MRSS Feed"
channel.append(channelTitle)

channelLink = ET.Element('link')
channelLink.text = args.feed_url
channel.append(channelLink)

channelDescription = ET.Element('description')
channelDescription.text = "Test of a MRSS Generator"
channel.append(channelDescription)

channelTTL = ET.Element('ttl')
channelTTL.text = '1'
channel.append(channelTTL)

#############
# Geerate images
#############

for img in filelist:
    item = ET.Element('item')

    itemTitle = ET.Element('title')
    itemTitle.text = img.name
    item.append(itemTitle)

    itemLink = ET.Element('link')
    itemLink.text = img.link
    item.append(itemLink)

    itemCategory = ET.Element('category')
    itemCategory.text = "image"
    item.append(itemCategory)

    itemDescription = ET.Element('description')
    itemDescription.text = img.name
    item.append(itemDescription)

    itemGUID = ET.Element('guid', attrib={'isPermaLink':'false'})
    itemGUID.text = img.fileHash
    item.append(itemGUID)

    itemMediaContent = ET.Element('media:content', attrib = {
    'url':str(img.link),
    'fileSize':str(img.fileSize),
    'type':str(img.mimetype),
    'medium':'image',
    'duration':str(img.displaytime)
    })
    item.append(itemMediaContent)


    channel.append(item)

print(prettify(rss))

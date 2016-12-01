#/usr/bin/python

import shutil

template_directory = "originals/template-card"
ID_FROM = 1
ID_TO = 50
brightsign_ids = map(lambda x:"%02d"%(x,), range(ID_FROM,ID_TO+1))

for bsid in brightsign_ids:
    shutil.copytree(template_directory, bsid)
    current_sync_filename = bsid+"/current-sync.xml"
    with open(current_sync_filename, 'r+') as f:
        text = f.read()
        text = text.replace("$BSID", bsid)
        text = text[0:-2] # Get rid of extra newline characters
        f.seek(0)
        f.write(text)
        f.truncate()

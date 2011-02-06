'''
Created on 30 Jan 2011

@author: david
'''
import json
import datetime
import re



cmd=''
i=0
entry = {}
item={}
while cmd !=  'ex':
    cmd = raw_input(">> \n").lower()
    # trim spaces between # and others
    cmd = ' '.join(cmd.split())
    cmd = cmd.replace('# ','')
    # extract hashtags for  taxonomy
    hashtags = re.findall(r"#(\w+)", cmd)
    for hashtag in hashtags:
        cmd = cmd.replace('#'+hashtag, '')

    now = datetime.datetime.now()
    tags = {}
    i=0
    for hashtag in hashtags:
        tags[str()] = hashtag 
        i = i+1 
    item['text'] = cmd
    item['tags'] = tags 
    entry[str(now)] = item            
    with open('entries.txt', mode='a') as f:
        # json for comms with online services
        json.dump(entry,f)
        entry = {}    
print 'tracker stopped'


import Message
from datetime import datetime
import time
import tweepy

with open('userList.txt', 'r') as file:
    users = file.readlines()
    users = [x.strip() for x in users]

config = []
fs = open("config_secret.txt", "r")
for line in fs:
    config.append(line.rstrip())

auth = tweepy.OAuthHandler(config[0], config[1])
auth.set_access_token(config[2], config[3])
api = tweepy.API(auth)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

relations = []

t = datetime.now()
i = 0
j = 0
while i < len(users):
    j = 0
    while j < len(users):
        print "Checking relations for ", users[i], users[j]
        try:
            status = api.show_friendship(source_screen_name=users[i], target_screen_name=users[j])
            if status[1].following:
                relations.append((users[i], users[j]))
                print "Relation exists between: ", users[i], users[j]
            j += 1
        except:
            delta = datetime.now() - t
            time.sleep(900 - delta.seconds)
            t = datetime.now()
    i += 1

with open('relationList.txt', 'w') as file:
    for relation in relations:
        file.write(str(relation[0])+" "+ str(relation[1]) + "\n")

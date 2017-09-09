import Message
import time
import tweepy

with open('userList.txt', 'r') as file:
    users = file.readlines()
    users = [x.strip() for x in users]

config = []
fs = open("config_secret.txt", "r")
for line in fs:
    config.append(line.rstrip())

auth = tweepy.AppAuthHandler(config[0], config[1])
api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

relations = []

for user in users:
    for friend in users:
        print "Checking relations for ", user, friend
        try:
            status = api.show_friendship(source_screen_name=user, target_screen_name=friend)
            if status[1].following:
                relations.append((user, friend))
                print user, friend
        except:
            time.sleep(900)

with open('relationList.txt', 'w') as file:
    for relation in relations:
        file.write(str(relation[0])+" "+ str(relation[1]))

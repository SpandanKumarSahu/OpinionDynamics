import tweepy
import pickle
import time
from datetime import datetime
from Message import Message

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

users = []
relations = []

with open('seed.txt', 'r') as file:
    for line in file:
        seed = line.rstrip()
users.append(seed)
sleeptime = 4
count = 0

def add_followers(user):
    pages = tweepy.Cursor(api.followers, screen_name=users[count]).pages()
    while True:
        try:
            page = next(pages)
            time.sleep(sleeptime)
        except tweepy.TweepError:
            print "Probable rate limit. Sleeping for 900 seconds"
            time.sleep(60*15)
            page = next(pages)
        except StopIteration:
            break
        for user in page:
            if user.screen_name not in users:
                if len(users) < 1000:
                    print "Adding User", user.screen_name
                    # Handle the situation of deleted accounts
                    try:
                        test = api.get_user(screen_name = user.screen_name)
                        users.append(user.screen_name)
                        relations.append((users[count], user.screen_name))
                    except:
                        print "The user ", user.screen_name, " doesn't exist." 
            else:
                print "Adding Relation", users[count], user.screen_name
                relations.append((users[count], user.screen_name))


# Notation: (A, B) => B follows A
while len(users) < 1000:
    add_followers(users[count])
    count += 1

while count < len(users):
    add_followers(users[count])

with open('usersList', 'w') as file:
    for user in users:
        file.write(user+"\n")

with open('relationsList', 'w') as file:
    for relation in relations:
        file.write(relation.first+" "+relation.second+"\n")

tweets = []

def get_all_tweets(screen_name):
    alltweets = []	
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    while len(new_tweets) > 0:
	print "getting tweets before %s" % (oldest)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
	alltweets.extend(new_tweets)
	oldest = alltweets[-1].id - 1
	print "...%s tweets downloaded so far" % (len(alltweets))
	
    outtweets = [Message(tweet.text.encode("utf-8"), screen_name, tweet.created_at)  for tweet in alltweets]
    with open('tweets.txt', 'a') as file:
        for message in outweets:
            message.show()
            pickle.dump(message, file, pickle.HIGHEST_PROTOCOL)

    pass

for user in users:
    get_all_tweets(user)


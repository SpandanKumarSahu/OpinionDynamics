import sys
import os
import tweepy

class Message:
    def __init__(self, text, uid, time):
        self.text = text
        self.uid = uid
        self.time = time

    def show(self):
        print "Message: ", self.text
        print "UserId: ", self.uid
        print "TimeStamp: ", self.time

    def get_UserId(self):
        return self.uid

    def getStr(self):
        return unicode(self.text) + "\n" + unicode(self.uid) + "\n" + unicode(self.time) + "\n"

config = []
fs = open("config_secret.txt", "r")
for line in fs:
    config.append(line.rstrip())

# Replace the API_KEY and API_SECRET with your application's key and secret.
auth = tweepy.AppAuthHandler(config[0], config[1])

api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

# Continue with rest of code

searchQuery = '#IndiaChinaFaceoff'  # this is what we're searching for
maxTweets = 20000 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
fName = 'data.txt' # We'll store the tweets in a text file.


# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = -1L

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))

while tweetCount < maxTweets:
    try:
        if (max_id <= 0):
            if (not sinceId):
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
            else:
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                        since_id=sinceId)
        else:
            if (not sinceId):
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                        max_id=str(max_id - 1))
            else:
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                        max_id=str(max_id - 1),
                                        since_id=sinceId)
        if not new_tweets:
            print("No more tweets found")
            break
        messages = []
        for tweet in new_tweets:
            message = Message(tweet.text, tweet.user.screen_name, tweet.created_at)
            messages.append(message)
        with open('data.txt', 'a') as file:
            for m in messages:
                s = m.getStr()
                file.write(s.encode('utf-8'))
        tweetCount += len(new_tweets)
        print("Downloaded {0} tweets".format(tweetCount))
        max_id = new_tweets[-1].id
    except tweepy.TweepError as e:
        # Just exit if any error
        print("some error : " + str(e))
        break

print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))

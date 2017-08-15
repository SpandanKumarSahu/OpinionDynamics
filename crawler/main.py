import twitter

config = []
fs = open("config_secret.txt", "r")
for line in fs:
    config.append(line.rstrip())

print config

api = twitter.Api(consumer_key = config[0],
                  consumer_secret = config[1],
                  access_token_key = config[2],
                  access_token_secret = config[3],
                  sleep_on_rate_limit=True)
print (api.VerifyCredentials())

results = api.GetSearch(
    raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100")
print results


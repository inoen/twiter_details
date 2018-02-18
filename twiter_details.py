# coding: utf-8
import config
from twython import Twython, TwythonError

twitter = Twython(config.api_key, config.api_secret, config.access_token, config.token_secret)

response = twitter.search(q='"#100DaysOfCode" -filter:retweets', result_type="recent", count="1")

for log in response['statuses']:
    for key, value in log.items():
        print(key, value)
# coding: utf-8
import config
from twython import Twython, TwythonError

twitter = Twython(config.api_key, config.api_secret, config.access_token, config.token_secret)

response = twitter.search(q='"#100DaysOfCode" -filter:retweets', result_type="recent", count="1")


for tweet in response['statuses']:
    main = (tweet['user']['screen_name']+'::'+tweet['user']['name'])
    print (main.encode("CP932", "replace").decode("CP932"))
    print (type(main))
    text = tweet['text']
    print (text.encode("CP932", "ignore").decode("CP932"))
    print(tweet['created_at'])
    print('----------------------------------------------------')
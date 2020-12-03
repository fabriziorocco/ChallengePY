import tweepy
import pandas as pd


access_token = '1043043366-Kc2mSuKM05B9g3QoeVmymxxZzN8XiFAk8HkRe42'
access_token_secret = 'dcQJ6NoqYAZZu0kxLERxz1yG3Ma8mWFpmvbaZzkQ2DRSJ'
consumer_key = 'eAuZUwSeWhg48MuoJ9J5mVTrX'
consumer_secret = 'LatqHXpgnuhF9JY8OzZ3MAKao64tJQ6uJWUqnYLBuqd4GLUqEF'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

tweets = []

count = 1

search_query = '(from:audi OR from:MercedesBenz OR from:bmw OR from:BMWItalia OR from:AudiIT OR from:MercedesBenz_IT) OR (@audi OR @MercedesBenz OR @bmw OR @BMWItalia OR @AudiIT OR @MercedesBenz_IT)'

for tweet in tweepy.Cursor(api.search, q=search_query, count=2750, since='2020-05-30', wait_on_rate_limit=True).items():

    print(count)
    count += 1

    try:
        data = [tweet.created_at, tweet.id, tweet.text, tweet.user._json['screen_name'], tweet.user._json['name']]
        data = tuple(data)
        tweets.append(data)

    except tweepy.TweepError as e:
        print(e.reason)
        continue

    except StopIteration:
        break

df = pd.DataFrame(tweets,
                  columns=['created_at', 'tweet_id', 'tweet_text', 'screen_name', 'name'])

df.to_csv(path_or_buf='resultsnew_larger.csv', index=False)


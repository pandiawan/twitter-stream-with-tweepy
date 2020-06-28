import json
from datetime import datetime

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = "your-consumer-key-here"
consumer_secret = "your-consumer-secret-here"
access_token = "your-access-token-here"
access_token_secret = "your-access-token-secret-here"


class StdOutListener(StreamListener):
    
    def on_data(self, data):
        d = json.loads(data)

        print("{}: {}\ncreated: {}".format(d["user"]["screen_name"],
                                           d["text"],
                                           datetime.fromtimestamp(int(str(d["timestamp_ms"])[:-3]))
                                           .strftime("%Y-%m-%d %H:%M:%S")))
        print("-" * 50)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    lstnr = StdOutListener()

    # config twitter auth
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, lstnr)
    stream.filter(track=['indonesia'])

from __future__ import absolute_import
import ConfigParser, message, datetime
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

config = ConfigParser.ConfigParser() 
config.read("./config.ini")

consumer_key = config.get('twitter', 'consumer_key')
consumer_secret = config.get('twitter', 'consumer_secret')
access_token = config.get('twitter', 'access_token')
access_token_secret = config.get('twitter', 'access_token_secret')

class tweetListener(StreamListener):
    def on_status(self, status):
        print status.text
        print message.message_to_array(status.text)
        return True

if __name__ == '__main__':
    l = tweetListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['football'])



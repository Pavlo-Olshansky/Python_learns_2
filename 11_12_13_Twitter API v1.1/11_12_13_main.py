import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

c_key = 'xPNTyVLL8u6SF9kL3D0UkcVP0'  #  consumer  key - ключ споживача
c_secret = '22TeTvRKxpoe72drZKYRTKMlnZF4kDPCI5b6GHsz0LDcZICvTT'
a_toket = '3712928596-ryYGVl31JH6F4RDxWSo2B9cmwXZr9M86yi7y2sK'
a_secret = 'GVRZChKjXbhPNdxP0KicTq9i6l7CoLagV3lZruiKiWJgV'


class listener(StreamListener):

    def on_data(self, raw_data):
        try:
            # print(raw_data)
            tweet = raw_data.split(',"text":"')[1].split('","source')[0]
            print(tweet)

            save_this = str(time.time()) + '::' + tweet
            save_file = open('twitDB.csv', 'a')  # comma-separated variables
            save_file.write(save_this)
            save_file.write('\n')
            save_file.close()
            return True
        except BaseException as e:
            print('Filed on_data, ', str(e))
            time.sleep(5)

    def on_error(self, status_code):
        print(status_code)


auth = OAuthHandler(c_key, c_secret)
auth.set_access_token(a_toket, a_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])

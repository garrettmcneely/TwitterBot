# Refrence https://www.youtube.com/watch?v=n5TgwdAbCFk&t=434s

import random
import tweepy

auth = tweepy.OAuthHandler("WHUbfW2rj0J9ygawwO32ePKxU","kQYVQHPzmT6YMo8H5TSXzUkLj4Qnrrlu0M9AqXr600T9T7ABay")
auth.set_access_token("1218203870771412993-KdCsHe9tGeLULxFjKF5fruv2K2yQUU","g0tqPHqye6fjbwQeMtFGV7NrXDg1QkmgDnkIieJIA5rxB")
api = tweepy.API(auth)

dog = "...DOG"
def editTweet (text):
    new = []
   
    
    for y in range(len(text)):
        x = text[y]
        r = random.randint(0,1)
        if r == 1:
            new.append(x.upper())
        else:  
            new.append(x.lower())
    return ''.join(new+[dog])

tweets = api.user_timeline(screen_name = "CaucasianJames")
first_tweet = tweets[0]



for tweet in tweets :
     if tweet.text[0:2] != "RT":
         api.update_with_media('aussie_playing.jpg',"@CaucasianJames {}".format(editTweet(first_tweet.text)),first_tweet.id)
         break
         
         

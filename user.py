# construct user object
# user has a [name, username, email, password]<-- must have, profile picture and tweers[]
# user can tweet or retweet

import csv

class User:

    def __init__(self,name,username,email,password):

        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.prof_pic = "upload a picture"
#   user tweeting action
    def tweet_action(self,tweet_id_,username_,date_time,message_):
        file_exist = os.path.isfile("tweets.csv")

        with open("tweets.csv","a") as tweet_list:

            fieldnames = ["tweet id","username","date created","message"]
            writer = csv.DictWriter(tweet_list,fieldnames=fieldnames)

            if not file_exist:
                writer.writeheader()

            writer.writerow("tweet_id"=tweet_id_,"username"=username_,"date created"=date_time,"message"=message_)

#   user can retweet
    def retweet_action(self,a_retweet):
        self.tweets.append(a_retweet)

#   display a users tweets
    def get_tweets(self):
        pass
        file_exist = os.path.isfile("tweets.csv")
        if file_exist:
            with open("tweets.csv","r") as tweet_list:
                reader = csv.DictReader(tweet_list)
                for row in reader:
                    print()
        # for tweet in self.tweets:
        #     print(tweet)
import csv
import json
from requests_oauthlib import OAuth1Session
import tweepy
import time
import os

api_key = "l7vDtcBNhLJQvjsTGUaxocyaO"
api_key_secret = "PSlzm3s9cZlBBeveHShPFRikPrt1i8hR5UxogfgjLGx6sdsBOj"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAFy2bgEAAAAAouqxA0icYuUETYHgTM0fEoUvaug%3DPbcwSQZVBtiTcKZAhgREpvY3xNILD2OEsmytOVva8Y2DyzoXMs"
access_token = "1516533206366916609-qKpO3nZ7Uj41cYMapuf2vECwXyPuol"
access_token_secret = "On7bZQXX0otohUL4D3SEKkcUSlVpI7eztlGbcNKR98eM7"

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

#Increment in filename

FILE_INDEX = 3

api = tweepy.API(auth, wait_on_rate_limit=True)

cur_path = "/Users/Diane/Twitter-Bot-Detection/Twitter-Bot-Detection/data"

r_user_file = open(os.path.join(cur_path, "real_user.json"))

real_user_file = json.load(r_user_file)

user = real_user_file[FILE_INDEX]

tweets = api.user_timeline(
    user_id=user['profile']['id_str'], trim_user=True)

tweetsId = []

for t in tweets:
    tweetsId.append(t._json["id_str"])

print(tweetsId)
len(tweetsId)

def get_retweets(id):
    try:
        return api.get_retweets(
            id=id, trim_user=True)
    except Exception as e:
        print("error:",e)
        time.sleep(10)
        return get_retweets(id)

def get_followers(id):
    try:
        return api.get_follower_ids(user_id=id)
    except Exception as e:
        print("error:", e)
        time.sleep(10)
        return get_followers(id)

def create_edge_list(rootTweetId, rootUserId, visitedTweets, graphEdges):
    if rootTweetId in visitedTweets:
        print("Duplicate tweets")
        return

    visitedTweets.add(rootTweetId)

    retweetsId =get_retweets(rootTweetId)
    for retweetId in retweetsId:
        graphEdges.append([rootUserId, retweetId._json["user"]["id_str"]])
        create_edge_list(
            retweetId._json["id_str"], retweetId._json["user"]["id_str"], visitedTweets, graphEdges)

    if len(retweetsId) == 0:
        followers = get_followers(rootUserId)
        for f in followers:
            graphEdges.append([rootUserId, f])

    return


graphEdges = []


visitedTweets = set()

for tweetId in tweetsId:
    create_edge_list(
        tweetId, user['profile']['id_str'], visitedTweets, graphEdges)

print("Edges in real graphs: ", len(graphEdges))

with open(os.path.join(cur_path, "real_user_edge_3.csv"), 'w') as f:
    writer = csv.writer(f)
    for row in graphEdges:
        writer.writerow(row)

r_bot_file = open(os.path.join(cur_path, "bot_user.json"))

bot_user_file = json.load(r_bot_file)

bot_user = bot_user_file[FILE_INDEX]

tweets = api.user_timeline(
    user_id=bot_user['profile']['id_str'], trim_user=True)

tweetsId_bot = []

for t in tweets:
    tweetsId_bot.append(t._json["id_str"])

graphEdges_bot = []

visitedTweets_bot = set()

for tweetId in tweetsId_bot:
    create_edge_list(
        tweetId, bot_user['profile']['id_str'], visitedTweets_bot, graphEdges_bot)

print("Edges in bot graph : ", len(graphEdges_bot))

with open(os.path.join(cur_path, "bot_user_edge_3.csv"), 'w') as f:
    writer = csv.writer(f)
    for row in graphEdges_bot:
        writer.writerow(row)


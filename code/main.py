import csv
import json
from requests_oauthlib import OAuth1Session
import tweepy
import time



api_key = "l7vDtcBNhLJQvjsTGUaxocyaO"
api_key_secret = "PSlzm3s9cZlBBeveHShPFRikPrt1i8hR5UxogfgjLGx6sdsBOj"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAFy2bgEAAAAAouqxA0icYuUETYHgTM0fEoUvaug%3DPbcwSQZVBtiTcKZAhgREpvY3xNILD2OEsmytOVva8Y2DyzoXMs"
access_token = "1516533206366916609-qKpO3nZ7Uj41cYMapuf2vECwXyPuol"
access_token_secret = "On7bZQXX0otohUL4D3SEKkcUSlVpI7eztlGbcNKR98eM7"

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

r_user_file = open("real_user.json")

real_user_file = json.load(r_user_file)

real_user_batch_1 = real_user_file[:10]

test_user = real_user_batch_1[2]

tweets = api.user_timeline(
    user_id=test_user['profile']['id_str'], trim_user=True)

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
        tweetId, test_user['profile']['id_str'], visitedTweets, graphEdges)

len(graphEdges)

header = ["source", "target"]

with open('real_test_user_edge_2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in graphEdges:
        writer.writerow(row)

r_bot_file = open("bot_user.json")

bot_user_file = json.load(r_bot_file)

bot_user_batch_1 = bot_user_file[:10]

bot_user = bot_user_batch_1[2]

tweets = api.user_timeline(
    user_id=bot_user['profile']['id_str'], trim_user=True)

tweetsId_bot = []

for t in tweets:
    tweetsId_bot.append(t._json["id_str"])

len(tweetsId_bot)

graphEdges_bot = []

visitedTweets_bot = set()

for tweetId in tweetsId_bot:
    create_edge_list(
        tweetId, bot_user['profile']['id_str'], visitedTweets_bot, graphEdges_bot)

len(graphEdges_bot)

header = ["source", "target"]

with open('real_bot_user_edge_2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in graphEdges_bot:
        writer.writerow(row)


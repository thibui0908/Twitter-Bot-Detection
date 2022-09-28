# Twitter Bot Detection Using Social Network Analysis

This is the repository for Twitter Bot Detection using Social Network Analysis

## Introduction

Twitter is a micro-blogging social media site that provides social networking services. Registered users can post and interact with each other through messages called "tweets", online messages that contains up to 280 characters. Tweets can be re-posted, or "retweeted" and liked, while users can follow each other to stay updated with the latest tweets. Twitter is mainly accessed by most registered users through web browsers and mobile applications. However, registered users also have an option of accessing the platform using Twitter's application programming interface (API). The third access option allows reading and writing on Twitter data. Users can compose tweets, retrieve tweets and profiles, and aggregating data at a high volume using various parameters. These features from the Twitter API have also enabled applications and software to automate and control accounts, and help researchers perform experiments and propose new solutions.

While the API is readily available to registered users, automated applications have to follow automation rules outlined and enforced by Twitter. Although Twitter's terms and conditions do not prohibit bots, they do prohibit malicious usage of such automation such as spamming, malware and violating user privacy. Specifically, as automated accounts can engage and compose content at a much higher volume than a regular human user could, the types of information that such automated accounts produce can convince humans of their content via visibility. In the past decade, the rise of usage in Twitter has produced automated content comparable to human-generated content. In 2016, bots generated content surpassed those of humans, as in the case of 2012 and 2013. Particularly, the malicious usage of bots was the source of a range of problems such as misinformation on social media, spread of conspiracy theories, and political election interference. Twitter insists that bots make up less than 5 percent of its active user base.

## Details

The dataset contains information for labeled users, where we retrieve their tweets and followers. For constructing graphs, we start with the an original tweet from an account, then recursively collects retweets and follower relationships to represent edges and users being nodes. The idea behind this approach is to observe how information propagates in a real user’s social network and a bot’s social network.

![image1](https://user-images.githubusercontent.com/60374374/191357972-546e425b-d879-4dd6-a98b-b592ed1a58e7.png)

## Citation
Please cite Twitter Bot Detection using Social Network Analysis if you use the dataset or this repository
```
Publication Title: 2022 Fourth International Conference on Transdisciplinary AI (TransAI)

Article Title: Twitter Bot Detection using Social Network Analysis

Authors: Thi Bui, Katerina Potika
```

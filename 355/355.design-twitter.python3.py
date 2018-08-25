#
# [355] Design Twitter
#
# https://leetcode.com/problems/design-twitter/description/
#
# algorithms
# Medium (26.07%)
# Total Accepted:    27.5K
# Total Submissions: 105.4K
# Testcase Example:  '["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]\n[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]'
#
# Design a simplified version of Twitter where users can post tweets,
# follow/unfollow another user and is able to see the 10 most recent tweets in
# the user's news feed. Your design should support the following methods:
# 
# 
# 
# postTweet(userId, tweetId): Compose a new tweet.
# getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news
# feed. Each item in the news feed must be posted by users who the user
# followed or by the user herself. Tweets must be ordered from most recent to
# least recent.
# follow(followerId, followeeId): Follower follows a followee.
# unfollow(followerId, followeeId): Follower unfollows a followee.
# 
# 
# 
# Example:
# 
# Twitter twitter = new Twitter();
# 
# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);
# 
# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);
# 
# // User 1 follows user 2.
# twitter.follow(1, 2);
# 
# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);
# 
# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id
# 5.
# twitter.getNewsFeed(1);
# 
# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);
# 
# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);
# 
# 
#
class User:
    def __init__(self, userID):
        self.userID = userID
        self.follower = []
        self.following = []

class News:
    def __init__(self, newsID, userID):
        self.userID = userID
        self.newsID = newsID

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}
        self.news = []
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.users.keys():
            self.users[userId] = User(userId)
        news = News(tweetId, userId)
        self.news.insert(0, news)


        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        result = []
        if userId not in self.users.keys():
            self.users[userId] = User(userId)
        followings = self.users[userId].following
        for news in self.news:
            if len(result) == 10:
                break
            if news.userID == userId or news.userID in followings:
                result.append(news.newsID)
        return result

        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.users.keys():
            self.users[followerId] = User(followerId)
        if followeeId not in self.users.keys():
            self.users[followeeId] = User(followeeId)
        if followeeId not in self.users[followerId].following:
            self.users[followerId].following.append(followeeId)
        if followerId not in self.users[followeeId].follower:
            self.users[followeeId].follower.append(followerId)

        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.users.keys():
            self.users[followerId] = User(followerId)
        if followeeId not in self.users.keys():
            self.users[followeeId] = User(followeeId)
        if followeeId in self.users[followerId].following:
            self.users[followerId].following.remove(followeeId)
        if followerId in self.users[followeeId].follower:
            self.users[followeeId].follower.remove(followerId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

class Twitter:

    def __init__(self):
        self.time=0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))    
        self.time+=1    

    def getNewsFeed(self, userId: int) -> List[int]:
        feeds = set()
        feeds.update(self.tweets[userId][-10:])
        for followers in self.follows[userId]:
            feeds.update(self.tweets[followers][-10:])
        
        res = sorted(feeds,key = lambda x:x[0],reverse=True)[:10]
        return [x[1] for x in res]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        

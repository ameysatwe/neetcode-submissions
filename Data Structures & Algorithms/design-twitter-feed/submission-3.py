class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.count = 0        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        self.followMap[userId].add(userId)
        for fId in self.followMap[userId]:
            if fId in self.tweetMap:
                i = len(self.tweetMap[fId]) - 1
                cnt,tweetId = self.tweetMap[fId][i]
                heapq.heappush(heap,[cnt,tweetId,fId,i-1])
            
        while heap and len(res)<10:
            cnt,tweet,fId,i = heapq.heappop(heap)
            res.append(tweet)
            if i>=0:
                cnt,tweet = self.tweetMap[fId][i]
                heapq.heappush(heap,[cnt,tweet,fId,i-1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

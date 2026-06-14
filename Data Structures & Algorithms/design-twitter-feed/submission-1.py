class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        #Include own tweets and followers
        users = self.following[userId] | {userId}
        for user in users:
            for time, tweetId in self.tweets[user]:
                heapq.heappush(heap, (-time, tweetId))

        #Get 10 most recent
        result = []
        while heap and len(result) < 10:
            time, tweetId = heapq.heappop(heap)
            result.append(tweetId)

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

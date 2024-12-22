class SocialMediaAccount():
    def __init__(self,username,password):
        self.username= username
        self.password= password
    def login():
        pass
    def post():
        pass
    
class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, followers):
        super().__init__(username, password)
        self.followers= followers
    def share_story():
        pass
        
class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, tweets):
        super().__init__(username, password)
        self.tweets= tweets
    def tweets():
        pass
    
user1= InstagramAccount("xshxngg", "12345678", 10000)
user2= TwitterAccount("ashongers", "ABCDEFG", 5000)
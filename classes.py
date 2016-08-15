class User(object):
    #super class
    def __init__(self, name, email, date_joined):
        self.name = name
        self.email = email
        self.date_joined = date_joined

class repo(object):
    def __init__(self, name, date_created):
        self.name = name
        self.date_created = date_created

class contributions(object):
    def __init__(self, name, no_of_code_lines):
        self.name = name
        self.no_of_code_lines = no_of_code_lines



class GithubUser(User):
    """GithubUser is a User"""
    def __init__(self, name, email):
        super(GithubUser, self).__init__(name, email)
        self.repos = []
        self.contributions = []
        self.followers = []
        self.following = []

    def follow(self, user):
        """Follow another user : arg=User object"""
        user.followers.append(self)
        self.following.append(user)

    def __repr__(self):
        return "<Github user " + self.name + ", " +\
            self.email + ", " + str(self.date_joined) + ">"


stan = GithubUser("Stan", "stan@gmail.com")
amos = GithubUser("Amos", "amos@gmail.com")
joan = GithubUser("Joan", "joan@gmail.com")
srepo = Repository("repo1", stan)
contrib1 = Contribution(amos, 100, srepo)
stan.follow(joan)
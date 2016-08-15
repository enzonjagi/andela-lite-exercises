from datetime import datetime

class user(object):
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.date_joined = datetime.now()
    def __repr__(self):
        return "<user " + self.name + ">"

class repo(object):
    def __init__(self, name, creator):
        self.name = name
        self.creator = creator
        self.date_created = datetime.now()

class contribution(object):
    def __init__(self, name, no_of_contributions):
        self.name = name
        


class github_user(user):
    def __init__(self, name, date_joined, repositories, followers, following, contributions):
        super(github_user, self).__init__(name, date_joined)

    def no_of_repositories(repositories):

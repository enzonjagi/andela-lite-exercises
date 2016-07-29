class repo(object):
    def __init__(self, name, date_created):
        self.name = name
        self.date_created = date_created


class user(object):
    def __init__(self, name, date_joined):
        self.name = name
        self.date_joined = date_joined

class contribution(object):
    def __init__(self, name, no_of_contributions):
        self.name = name
        self.no_of_contributions = no_of_contributions


class github_user(user):
    def __init__(self, name, date_joined, repositories, followers, following, contributions):
        super(github_user, self).__init__(name, date_joined)

    def no_of_repositories(repositories):
        

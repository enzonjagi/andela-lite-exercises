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



class github_user(User):
     def __init__(self, name, email, date_joined):
         super(github_user, self).__init__(name, email, date_joined)
         self.repo_list = []
         self.followers = []
         self.following = []
         self.contributions = []

     def add_repo(self, name, date_created):
         repo = repo(name, date_created)
         repo_list.append(repo)

     def follow():

from github import Github
from glass.hoster import GitHoster

class GitHubHoster(GitHoster):
    def __init__(self, username, token):
        self.gh = Github(token)
    
    def repositories(self):
        return [repo.clone_url for repo in self.gh.get_user().get_repos()]

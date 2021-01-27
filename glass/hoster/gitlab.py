import gitlab
from glass.hoster import GitHoster

class GitLabHoster(GitHoster):
    def __init__(self, url, token):
        self.gl = gitlab.Gitlab(url, token)
    
    def repositories(self):
        return [f'{repo.web_url}.git' for repo in self.gl.projects.list(all=True)]

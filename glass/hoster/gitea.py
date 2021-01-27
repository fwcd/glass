import gitea
from glass.hoster import GitHoster

class GiteaHoster(GitHoster):
    def __init__(self, url, token):
        self.gt = gitea.Gitea(url, token)
    
    def repositories(self):
        return [
            repo.clone_url.replace('http:', 'https:')
            for org in self.gt.get_user().get_repositories()
            for repo in org.get_repositories()
        ]

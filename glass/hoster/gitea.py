import gitea
from glass.hoster import GitHoster

class GiteaHoster(GitHoster):
    def __init__(self, url: str, token: str):
        self.gt = gitea.Gitea(url, token)
    
    def repositories(self) -> list[str]:
        return [
            repo.clone_url.replace('http:', 'https:')
            for org in self.gt.get_user().get_repositories()
            for repo in org.get_repositories()
        ]

import github
from glass.hoster import GitHoster

class GitHubHoster(GitHoster):
    def __init__(self, token: str):
        self.gh = github.Github(token)
    
    def repositories(self) -> list[str]:
        return [repo.clone_url for repo in self.gh.get_user().get_repos()]

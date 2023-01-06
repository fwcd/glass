from github import Github
from github.Repository import Repository

from glass.hoster import GitHoster

class GitHubHoster(GitHoster):
    def __init__(self, token: str):
        self.token = token
        self.gh = Github(token)
    
    def repositories(self) -> list[str]:
        return [self.clone_url(repo) for repo in self.gh.get_user().get_repos()]
    
    def clone_url(self, repo: Repository) -> str:
        return f'https://oauth2:{self.token}@github.com/{repo.full_name}.git'

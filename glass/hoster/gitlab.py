from gitlab import Gitlab

from glass.hoster import GitHoster

class GitLabHoster(GitHoster):
    def __init__(self, url: str, token: str):
        self.gl = Gitlab(url, token)
    
    def repositories(self) -> list[str]:
        return [f'{repo.web_url}.git' for repo in self.gl.projects.list(all=True)]

from glass.hoster import GitHoster

class SingleRepoGitHoster(GitHoster):
    def __init__(self, url: str):
        self.url = url

    def repositories(self) -> list[str]:
        return [self.url]


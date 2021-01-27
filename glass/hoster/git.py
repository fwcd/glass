from glass.hoster import GitHoster

class SingleRepoGitHoster(GitHoster):
    def __init__(self, url):
        self.url = url

    def repositories(self):
        return [url]


class GitHoster:
    def repositories(self) -> list[str]:
        '''Fetches a list of repo URLs.'''
        raise NotImplementedError(f'{__name__} does not provide repositories.')

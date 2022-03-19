import argparse
import json
import os
from pathlib import Path

from glass.hoster.git import SingleRepoGitHoster
from glass.hoster.github import GitHubHoster
from glass.hoster.gitlab import GitLabHoster
from glass.hoster.gitea import GiteaHoster
from glass.mirror import mirror_repo

DEFAULT_CONFIG_PATH = Path.home() / '.config' / 'glass' / 'config.json'
HOSTERS = {
    'github': lambda acc: GitHubHoster(acc['token']),
    'gitlab': lambda acc: GitLabHoster(acc['url'], acc['token']),
    'gitea': lambda acc: GiteaHoster(acc['url'], acc['token']),
    'git': lambda _: SingleRepoGitHoster()
}

def main():
    parser = argparse.ArgumentParser(description='Tool for mirroring GitHub repositories.')
    parser.add_argument('--config', required=not DEFAULT_CONFIG_PATH.exists(), default=str(DEFAULT_CONFIG_PATH), help='Path to your config.json')

    args = parser.parse_args()
    with open(args.config, 'r') as f:
        config = json.loads(f.read())
    
    target_dir = Path(config['targetDir'])
    accounts = config['accounts']

    for account in accounts:
        acc_type = account['type']
        acc_name = account['name']

        if acc_type in HOSTERS:
            hoster = HOSTERS[acc_type](account)
            print(f"Querying {acc_name}...")
            repo_urls = hoster.repositories()
            print(f"Found {len(repo_urls)} repo(s) on {acc_name}...")

            for url in repo_urls:
                mirror_repo(url, target_dir / acc_name)
        else:
            raise ValueError(f"Unknown account type '{acc_type}'")


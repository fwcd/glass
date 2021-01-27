import argparse
import json
import os

from glass.hoster.git import SingleRepoGitHoster
from glass.hoster.github import GitHubHoster
from glass.mirror import mirror_repo

HOSTERS = {
    'github': lambda acc: GitHubHoster(acc['username'], acc['token']),
    'git': lambda _: SingleRepoGitHoster()
}

def main():
    parser = argparse.ArgumentParser(description='Tool for mirroring GitHub repositories.')
    parser.add_argument('--config', required=True, help='Path to your config.json')

    args = parser.parse_args()
    with open(args.config, 'r') as f:
        config = json.loads(f.read())
    
    target_dir = config['targetDir']
    accounts = config['accounts']

    for account in accounts:
        acc_type = account['type']
        acc_desc = account['description']
        hoster = HOSTERS[acc_type](account)

        if hoster:
            repo_urls = hoster.repositories()
            print(f"Found {len(repo_urls)} repo(s) on {acc_desc}...")
            for url in repo_urls:
                mirror_repo(url, os.path.join(target_dir, acc_desc))
        else:
            raise ValueError(f"Unknown account type '{acc_type}'")


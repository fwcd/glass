import argparse
import json

from glass.hoster.github import GitHubHoster
from glass.mirror import mirror_repo

HOSTERS = {
    'github': lambda acc: GitHubHoster(acc['username'], acc['token'])
}

def main():
    parser = argparse.ArgumentParser(description='Tool for mirroring GitHub repositories.')
    parser.add_argument('--config', required=True, help='Path to your config.json')

    args = parser.parse_args()
    with open(args.config, 'r') as f:
        config = json.loads(f.read())
    
    for account in config['accounts']:
        hoster = HOSTERS[account['type']](account)
        if hoster:
            repo_urls = hoster.repositories()
            print(f"Found {len(repo_urls)} repo(s) on {account['description']}...")
            for url in repo_urls:
                mirror_repo(url, account['targetDir'])
        else:
            raise ValueError(f"Unknown account type {account['type']}")


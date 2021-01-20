import argparse
import json

from glass.hoster.github import GitHubHoster
from glass.mirror import mirror_repo

HOSTERS = {
    'github': GitHubHoster()
}

def main():
    parser = argparse.ArgumentParser(description='Tool for mirroring GitHub repositories.')
    parser.add_argument('--config', required=True, help='Path to your config.json')

    args = parser.parse_args()
    with open(args.config, 'r') as f:
        config = json.loads(f.read())
    
    for account in config['accounts']:
        hoster = HOSTERS[account['type']]
        if hoster:
            for url in hoster.repositories():
                mirror_repo(url, account['target_dir'])
        else:
            raise ValueError(f"Unknown account type {account['type']}")


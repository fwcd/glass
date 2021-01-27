import subprocess
from pathlib import Path
from urllib.parse import urlparse

def mirror_repo(repo_url, target_dir):
    target_dir.mkdir(parents=True, exist_ok=True)
    repo_dir = Path(str(target_dir) + urlparse(repo_url).path)

    if repo_dir.exists():
        print(f'Updating from {repo_url}...')
        subprocess.run(['git', 'remote', 'update'], cwd=str(repo_dir))
    else:
        print(f'Mirroring from {repo_url}...')
        subprocess.run(['git', 'clone', repo_url, '--mirror'], cwd=str(repo_dir.parent))

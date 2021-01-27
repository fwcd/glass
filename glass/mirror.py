import os
import subprocess

def mirror_repo(repo_url, target_dir):
    dir_name = repo_url.rsplit('/', 1)[-1]
    repo_dir = os.path.join(target_dir, dir_name)

    if os.path.exists(repo_dir):
        print(f'Updating from {repo_url}...')
        subprocess.run(['git', 'remote', 'update'], cwd=repo_dir)
    else:
        print(f'Mirroring from {repo_url}...')
        subprocess.run(['git', 'clone', repo_url, '--mirror'], cwd=target_dir)

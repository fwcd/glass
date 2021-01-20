import subprocess

def mirror_repo(repo_url, target_dir):
    dir_name = repo_url.rsplit('/', 1)[-1]
    code = subprocess.run(['git', 'clone', repo_url, '--mirror'], cwd=target_dir).returncode
    if code == 0:
        print(f'Mirrored {repo_url}')
    else:
        subprocess.run(['git', 'remote', 'update'], cwd=f'{target_dir}/{dir_name}')
        print(f'Updated {repo_url}')

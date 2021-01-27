import subprocess

def mirror_repo(repo_url, target_dir):
    target_dir.mkdir(parents=True, exist_ok=True)

    # TODO: Mirror repo to path under username/group/subgroup dir
    dir_name = repo_url.rsplit('/', 1)[-1]
    repo_dir = target_dir / dir_name

    if repo_dir.exists():
        print(f'Updating from {repo_url}...')
        subprocess.run(['git', 'remote', 'update'], cwd=repo_dir)
    else:
        print(f'Mirroring from {repo_url}...')
        subprocess.run(['git', 'clone', repo_url, '--mirror'], cwd=str(target_dir))

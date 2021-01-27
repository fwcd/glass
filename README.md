# Glass

A tool that mirrors repositories from your online Git hosting accounts, including from GitHub, GitLab and Gitea.

## Usage

To use, create a `config.json` using any combination of the listed account types:

```json
{
    "targetDir": "<path/to/your/local/mirroring/folder>",
    "accounts": [
        {
            "description": "your-github",
            "type": "github",
            "token": "<your personal access token>"
        },
        {
            "description": "your-gitlab",
            "type": "gitlab",
            "url": "<https://your.gitlab>",
            "token": "<your personal access token>"
        },
        {
            "description": "your-gitea",
            "type": "gitea",
            "url": "<https://your.gitea>",
            "token": "<your personal access token>"
        },
        {
            "description": "a-single-repo",
            "type": "git",
            "url": "<https://your.host/repo.git>"
        }
    ]
}
```

The directory structure generated by `glass` will look similar to the following:

```
targetDir
├ your-github
│ ├ your-account
│ │ ├ repo1.git   <- https://github.com/your-account/repo1.git
│ │ ├ repo2.git   <- https://github.com/your-account/repo2.git
│ ...
├ your-gitlab
│ ├ your-account
│ │ ├ repo1.git   <- https://your.gitlab/your-account/repo1.git
│ │ ├ repo2.git   <- https://your.gitlab/your-account/repo2.git
├ your-gitea
│ ├ your-account
│ │ ├ repo1.git   <- https://your.gitea/your-account/repo1.git
│ │ ├ repo2.git   <- https://your.gitea/your-account/repo2.git
│ ...
├ a-single-repo
│ └ repo.git      <- https://your.host/repo.git
...
```

Make sure that your token has permissions to read and clone the repositories you intend to mirror. Then launch the program with

```
python3 -m glass --config <path/to/config.json>
```

Alternatively, you can place the config file in `~/.config/glass/config.json` and omit the argument:

```
python3 -m glass
```

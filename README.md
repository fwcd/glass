# Glass

A tool that mirrors every repository from a list of GitHub accounts.

## Usage

To use, create a `config.json` with the following contents:

```
{
    "accounts": [
        {
            "type": "github",
            "username": "<your username>",
            "token": "<your personal access token>",
            "targetDir": "<path/to/where/the/repos/should/be/placed>"
        }
    ]
}
```

Make sure that your token has permissions to read and clone the repositories you intend to mirror. Then launch the program with

```
python3 -m glass --config <path/to/config.json>
```

# Glass

A tool that mirrors all repositories from a given GitHub account.

## Usage

To use, create a `config.json` with the following contents:

```
{
    "accounts": [
        {
            "type": "github",
            "token": "<your personal access token>",
            "targetDir": "<path/to/where/the/repos/should/be/placed>"
        }
    ]
}
```

Then launch the program with

```
python3 -m glass --config <path/to/config.json>
```

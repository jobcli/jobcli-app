# JobCLI

## Features
- More than 10k active jobads from companies in the US and Germany (for now)
- Simple command line interface
- CSV or JSON output


## Installation
```bash
$ pip install jobcli
```

## Usage
To list all engineering jobs in the US, do:
```bash
$ jobcli -j engineer -c US
```
To list frontend jobads in Germany that mention 'react', do:
```bash
$ jobcli -j frontend -c DE -s react
```


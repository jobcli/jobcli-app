# JobCLI
### Job Search from the Command Line

![Screencast](https://s3.amazonaws.com/aws-website-jobclicom-iq2rf/assets/img/screencast.gif)

## Features
- :earth_americas: More than 10k active jobads from companies in :us: and :de: (for now)
- :cool: Simple command line interface
- :open_file_folder: CSV or JSON output


## :books: Documentation

## :electric_plug: Installation
```bash
$ pip install jobcli
```

## :computer: Usage
To list all engineering jobs in the US, do:
```bash
$ jobcli -j engineer -c US
```
To list frontend jobads in Germany that mention 'react', do:
```bash
$ jobcli -j frontend -c DE -s react
```


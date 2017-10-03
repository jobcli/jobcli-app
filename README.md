# JobCLI
## Job Search from the Command Line

## Features
- Tech jobs from companies in :us: and :de: (for now)
- Simple command line interface
- CSV or JSON output

![Screencast]()

## :electric_plug: Installation
```bash
$ pip install jobcli
```

## :computer: Usage

To list all available options in your command line, do:
```bash
$ jobcli --help

Usage: jobcli [OPTIONS]

  JobCLI: Your Command Line Job Board

Options:
  -c, --country [US|DE]    iso-alpha2 country code
  -l, --location TEXT      city
  -j, --jobtitle TEXT      job title
  -s, --skills TEXT        search terms
  -f, --firm TEXT          company name
  -p, --page INTEGER       search result page
  -o, --output [CSV|JSON]  output format
  -v, --version            Show the version and exit.
  --help                   Show this message and exit.
```

### Example 1
To list all engineering jobs in the US, do:
```bash
$ jobcli -j engineer -c US
```

### Example 2
To list front-end jobs in Germany that mention 'react' in their description, do:
```bash
$ jobcli -j frontend -c DE -s react
```


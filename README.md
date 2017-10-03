# JobCLI
### Job search from the command line

## Features
- More than 15K jobs in software development, engineering and data science 
- Companies in :us: and :de: (for now)
- Simple command line interface
- CSV or JSON output

## :electric_plug: Installation
```
$ pip install jobcli
```

## :computer: Usage

To list all available options in your command line, do:
```
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
```
$ jobcli -j engineer -c US
```

### Example 2
To list front-end jobs in Germany that mention 'react' in their description, do:
```
$ jobcli -j frontend -c DE -s react
```

### Pretty-printing
#### CSV
For csv output, [csvkit](https://csvkit.readthedocs.io/en/1.0.2/) comes with `csvlook`:
```
$ jobcli | csvlook | head

| url                        | jobtitle                                              | company              | location             | country | page |
| -------------------------- | ----------------------------------------------------- | -------------------- | -------------------- | ------- | ---- |
| http://jobcli.com/9xUIe0Ju | UX Research Analyst                                   | Quantix/Protech      | Cleveland, OH        | US      | 1    |
| http://jobcli.com/QPnZx-Kk | senior systems engineer, Starbucks Technology - Se... | Starbucks            | Seattle, WA          | US      | 1    |
| http://jobcli.com/qEP3KyUV | Drafter/Designer                                      | UPMC                 | New York, NY         | US      | 1    |
| http://jobcli.com/pKlL-WbP | Project Manager (HVAC)/Systems Specialist             | Johnson Controls     | Syosset, NY          | US      | 1    |
| http://jobcli.com/NPnYSJbV | Aem Developer                                         | TCS                  | Cleveland, OH        | US      | 1    |
| http://jobcli.com/4gu9gW3q | Floral Designer                                       | Daniels Foods Sentry | Walworth, WI         | US      | 1    |
| http://jobcli.com/sXgOPNlq | Android Developer                                     | BuzzHero             | San Francisco, CA    | US      | 1    |
| http://jobcli.com/GuVB_NUi | Graphic Designer                                      | Jillian's Circus     | Oceanside, NY        | US      | 1    |
```
You can install csvkit with pip:
```
$ pip install csvkit
```

![Screencast](https://s3.amazonaws.com/aws-website-jobclicom-iq2rf/assets/img/screencast.gif)


#### JSON
For json output, there's a handy tool in the python standard library:
```
$ jobcli -o json | python -m json.tool | less

[
    {
        "url": "http://jobcli.com/9xUIe0Ju",
        "jobtitle": "UX Research Analyst",
        "company": "Quantix/Protech",
        "location": "Cleveland, OH",
        "country": "US",
        "page": 1
    },
    {
        "url": "http://jobcli.com/qEP3KyUV",
        "jobtitle": "Drafter/Designer",
        "company": "UPMC",
        "location": "New York, NY",
        "country": "US",
        "page": 1
    },
    [...]
```


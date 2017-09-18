#!/usr/local/bin/python3
import click
import requests
import sys
import urllib.parse


def validate_output(ctx, param, value):
    o = value.lower()
    if o == 'csv':
        return 'text/csv; charset=utf8'
    if o == 'json':
        return 'application/json; charset=utf8'
    else:
        raise click.BadParameter('Output needs to be csv or json.')


def validate_country(ctx, param, value):
    if len(value) == 2:
        return value.lower()
    else:
        raise click.BadParameter('Country needs to be valid ISO-alpha2 code.')


@click.command()
@click.option('--country' , '-c', default ='US' , help='iso-alpha2'  , callback=validate_country )
@click.option('--location', '-l', default =''   , help='city'                                    )
@click.option('--jobtitle', '-j', default =''   , help='job title'                               )
@click.option('--skills'  , '-s', default =''   , help='search terms (comma-separated)'          )
@click.option('--firm'    , '-f', default =''   , help='company name'                            )
@click.option('--output'  , '-o', default ='csv', help='csv | json'  , callback=validate_output  )


def download_jobs(jobtitle, country, location, output, firm, skills):
    """Commandline job board"""
    url     = 'http://api.jobcli.com:3000/rpc/ads'
    headers = {'Accept': output}
    payload = {
               "country"  : country
              ,"location" : location
              ,"company"  : firm
              ,"jobtitle" : jobtitle
              ,"skills"   : skills
    }

    r = requests.post(url, headers=headers, data=payload)
   #sys.stdout.write(r.url)
   #sys.stdout.write('\n\n')
    sys.stdout.write(r.text)


if __name__ == '__main__':
    download_jobs()


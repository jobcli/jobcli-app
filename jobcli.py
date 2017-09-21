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
        raise click.BadParameter('Output type must be CSV or JSON.')


def validate_country(ctx, param, value):
    if len(value) == 2:
        return value.lower()
    else:
        raise click.BadParameter('Country must be ISO-alpha2 code.')


@click.command()
@click.option('--country', '-c', default ='US', help='iso-alpha2'
              , callback=validate_country )
@click.option('--location', '-l', default ='', help='city' )
@click.option('--jobtitle', '-j', default ='', help='job title' )
@click.option('--skills', '-s', default ='', help='search terms' )
@click.option('--firm', '-f', default ='', help='company name' )
@click.option('--output', '-o', default ='csv', help='csv | json'
              , callback=validate_output )

def cli(jobtitle, country, location, output, firm, skills):
    """Command Line Job Board"""
    url     = 'http://api.jobcli.com/rpc/ads'
    headers = {'Accept': output}
    payload = {
               "country"  : country
              ,"location" : location
              ,"company"  : firm
              ,"jobtitle" : jobtitle
              ,"skills"   : skills
    }
    try:
        r = requests.post(url, headers=headers, data=payload)
        sys.stdout.write(r.text)
    except:
        raise click.ClickException('The JobCLI server could not be reached at this moment.')


if __name__ == '__main__':
    cli()


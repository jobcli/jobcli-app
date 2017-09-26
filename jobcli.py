import click
import requests
import sys


def validate_output(ctx, param, value):
    o = value.lower()
    if o == 'csv':
        return 'text/csv; charset=utf8'
    if o == 'json':
        return 'application/json; charset=utf8'
    else:
        raise click.BadParameter('Output type must be CSV or JSON.')

CONTEXT_SETTINGS = dict(token_normalize_func=lambda x: x.lower())

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--country', '-c', default ='US', help='iso-alpha2 country code'
              , type=click.Choice(['US', 'DE']))
@click.option('--location', '-l', default ='', help='city')
@click.option('--jobtitle', '-j', default ='', help='job title')
@click.option('--skills', '-s', default ='', help='search terms')
@click.option('--firm', '-f', default ='', help='company name')
@click.option('--page', '-p', default = 1, help='search result page')
@click.option('--output', '-o', default ='csv', help='output format'
              , type=click.Choice(['CSV', 'JSON'])
              , callback=validate_output)
@click.version_option('0.1b1', '--version', '-v')

def cli(jobtitle, country, location, output, firm, skills, page):
    """JobCLI: Your Command Line Job Board"""
    url     = 'http://api.jobcli.com/rpc/ads'
    headers = {'Accept': output}
    payload = {
               "country"  : country
              ,"location" : location
              ,"company"  : firm
              ,"jobtitle" : jobtitle
              ,"skills"   : skills
              ,"page"     : page
    }
    try:
        r = requests.post(url, headers=headers, data=payload)
        sys.stdout.write(r.text)
    except:
        raise click.ClickException('The JobCLI server could not be reached at this moment.')


if __name__ == '__main__':
    cli()


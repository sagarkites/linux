import click
import os
'''
click-arguments must be passed as the function arguments
'''
@click.command()
@click.option('--p', type=str, help='Package Installer.')

def cli(p):
    i = os.system('sudo yum install -y {}'.format(p))
    click.echo('Installed {} is '.format(i))

if __name__ == '__main__':
   cli()

import click
import requests
import json as js_pck
from helpers import export


@click.group()
def ah():
    pass


@ah.command()
@click.option('--save', is_flag=True, default=False)
@click.option('--json', is_flag=True, default=False)
@click.option('--csv', is_flag=True, default=False)
@click.argument('article', default=False)
def view(article, save, json, csv):
    url = 'https://ah-premier-staging.herokuapp.com/api/articles/{}'.format(
        article)
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        article = js_pck.dumps(data['article'], indent=2)
        slug = data['article']['slug']
        click.echo(article)
        if save:
            filename = slug
            if json:
                export.export_json(filename, data)
            elif csv:
                export.export_csv(filename=filename, data=dict(data['article']))
    elif res.status_code == 404:
        click.echo('🙀 🙀 🙀 🙀 The article does no exist 🙀 🙀 🙀 🙀')
    else:
        click.echo('🙀 🙀 🙀 🙀 Oops an error occured 🙀 🙀 🙀 🙀')


@ah.command()
@click.option('--save', is_flag=True, default=False)
@click.option('--json', is_flag=True, default=False)
@click.option('--csv', is_flag=True, default=False)
def list(save, json, csv):
    url = 'https://ah-premier-staging.herokuapp.com/api/articles/'
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        articles = js_pck.dumps(data['articles'], indent=2)
        click.echo(articles)
        if save:
            filename = 'all_articles'
            if json:
                export.export_json(filename=filename, data=data)
            elif csv:
                export.export_csv(filename='all_articles',
                                  data=data['articles'])
    else:
        click.echo('🙀 🙀 🙀 🙀 Oops an error occured 🙀 🙀 🙀 🙀')

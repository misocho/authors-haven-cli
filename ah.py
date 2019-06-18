import click
import requests
import json
@click.group()
def ah():
    pass


@ah.command()
@click.argument('article', default=False)
def view(article, json):
    url = 'https://ah-premier-staging.herokuapp.com/api/articles/{}'.format(
        article)
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        article = json.dumps(data['article'], indent=2)
        click.echo(article)
    elif res.status_code == 404:
        click.echo('🙀 🙀 🙀 🙀 The article does no exist 🙀 🙀 🙀 🙀')
    else:
        click.echo('🙀 🙀 🙀 🙀 Oops an error occured 🙀 🙀 🙀 🙀')

@ah.command()
def list():
    url = 'https://ah-premier-staging.herokuapp.com/api/articles/'
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        articles = json.dumps(data['articles'], indent=2)
        click.echo(articles)
    else:
        click.echo('🙀 🙀 🙀 🙀 Oops an error occured 🙀 🙀 🙀 🙀')

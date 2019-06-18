import click
import requests
@click.group()
def ah():
    pass

@ah.command()
@click.argument('article', default=False)
def view(article):
    url = 'https://ah-premier-staging.herokuapp.com/api/articles/{}'.format(
        article)
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        article = data['article']
        click.echo(article)
    elif res.status_code == 404:
        click.echo('🙀 🙀 🙀 🙀 The article does no exist 🙀 🙀 🙀 🙀')
    else:
        click.echo('🙀 🙀 🙀 🙀 Oops an error occured 🙀 🙀 🙀 🙀')

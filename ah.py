import click
import requests
import json as js_pck
from helpers import export


@click.group()
def ah():
    pass


@ah.command()
@click.option('--save', is_flag=True, default=False, help="Save the article")
@click.option('--json', is_flag=True, default=False)
@click.option('--csv', is_flag=True, default=False)
@click.argument('article', default=False)
def view(article, save, json, csv, limit, page):
    '''
    view <article_slug> to view a specific article \
    view <article_slug> --save --json to save in JSON \
    view <article_slug> --save --csv to save in CSV \
    '''
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
                export.export_csv(filename=filename,
                                  data=dict(data['article']))
    elif res.status_code == 404:
        click.echo('🙀 🙀 🙀 🙀 The article does no exist 🙀 🙀 🙀 🙀')
    else:
        click.echo('🙀 🙀 🙀 🙀 Oops an error occured 🙀 🙀 🙀 🙀')


@ah.command()
@click.option('--save', is_flag=True, default=False)
@click.option('--json', is_flag=True, default=False)
@click.option('--csv', is_flag=True, default=False)
@click.option('--limit', type=int, default=5)
@click.option('--page', type=int, default=1)
@click.pass_context
def list(ctx, save, json, csv, limit, page):
    ''' List all articles '''
    url = ('https://ah-premier-staging.herokuapp.com/api/articles'
           '?page_size={}&page={}'.format(limit, page))
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
        next_article = click.prompt(
            "Type [n] to go to the next page, [q] to exit", default='q'
        )
        if next_article.lower() == 'n':
            ctx.invoke(
                list, limit=limit, save=False, page=page+1
            )
    else:
        click.echo('🙀 🙀 🙀 🙀 Oops an error occured 🙀 🙀 🙀 🙀')

# Authors Haven Cli App
This is a cli app that consumes some of the endpoints of the authors haven backend app

### Instalation
- Clone the [repo](https://github.com/misocho/authors-haven-cli.git)
- Navigate into the project directory
```
$ cd authors-haven-cli
```
- Create and activate a virtual environment
```
$ virtualenv env
$ source env/bin/activate
```
- Install the dependencies and app
```
$ pip install --editable .
```
- To confirm the install run:
```
$ ah --help
```
- You should receive a list of commands and help text
```
Usage: ah [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  list    List all articles
  search  Search for an article
  view    view <article_slug> to view a specific article view
          <article_slug>...
```

### Commands
- List all articles
```
$ ah list
```
- View a specific article
```
$ ah view <article_slug>
```
- Save a specific article as JSON
```
$ ah view <article_slug> --save --json
```
- Save a specific article as CSV
```
$ ah view <article_slug> --save --csv
```
- Save all articles as JSON
```
$ ah list --save --json
```
- Save all articles as CSV
```
$ ah list --save --csv
```
- Search for an article title
```
$ ah search <title_key_word>
```
- Limit number of articles
```
$ ah list --limit <limit_as_int>
```
- Select page after limit
```
$ ah list --limit <limit_as_int> --page <page_as_int>
```

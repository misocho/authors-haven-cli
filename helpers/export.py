import json
import os
import click
import csv


def create_dir():
    if not os.path.isdir('./articles'):
        os.mkdir('./articles')


def export_json(filename='json_export', data=None):
    create_dir()
    with click.open_file('./articles/'+filename+'.json', 'w') as js_file:
        js_file.write(json.dumps(data, indent=2))


def export_csv(filename='csv_export', data=None):
    create_dir()
    with click.open_file('./articles/' + filename + '.csv', 'w') as csv_file:
        if type(data) == list:
            data_keys = data[0].keys()
            write_csv = csv.DictWriter(csv_file, data_keys)
            write_csv.writeheader()
            write_csv.writerows(data)
        else:
            data_keys = data.keys()
            write_csv = csv.DictWriter(csv_file, data_keys)
            write_csv.writeheader()
            write_csv.writerow(data)

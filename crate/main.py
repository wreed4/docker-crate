import click
import yaml
from . import types


@click.command()
def main():
    with open('crates.yml') as f:
        data = yaml.load(f)

    crates = [types.Crate(key, **d) for key, d in data.items()]

    test = crates[0]
    test.run()


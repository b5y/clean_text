# -*- coding: utf-8 -*-
# import sys
# import os.path
#
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import logging
import click

from clean_text.cleaner import clean_text

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
def cli():
    pass


@cli.command()
@click.argument('text_file_s',
                required=True,
                nargs=1,
                type=click.Path(exists=True, resolve_path=True),
                metavar="<path or file>")
def run(text_file_s=basestring):
    clean_text(text_file_s)
    logger.info('\nTexts cleaned successfully\n')


def main():
    cli()


if __name__ == '__main__':
    main()

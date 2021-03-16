# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
[options.entry_points] section in setup.cfg:

    console_scripts =
         fibonacci = auto_boilerplate.skeleton:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""

import argparse
import sys
import os
import logging

from auto_boilerplate import __version__
from auto_boilerplate.Data import Data
from auto_boilerplate.file_tools.FileTools import FileTools
from auto_boilerplate.file_tools.IFileTools import IFileTools
from auto_boilerplate.file_tools.NoopFileTools import NoopFileTools

__author__ = "Kuklin István"
__copyright__ = "Kuklin István"
__license__ = "ALL RIGHTS RESERVED"

_logger = logging.getLogger(__name__)


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Extracts boilerplates from a boilerplates.yml file")
    parser.add_argument(
        "--version",
        action="version",
        version="auto-boilerplate {ver}".format(ver=__version__))
    parser.add_argument(
        dest="yml_path",
        help="boilerplates.yml path",
        type=str,
        metavar="yml_path")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO)
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG)
    parser.add_argument(
        "-e",
        "--execute",
        dest="execute",
        help="Pass this NOT to dry run",
        action="store_true"
    )
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)

    yml_path = os.path.abspath(args.yml_path)

    if args.execute:
        file_tools: IFileTools = FileTools()
    else:
        file_tools: IFileTools = NoopFileTools()

    data = Data.from_yaml(args.yml_path)

    for file_template in data.get_file_list_to_be_created():
        file_tools.overwrite(file_template.path, file_template.content)


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()

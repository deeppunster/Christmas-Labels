"""
ChristmasLabels.py - Manage christmas labels program.
"""

import logging
import logging.config
import yaml  # from PyYAML library
from logging import getLogger, debug, error
from pathlib import Path
from typing import Any, Union, Optional

from ChristmasLabelsPkg.ChristmasLabelsGUI import MainMenuFrame

__author__ = 'Travis Risner'
__project__ = "Christmas-Labels"
__creation_date__ = "03/07/2019"
# Copyright 2019 by Travis Risner - MIT License

log = None


class ChristmasLabelsClass:
    """
    ChristmasLabelsClass - Manage christmas labels user interface.
    """

    def __init__(self):
        self.clg = MainMenuFrame()

    def run_CLbls(self):
        """
        Top method for running Run the Christmas labels user interface..

        :return:
        """
        pass


class Main:
    """
    Main class to start things rolling.
    """

    def __init__(self):
        """
        Get things started.
        """
        self.ChrLbls = None
        return

    def run_ChrLbls(self):
        """
        Prepare to run Run the Christmas labels user interface..

        :return:
        """
        self.ChrLbls = ChristmasLabelsClass()
        debug('Starting up ChrLbls')
        self.ChrLbls.run_CLbls()
        return

    @staticmethod
    def start_logging(work_dir: Path, debug_name: str):
        """
        Establish the logging for all the other scripts.

        :param work_dir:
        :param debug_name:
        :return: (nothing)
        """

        # Set flag that no logging has been established
        logging_started = False

        # find our working directory and possible logging input file
        _workdir = work_dir
        _logfilename = debug_name

        # obtain the full path to the log information
        _debugConfig = _workdir / _logfilename

        # verify that the file exists before trying to open it
        if Path.exists(_debugConfig):
            try:
                #  get the logging params from yaml file and instantiate a log
                with open(_logfilename, 'r') as _logdictfd:
                    _logdict = yaml.load(_logdictfd)
                logging.config.dictConfig(_logdict)
                logging_started = True
            except Exception as xcp:
                print(f'The file {_debugConfig} exists, but does not contain '
                      f'appropriate logging directives.')
                raise ValueError('Invalid logging directives.')
        else:
            print(f'Logging directives file {_debugConfig} either not '
                  f'specified or not found')

        if not logging_started:
            # set up minimal logging
            _logfilename = 'debuginfo.txt'
            _debugConfig = _workdir / _logfilename
            logging.basicConfig(filename='debuginfo.txt', level=logging.INFO,
                                filemode='w')
            print(f'Minimal logging established to {_debugConfig}')

        # start logging
        global log
        log = logging.getLogger(__name__)
        logging.info(f'Logging started: working directory is {_workdir}')
        return


if __name__ == "__main__":
    workdir = Path.cwd()
    debug_file_name = 'debuginfo.yaml'
    main = Main()
    main.start_logging(workdir, debug_file_name)
    main.run_ChrLbls()

# EOF

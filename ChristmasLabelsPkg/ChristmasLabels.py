"""
ChristmasLabels.py - Manage christmas labels program.
"""

import logging
import logging.config
import yaml  # from PyYAML library
from logging import getLogger, debug, error
from pathlib import Path
from typing import Any, Union, Optional

import wx
import gettext

from ChristmasLabelsPkg.ORMTables import Contact, State, create_db
from ChristmasLabelsPkg.ChristmasLabelsGUI import ChristmasLabelsApp, \
    MainMenuFrameClass

__author__ = 'Travis Risner'
__project__ = "Christmas-Labels"
__creation_date__ = "03/07/2019"
# Copyright 2019 by Travis Risner - MIT License

log = None


class FullMainMenuFrameClass(MainMenuFrameClass):
    """
    Implement details of GUI methods.
    """

    # def __init__(self, *args, **kwargs):
    #     MainMenuFrameClass.__init__(self, *args, **kwargs)
    #
    #     return

    def on_button_quit_clicked(self, event):
        """
        Implement the main quit button to shut down the application.

        :param event:
        :return:
        """
        self.Close()
        return

class ChristmasLabelsClass(ChristmasLabelsApp):
    """
    ChristmasLabelsClass - Manage christmas labels user interface.
    """

    def __init__(self, *args, **kwargs):
        ChristmasLabelsApp.__init__(self, *args, **kwargs)

    def OnInit(self, working_dir: Path = None):

        # set up my version of the main menu frame
        self.main_menu_frame = FullMainMenuFrameClass(None, wx.ID_ANY, "")
        self.SetTopWindow(self.main_menu_frame)
        self.main_menu_frame.Show()
        return True


class Main:
    """
    Main class to start things rolling.
    """

    def __init__(self):
        """
        Get things started.
        """
        self.ChrLbls = None
        self.working_dir = None
        return

    def run_ChrLbls(self):
        """
        Prepare to run Run the Christmas labels user interface..

        :return:
        """
        debug('Starting up ChrLbls')
        gettext.install('Why Me')

        # create db if needed
        db_created = create_db(self.working_dir)
        debug(f'Database created? {db_created}')

        self.ChrLbls = ChristmasLabelsClass(0)
        self.ChrLbls.MainLoop()
        return

    def start_logging(self, work_dir: Path, debug_name: str):
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
                    _logdict = yaml.load(_logdictfd, Loader=yaml.FullLoader)
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
        self.working_dir = _workdir
        return


if __name__ == "__main__":
    workdir = Path.cwd()
    debug_file_name = 'debuginfo.yaml'
    main = Main()
    main.start_logging(workdir, debug_file_name)
    main.run_ChrLbls()

# EOF

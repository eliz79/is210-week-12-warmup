#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Custom Logger Class"""


import time


class CustomLogger(object):
    """Docstring.

    """

    def __init__(self, logfilename):
        """A class instance.
        Attributes:
            None
        Args:
            logfilename(str): a file name for loggers.
            msgs(list): a list of messages.
        """
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Docstring.
        Args:
            msg(str): a message.
            timestamp(Unix Time Stamp): timestamp default to None.
        Returns:
            Logged messages and timestamps.
        Examples:
            >>> logger.log('hello')
            >>> logger.log('goodbye')
            logger.msgs
            [(1429838843.838129, 'hello'), (1429838858.844048, 'goodbye')]
        """
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """A simple login.
        Args:
            None
        Returns:
            None
        Examples:
            >>> open('somelongfilename')
        """
        handled = []
        try:
            fhandler = open(self.logfilename, 'a')
        except:
            raise IOError
        try:
            for index, entry in enumerate(self.msgs):
                fhandler.write(str(entry) + '\n')
                handled.append(index)
        except:
            raise IOError
        try:
            for index in handled[::-1]:
                del self.msgs[index]
        except IOError:
            self.log(IOError)
            raise IOError
        finally:
            fhandler.close()

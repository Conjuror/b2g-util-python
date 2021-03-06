# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import re
import logging
import subprocess
from distutils import spawn
from adb_helper import AdbWrapper


logger = logging.getLogger(__name__)


class B2GHelper(object):

    @classmethod
    def stop_b2g(cls, serial=None):
        logger.info('Stop B2G.')
        output, retcode = AdbWrapper.adb_shell('stop b2g', serial=serial)

    @classmethod
    def start_b2g(cls, serial=None):
        logger.info('Start B2G.')
        output, retcode = AdbWrapper.adb_shell('start b2g', serial=serial)

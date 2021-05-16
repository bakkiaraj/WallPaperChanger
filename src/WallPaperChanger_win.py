#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author        : Bakkiaraj Murugesan
# @EMail         :
# @Software      : WallPaperChanger
# SPDX short identifier: MIT
# License
# Copyright 2021 Bakkiaraj Murugesan
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from OSHelper import CURRENT_OS
from Utils.AppData import APP_VERSION
from Utils.LoggerUtils import configure_logger
import logging
from pathlib import Path

# Globals
logger = logging.getLogger(__name__)
__version__ = APP_VERSION
if __name__ == "__main__":
    configure_logger()

    logger.info(f"Starting {Path(__file__).stem} version {__version__}")
    logger.info(f"{CURRENT_OS}")



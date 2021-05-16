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
import logging
import sys
from dataclasses import dataclass
from pathlib import Path

import click

from ArtGallery.WallPaperArtistFactory import WallPaperArtistsTypes
from Utils.AppData import APP_VERSION, EXIT_INPUT_IS_INVALID

logger = logging.getLogger(__name__)

@dataclass
class app_startup_cli_options:
    wallpaper_save_dir: str
    enable_debug: bool
    wallpaper_service_provider: WallPaperArtistsTypes

@click.command()
@click.version_option(version=APP_VERSION)
@click.option('--savedir', default=False, help='Folder where wallpaper files to be saved.', show_default=True, type=str)
@click.option('--debug/--no-debug', is_flag=True, default=False, help='Enable DEBUG logging.', show_default=True, type=bool)
@click.option('--provider', default="bing", help='Wallpaper Providers. Possible values are "bing"', show_default=True, type=str)
def process_applications_args(savedir: str, debug: bool, provider: str) -> None:
    """
    Process command line options
    :param savedir:
    :param debug:
    :param provider:
    :return:
    """
    click.clear()
    logger.info("Processing user entered command line options")
    # Check savedir if not exists create one
    try:
        Path(savedir).mkdir(parents=True,exist_ok=True)
    except Exception as ex:
        logger.error(f"Can not create / access {savedir}. Exiting.")
        sys.exit(EXIT_INPUT_IS_INVALID)
    # Check provider
    provider = WallPaperArtistsTypes(provider)
    app_startup_cli_options(wallpaper_save_dir=savedir,enable_debug=debug,)
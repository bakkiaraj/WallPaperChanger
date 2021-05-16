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

import os
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field

@dataclass
class CanvasData:
    """
    A data class to have details of desktop details
    """
    width: int = field(default=1920)
    height: int = field(default=1080)
    wallpaper_directory: str = field(default=os.path.abspath('.'))

class WallPaperArtist(metaclass=ABCMeta):
    """
    Abstract class for wallpaper painter / downloader implementations
    """

    def get_wallpaper(self,canvas_details:CanvasData) -> str:
        raise NotImplementedError("This is an Interface.")




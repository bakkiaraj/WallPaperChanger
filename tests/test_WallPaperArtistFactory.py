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

from ArtGallery.WallPaperArtistFactory import WallPaperArtistsTypes
from assertpy import assert_that
from grappa import should

logger = logging.getLogger(__name__)

def test_wall_paper_artists_types():
    bing_type = WallPaperArtistsTypes(1)
    assert_that(bing_type).is_type_of(type(WallPaperArtistsTypes.BING))

    bing_type1 = WallPaperArtistsTypes["bing".upper()]
    assert_that(bing_type1).is_type_of(type(WallPaperArtistsTypes.BING))

    bing_type2 = WallPaperArtistsTypes["bing".upper()]
    bing_type2 | should.be.a(type(WallPaperArtistsTypes.BING))
    assert_that(bing_type1).is_type_of(type(WallPaperArtistsTypes.BING))

    def check_non_exist_member_in_WallPaperArtistsTypes(member):
        WallPaperArtistsTypes[member]

    assert_that(check_non_exist_member_in_WallPaperArtistsTypes).described_as("Check for KeyError exception").raises(KeyError).when_called_with("FOO")







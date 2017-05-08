# -*- coding: utf-8 -*-
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.docsquiffy'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon()
icon = local.getAddonInfo('icon')


YOUTUBE_PLAYLIST_ID = "UCFOStcorp34JSwYTaTZB1oQ"

# Entry point
def run():
    plugintools.log("docsquiffy.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        pass
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docsquiffy.main_list "+repr(params))

    plugintools.add_item( 
        title="Liked Videos",
        url="plugin://plugin.video.youtube/playlist/LLFOStcorp34JSwYTaTZB1oQ/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        title="Stand Alone APKs",
        url="plugin://plugin.video.youtube/playlist/PLTLj1aYVquJnP9bhGUW7ADT2jyYR3yyb4/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        title="Builds",
        url="plugin://plugin.video.youtube/playlist/PLTLj1aYVquJmk1tEd7lKXtcj7AdOnSp-k/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        title="How To Run Maintenance Kodi",
        url="plugin://plugin.video.youtube/playlist/PLTLj1aYVquJmtLDryUYk0Okzx-hP5j3pI/",
        thumbnail=icon,
        folder=True )


run()
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

addonID = 'plugin.video.ghostware'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon()
icon = local.getAddonInfo('icon')


YOUTUBE_PLAYLIST_ID = "UC0j1U3QzGciIodKLuFHr8jA"

# Entry point
def run():
    plugintools.log("ghostware.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        pass
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("ghostware.main_list "+repr(params))

    plugintools.add_item( 
        title="Ghostware Support",
        url="plugin://plugin.video.youtube/playlist/UC0j1U3QzGciIodKLuFHr8jA/",
        thumbnail=icon,
        folder=True )

    


run()
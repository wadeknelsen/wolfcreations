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

addonID = 'plugin.video.vldl'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon()
icon = local.getAddonInfo('icon')


YOUTUBE_PLAYLIST_ID = "UCchBatdUMZoMfJ3rIzgV84g"

# Entry point
def run():
    plugintools.log("vldl.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        pass
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("vldl.main_list "+repr(params))

    plugintools.add_item( 
        title="Bored",
        url="plugin://plugin.video.youtube/playlist/PLSMETuURtTXDkOm6Xx4Q-1HS8W54GrBDm/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        title="Epic NPC Man",
        url="plugin://plugin.video.youtube/playlist/PLSMETuURtTXCzW7Q_ZIy4QzEnyUG8totf/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        title="Wildcard",
        url="plugin://plugin.video.youtube/playlist/PPLSMETuURtTXAG7OHhomYAUsZphDDN6szE/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        title="Hearthstone Skits",
        url="plugin://plugin.video.youtube/playlist/PLSMETuURtTXDq42FuxaYo4Oem7AmZunrJ/",
        thumbnail=icon,
        folder=True )
		
    plugintools.add_item( 
        title="Music Videos",
        url="plugin://plugin.video.youtube/playlist/PLSMETuURtTXB-tCki9QpNg-pGJEB4qBRl/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        title="Lets Play",
        url="plugin://plugin.video.youtube/playlist/PLSMETuURtTXCSyeoH2a5_KIZdXN1mzmUK/",
        thumbnail=icon,
        folder=True )
run()
# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GenieLamp
                                 A QGIS plugin
 prototype
                             -------------------
        begin                : 2015-04-04
        copyright            : (C) 2015 by hui han CHIN
        email                : chuihan@dso.org.sg
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GenieLamp class from file GenieLamp.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .genie_lamp import GenieLamp
    return GenieLamp(iface)

# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MultiPointsRoute
                                 A QGIS plugin
 Compute route with multiple middle points using Webservices
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-10-05
        copyright            : (C) 2020 by Guilhem Allaman
        email                : dev@guilhemallaman.net
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
    """Load MultiPointsRoute class from file MultiPointsRoute.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .multi_points_route import MultiPointsRoute
    return MultiPointsRoute(iface)

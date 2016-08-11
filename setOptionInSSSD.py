#!/usr/bin/python
# Author: Shridhar Gadekar
# Date: 11th August 2016
# Purpose: This script will modify and set an option 'user' from  [sssd] section of sssd.conf and set it to the non root user such as a sysetm user called 'sssd'.  
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from SSSDConfig import SSSDConfig

sssdconfig = SSSDConfig()
sssdconfig.import_config('/etc/sssd/sssd.conf')

sssd_option = sssd.config.get_service('sssd')
sssd_option.set_option('user', 'sssd')
sssd_option.save_service('sssd_options')

sssdconfig.write()

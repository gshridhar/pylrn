#!/usr/bin/python
# This piece of code is from SSSD documentions, i've modified it for testing purpose

from SSSDConfig import SSSDConfig

sssdconfig = SSSDConfig()
sssdconfig.import_config('/etc/sssd/sssd.conf')

ldap_domain = sssdconfig.get_domain('ipa.test')
ldap_domain.set_option('enumerate', False)
sssdconfig.save_domain(ldap_domain)

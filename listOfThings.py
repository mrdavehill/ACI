#python 3

"""

The APIC naming conventions in my company were designed to be globally uniformed and this script will need to be updated to match your standards

Tenant - tnt_{environment}_baremetal_prod

epg - epg_{vlan}_core_(subnet}

BD - bd_core_{subnet}

The Vlan and subnet variables are input() in the script

"""

import pyfiglet

banner = pyfiglet.figlet_format("Lab L2 Vlan Builder")

#Add the FQDN of the APIC as the host string below
host = ''

#country code or 'lab'
environment = ''

#vrf name
vrf = ''

#these are the interfaces you would normally statically pin to the BD
#update them so they match your vPCs etc
#ipdate the domain in 'fvRsDomAtt'
  
borderLeafInterfaces = [{'fvRsPathAtt': {'attributes': {'encap': '', 'tDn': 'topology/pod-1/paths-202/pathep-[eth1/35]'}}},
{'fvRsPathAtt': {'attributes': {'encap': '', 'tDn': 'topology/pod-1/paths-202/pathep-[eth1/33]'}}},
{'fvRsPathAtt': {'attributes': {'encap': '', 'tDn': 'topology/pod-1/paths-201/pathep-[eth1/33]'}}},
{'fvRsPathAtt': {'attributes': {'encap': '', 'tDn': 'topology/pod-1/paths-201/pathep-[eth1/35]'}}},
{'fvRsPathAtt': {'attributes': {'encap': '', 'tDn': 'topology/pod-1/protpaths-201-202/pathep-[policy_vpc_201_202_23_24]'}}},
{'fvRsDomAtt': {'attributes': {	'tDn': 'uni/phys-domain_core'}}},
{'fvRsBd': {'attributes': {'tnFvBDName': ''}}}
]

    

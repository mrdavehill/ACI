#python 3

"""
The Vlan and subnet variables are input() in the script
"""

import pyfiglet

banner = pyfiglet.figlet_format("ACI Automation")

#Add the FQDN of the APIC as the host string below
host = 'sandboxapicdc.cisco.com'

#Vlan pool
vlanPool = 'Vlan_Pool_Core'

#AEP
aep = 'AEP_Core'

#Physical domain
domain = 'Domain_Core'

#Tenant - using common to test
environment = 'common'

#VRF - using default to test
vrf = 'default'

#these are the interfaces you would normally statically pin to the BD from your border leaves
#update them so they match your vPCs etc
#update the domain in 'fvRsDomAtt'. 
  
borderLeafInterfaces = [{'fvRsPathAtt': {'attributes': {'encap': '', 'tDn': 'topology/pod-1/paths-202/pathep-[eth1/35]'}}},
{'fvRsPathAtt': {'attributes': {'encap': '', 'tDn': 'topology/pod-1/paths-202/pathep-[eth1/33]'}}},
{'fvRsPathAtt': {'attributes': {'encap': '', 'tDn': 'topology/pod-1/paths-201/pathep-[eth1/33]'}}},
{'fvRsPathAtt': {'attributes': {'encap': '', 'tDn': 'topology/pod-1/paths-201/pathep-[eth1/35]'}}},
{'fvRsPathAtt': {'attributes': {'encap': '', 'tDn': 'topology/pod-1/protpaths-201-202/pathep-[policy_vpc_201_202_23_24]'}}},
{'fvRsDomAtt': {'attributes': {	'tDn': f'uni/phys-domain_{domain}'}}},
{'fvRsBd': {'attributes': {'tnFvBDName': ''}}}
]

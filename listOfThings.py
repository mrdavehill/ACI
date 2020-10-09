


#python 3
#
#

"""

It's the listOfThings for the Lab APIC

Created 25/04/2019

Updated 14/07/2020

"""



import pyfiglet

banner = pyfiglet.figlet_format("Lab L2 Vlan Builder")

#Add the FQDN of the APIC as the host string below

host = ''

environment = 'lab'

vrf = 'ctx-vrf_uslab_core'
  
borderLeafInterfaces = [{'fvRsPathAtt': {'attributes': {'encap': '', 'tDn': 'topology/pod-1/paths-202/pathep-[eth1/35]'}}},
{'fvRsPathAtt': {'attributes': {'encap': '', 'tDn': 'topology/pod-1/paths-202/pathep-[eth1/33]'}}},
{'fvRsPathAtt': {'attributes': {'encap': '', 'tDn': 'topology/pod-1/paths-201/pathep-[eth1/33]'}}},
{'fvRsPathAtt': {'attributes': {'encap': '', 'tDn': 'topology/pod-1/paths-201/pathep-[eth1/35]'}}},
{'fvRsPathAtt': {'attributes': {'encap': '', 'tDn': 'topology/pod-1/protpaths-201-202/pathep-[policy_vpc_201_202_23_24]'}}},
{'fvRsDomAtt': {'attributes': {	'tDn': 'uni/phys-domain_core'}}},
{'fvRsBd': {'attributes': {'tnFvBDName': ''}}}
]

    

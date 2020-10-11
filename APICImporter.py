#python 3

"""
This script automates importing Vlans over a brdige from legacy into ACI

It...

1. logs onto the APIC and generates a cookie
2. saves a snapshot referencing the change number
3. creates a vlan pool using entered data
4. creates bridge domains but does not include the subnets using entered data
5. creates epgs and adds them to the edge interfaces and vpcs using entered data

Requires separate credentials.py file for authentication

Requires separate listOfThings.py file with APIC specific variables

Created 04/04/2019

Latest version 11/10/2019
"""

import requests
requests.packages.urllib3.disable_warnings()

import pprint
import json

import credentials

from listOfThings import host
from listOfThings import environment
from listOfThings import vrf
from listOfThings import borderLeafInterfaces
from listOfThings import banner
#import confirm

def confirm(prompt=None, resp=False):
    if prompt is None:
        prompt = '\nProceed?'
    if resp:
        prompt = '%s [%s]|%s: ' % (prompt, 'y', 'n')
    else:
        prompt = '%s [%s]|%s: ' % (prompt, 'n', 'y')
    while True:
        ans = input(prompt)
        if not ans:
            return resp
        if ans not in ['y', 'Y', 'n', 'N']:
            print('please enter y or n.')
            continue
        if ans == 'y' or ans == 'Y':
            return True
        if ans == 'n' or ans == 'N':
            quit()

def get_cookies(apic):
    url = apic + '/api/aaaLogin.json'
    auth = {'aaaUser': {'attributes': {'name': credentials.username, 'pwd': credentials.password}}}
    authenticate = requests.post(url, data=json.dumps(auth), verify=False)
    return authenticate.cookies

def create_snapshot(apic, cookies):
    url = '{0}/api/node/mo/uni/fabric/configexp-defaultOneTime.json'.format(apic)
    snapshotRef = input('\nTen Digit Change Number and user ID:' )
    payload = {
	'configExportP': {
		'attributes': {
			'dn': 'uni/fabric/configexp-defaultOneTime',
			'adminSt': 'triggered',
			'descr': ''
		}
	}
}  
    payload['configExportP']['attributes']['descr'] = snapshotRef
    print('\nHit Y to create a snapshot with ref {0} \n'.format(snapshotRef))
    descr = 'Snapshot {0}'.format(snapshotRef)    
    print(url)
    print('\n')
    pprint.pprint(payload)
    confirm()
    result = requests.post(url, data=json.dumps(payload), verify=False, cookies=cookies)
    text = json.loads(result.text)
    code = result.status_code
    if code == 200:
        print('\nReturn 200, {0} added.'.format(descr))
    else:
        print('\nReturn {0}, {1} failed.'.format(code, descr))
        pprint.pprint(text)
        quit()
        
def create_vlans(apic, cookies):
    url = '{0}/api/node/mo/uni/infra/vlanns-[Vlan_Pool_Core]-static/from-[vlan-{1}]-to-[vlan-{2}].json'.format(apic, firstVlan, lastVlan)
    payload = {
	'fvnsEncapBlk': {
		'attributes': {
			'allocMode': 'static',
			'dn': '',
			'from': '',
			'to': ''
		}
	}
}
    payload ['fvnsEncapBlk']['attributes']['dn'] = 'uni/infra/vlanns-[Vlan_Pool_Core]-static/from-[vlan-{1}]-to-[vlan-{2}]'.format(apic, firstVlan, lastVlan)
    payload ['fvnsEncapBlk']['attributes']['from'] = 'vlan-{0}'.format(firstVlan)
    payload ['fvnsEncapBlk']['attributes']['to'] = 'vlan-{0}'.format(lastVlan)
    print('\nCheck the Vlan Pool URL and JSON for Vlans {0} to {1}: \n'.format(firstVlan, lastVlan))
    descr = 'Vlans {0} to {1}'.format(firstVlan, lastVlan)
    print(url)
    print('\n')
    pprint.pprint(payload)
    confirm()
    result = requests.post(url, data=json.dumps(payload), verify=False, cookies=cookies)
    text = json.loads(result.text)
    code = result.status_code
    if code == 200:
        print('\nReturn 200, {0} added.'.format(descr))
    else:
        print('\nReturn {0}, {1} failed.'.format(code, descr))
        pprint.pprint(text)
        quit()

def create_bds(apic):
    payload = {
	"fvBD": {
		"attributes": {
			"arpFlood": "yes",
			"dn": "",
			"mac": "00:22:BD:F8:19:FF",
			"mcastAllow": "no",
			"name": "",
			"unicastRoute": "no"
		},
		"children": [{
			"fvRsCtx": {
				"attributes": {
					"tnFvCtxName": ""
				}
			}
		}]
	}
}   
    bdList = len(subnetList)   
    for i in range(bdList):
        url = '{0}/api/node/mo/uni/tn-{1}/BD-bd_core_{2}.json'.format(apic, environment, subnetList[i]) 
        payload['fvBD']['attributes']['dn'] = 'uni/tn-{0}/BD-bd_core_{1}'.format(environment, subnetList[i])
        payload['fvBD']['attributes']['name'] = 'bd_core_{0}'.format(subnetList[i])
        payload['fvBD']['children'][0]['fvRsCtx']['attributes']['tnFvCtxName'] = vrf
        print('\nCheck the Bridge Domain URL and JSON for {0}: \n'.format(subnetList[i]))
        descr = 'Bridge Domain {0}'.format(subnetList[i])
        print(url)
        print('\n')
        pprint.pprint(payload)
        confirm()
        result = requests.post(url, data=json.dumps(payload), verify=False, cookies=cookies)
        text = json.loads(result.text)
        code = result.status_code
        if code == 200:
            print('\nReturn 200, {0} added.'.format(descr))
        else:
            print('\nReturn {0}, {1} failed.'.format(code, descr))
            pprint.pprint(text)
            quit()

def create_epgs(apic):
    encapList = len(borderLeafInterfaces) - 2
    for i in range(vlanLen):
        for vlan in range(encapList):
            borderLeafInterfaces[vlan]['fvRsPathAtt']['attributes']['encap'] = 'vlan-{0}'.format(vlanList[i])
        borderLeafInterfaces[-1]['fvRsBd']['attributes']['tnFvBDName'] = 'bd_core_{0}'.format(subnetList[i])
        epgnames = 'epg_{0}_core_{1}'.format(vlanList[i], subnetList[i])
        epgdns = 'uni/tn-{0}/ap-default/epg-{1}'.format(environment, epgnames)
        url = '{0}/api/node/mo/{1}.json'.format(apic, epgdns)
        payload = {
	'fvAEPg': {
		'attributes': {
			'dn': '',
			'name': ''
		},
		'children': []
	}
}                                                                                                                                                                                         
        payload['fvAEPg']['attributes']['dn'] = epgdns
        payload['fvAEPg']['attributes']['name'] = epgnames
        payload['fvAEPg']['children'] = borderLeafInterfaces
        print('\nCheck the EPG URL and JSON for Vlan {0}: \n'.format(vlanList[i]))
        descr = 'EPG {0}'.format(vlanList[i])
        print(url)
        print('\n')
        pprint.pprint(payload)
        confirm()
        result = requests.post(url, data=json.dumps(payload), verify=False, cookies=cookies)
        text = json.loads(result.text)
        code = result.status_code
        if code == 200:
            print('\nReturn 200, {0} added.'.format(descr))
        else:
            print('\nReturn {0}, {1} failed.'.format(code, descr))
            pprint.pprint(text)
            quit()
            
if __name__ == '__main__':

    print(banner)
    
    print('This script will genetrate URLs and JSON for a Vlan Pool, Bridge Domains and EPGs to bridge Legacy Vlans into ACI and push them into the APIC REST API.\n\nIt does not build any L3 connectivity.')
    
    vlanInput = input('\nEnter a contiguous list of Vlans in nnn format, comma separated with no spaces (so it looks like 311,312,313), then hit return: ')
    vlanList = list(map(str, vlanInput.split(',')))
    print('\nVerify these are your Vlans and check for white spaces: {0}'.format(vlanList))
    confirm()

    vlanLen = len(vlanList)
    firstVlan = vlanList[0]
    lastVlan = vlanList[-1]
  
    subnetInput = input('\nEnter the subnets in n.n.n.n_n format(so it looks like 10.116.22.0_23,10.116.24.0_23), comma separated, then hit return: ')
    subnetList = list(map(str, subnetInput.split(',')))
    print('\nVerify these are your subnets and check for white spaces: {0}'.format(subnetList))
    confirm()

    vlanSubnet = dict(zip(vlanList, subnetList))
    print('\nHow does this look, do the Vlans and subnets match?\n')
    pprint.pprint(vlanSubnet, width=1)
    print('\nNothing has been sent to the APIC so far, confirm you want to start')
    confirm()

    protocol = 'https'
    apic = '{0}://{1}'.format(protocol, host)
    cookies = get_cookies(apic)
    create_snapshot(apic, cookies)
    
    create_vlans(apic, cookies)
    create_bds(apic)
    create_epgs(apic)

    print('\nScript complete, IVP using APIC GUI\n')

This script automates importing Vlans over a bridge from legacy into ACI

It...

1. logs onto the APIC and generates a cookie
2. saves a snapshot referencing the change number
3. creates a vlan pool using entered data
4. creates bridge domains but does not include the subnets using entered data
5. creates epgs and adds them to the edge interfaces and vpcs using entered data

You need to...

Clone this repo

Update credentials.py file with username and password

Update listOfThings.py with device names and switchports

Run APICImporter.py


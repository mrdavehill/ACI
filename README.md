# ACI---Add-BD-EPG-and-Vlan-Pool

Not working atm - I'm fixing it up so it works on a Cisco Devnet Sandbox.

Cisco ACI automation

Creates EPGs, BDs, Vlan pools and POSTs them onto the APICs REST API as JSON. 

![Here be screengrab]()
 
## Use Case Description

I needed to create multiple Bridge Domains and End Point Groups in ACI for temporary bridges into legacy NXOS as we moved our VM estate.

The configs for each BD/EPG were pretty much the same so I created a script to save some clicking.

## Installation

Clone to your machine, update credentials.py and listOfThings.py so it matches your environment.

## Configuration

Get into that credentials.py file and add your details to the host, username and password objects.

It's currently set up to use a Cisco Devnet sandbox but you can change that to suit your environment.

host = 'https://sandboxapicdc.cisco.com'
username = 'admin'
password = 'ciscopsdt'

Then start on the listOfThings.py

## Usage

There's an example of this script in one of my projects that [creates EPGs, BDs and Vlan pools.](https://github.com/mrdavehill/ACI---Add-BD-EPG-and-Vlan-Pool/blob/main/APICImporter.py)

### DevNet Sandbox

Cisco has an 'always on' APIC [here](https://sandboxapicdc.cisco.com/) you can test this sript on. 

It really does work; amaze!

## How to test the software

See Sandbox ^.

## Known issues

The credentials file doesn't fit best practices for hiding your username and password. I am truly sorry for this.

## Getting help

Hit me up if you have any issues.

## Author(s)

This project was written and is maintained by the following individuals:

* Dave Hill <dave@davehill.org>


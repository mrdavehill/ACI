# ACI---Add-BD-EPG-and-Vlan-Pool

Cisco ACI automation

Creates EPGs, BDs, Vlan pools and POSTs them onto the APICs REST API as JSON. 

![Here be screengrab](https://github.com/mrdavehill/ACI---Add-BD-EPG-and-Vlan-Pool/blob/main/ACI-APIC-Automation.png)
 
## Use Case Description

I needed to create multiple Bridge Domains and End Point Groups in ACI for temporary bridges into legacy NXOS as we moved our VM estate.

There's no gateway config - we left out gateways in legacy during the migration.

The configs for each BD/EPG were pretty much the same so I created a script to save some clicking.

The screengrab below is the completed config on a Devnet APIC run from this script. I know, right?

![Here be mo screengrab](https://github.com/mrdavehill/ACI---Add-BD-EPG-and-Vlan-Pool/blob/main/APIC-Sreenshot.png)

## Installation

Clone to your machine, update credentials.py and listOfThings.py so it matches your environment.

## Configuration

Get into that credentials.py file and add your details to the host, username and password objects.

It's currently set up to use a Cisco Devnet sandbox but you can change that to suit your environment.

host = 'https://sandboxapicdc.cisco.com'

username = 'admin'

password = 'ciscopsdt'

Then start on the listOfThings.py

This is also set up for the sandbox

host = 'sandboxapicdc.cisco.com'

domain = 'Domain_Core'

environment = 'common'

## Usage

VM migrations over a layer 2 bridge.

### DevNet Sandbox

Cisco has an 'always on' APIC [here](https://sandboxapicdc.cisco.com/) you can test this sript on. 

It really does work; amaze!

## How to test the software

You may need to create the objects below on the sandbox, check and see if they're still there.

AEP - AEP_Core

Vlan Pool - Vlan_Pool_Cpre

Domain - Domain_Core

I've used the common tenant. You wouldn't do that in Prod but as the config on this APIC is a moving target I'll take whatever stability I can get.

## Known issues

The credentials file doesn't fit best practices for hiding your username and password. I am truly sorry for this.

I could have used 'tenant' instead of 'environment' to clearer.

## Getting help

Hit me up if you have any issues.

## Author(s)

This project was written and is maintained by the following individuals:

* Dave Hill <dave@davehill.org>

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/mrdavehill/ACI---Add-BD-EPG-and-Vlan-Pool)



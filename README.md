# ACI--Create-Config-Rollback

Cisco ACI automation

Creates EPGs, BDs, Vlan pools and adds them to

![Here be screengrab]()
 
## Use Case Description

Dev.

Test code and easily back any changes out. Update, rinse, repeat.

Prod.

Create a rollback as a first step in any script and reference the change record number. CAB will love you.

## Installation

Clone to your machine, update credentials.py, run APICSnapshot.py.

## Configuration

Get into that credentials.py file and add your details to the host, username and password objects.

It's currently set up to use a Cisco Devnet sandbox but you can change that to suit your environment.

host = 'https://sandboxapicdc.cisco.com'
username = 'admin'
password = 'ciscopsdt'

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


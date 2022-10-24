## Python subdomain scanner using the Sublist3r tool

import os
import sys
import subprocess
import argparse

# Input domain name

parser = argparse.ArgumentParser(description='Subdomain scanner')
parser.add_argument('-d', '--domain', help='Domain name', required=True)
args = parser.parse_args()

# Run Sublist3r

subprocess.call(['python', 'sublist3r.py', '-d', args.domain, '-o', 'subdomains.txt'])

# Read subdomains.txt and print to screen

with open('subdomains.txt', 'r') as f:
    for line in f:
        print (line.strip())



# Nmap project to detect open ports on a network

import nmap # import nmap.py module
import sys

# Create a scanner object

scanner = nmap.PortScanner()

# Ask user for input

print("Welcome, this is a simple nmap automation tool")
print("<-------------------------------------------------->")

ip_add = input("Enter the IP address you want to scan: ")

print("The IP you entered is: ", ip_add)

type(ip_add)

# function to get open ports from ip_add

def nmap_scan(ip_add):
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_add, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_add].state())
    print(scanner[ip_add].all_protocols())
    print("Open ports: ", scanner[ip_add]['tcp'].keys())

nmap_scan(ip_add)

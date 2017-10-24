#!/usr/bin/env python3

import argparse
import os


def main():
	parser = argparse.ArgumentParser(prog='hostslist.py', description='create hosts list with top 500 domains for use in dns spoofing')
	parser.add_argument('ip', action='store', type=str, help='ip to insert in hosts file')
	parser.add_argument('filename', action='store', type=str, help='file to save hosts list to')
	args = parser.parse_args()

	ip = args.ip
	filename = args.filename
// adjusted file name	
	domains = []
	with open('top500.txt', 'r') as f:
		domains = [l.strip() for l in f]
	
	hostslist = []
	for i in domains:
		hostslist.append(ip+'\t'+i+'\n')
	
	with open(filename, mode='wt', encoding='utf-8') as myFile:
		myFile.write(''.join(hostslist))

if __name__ == '__main__':
	main()

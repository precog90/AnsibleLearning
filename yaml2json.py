import sys
import yaml
from pprint import pprint

file_name = raw_input("Enter YAML File Name: ")

with open(file_name) as f:
	out = yaml.load(f)
	pprint(out)
	#for key,value in out.items():
	#	print("{} --> {}".format(key,value))

import os
import sys

#base_dir="./data1"
base_dir=sys.argv[1]

for path,pathname,filenames in os.walk(base_dir):
	if "out1" in path:
		os.popen("cp -rf %s/* ./out4"%path)
		print("cp -rf %s/* ./out4"%path)

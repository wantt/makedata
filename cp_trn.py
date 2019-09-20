import os
import sys

base_dir=sys.argv[1]

trn_dir="./data/"

for path,pathname,filenames in os.walk(base_dir):
	for filename in filenames:
		os.popen("cp -rf '%s' '%s'"%(os.path.join(trn_dir,filename.replace(".wav",".wav.trn")),os.path.join(base_dir,filename.replace(".wav",".wav.trn"))))

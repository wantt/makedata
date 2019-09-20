import os
import sys

base_dir=sys.argv[1]

for path,pathname,filenames in os.walk(base_dir):
	for filename in filenames:
		if filename.endswith('.pcm'):
			os.popen("./pcm2wav '%s' '%s'"%(os.path.join(path,filename),os.path.join(path,filename.replace(".pcm",".wav"))))

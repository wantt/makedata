import os
import sys

base_dir=sys.argv[1]
for path,pathname,filenames in os.walk(base_dir):
	for filename in filenames:
		if filename.endswith(".pcm"):
			if "wakeup_out_Chao25_eq" in filename:
				os.popen("rm '%s'"%os.path.join(path,filename))
			else:
				os.popen("mv '%s' '%s'"%(os.path.join(path,filename),os.path.join(path,filename.split("_asr_out2.pcm")[0]+".pcm")))

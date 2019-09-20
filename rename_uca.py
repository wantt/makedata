import os
import sys

base_dir=sys.argv[1]
for path,pathname,filenames in os.walk(base_dir):
	for filename in filenames:
		if filename.endswith(".wav"):
#			os.popen("mv '%s' '%s'"%(os.path.join(path,filename),os.path.join(path,filename.split("_wakeup_out_Chao25_eq.pcm")[0]+".pcm")))
			os.popen("mv '%s' '%s'"%(os.path.join(path,filename),os.path.join(path,filename.split("_wakeup_out_Chao25_eq.wav")[0]+".wav")))
#			print("mv '%s' '%s'"%(os.path.join(path,filename),os.path.join(path,filename.split("_wakeup_out_Chao25_eq.pcm")[0]+".pcm")))

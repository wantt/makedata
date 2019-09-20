import os
import scipy.io.wavfile
import numpy as np


def to8(in_path,in_filename,out_path):
	# convert mono to 8 channel pcm
	Fs, y_input = scipy.io.wavfile.read(os.path.join(in_path,in_filename))
	zero1 = np.zeros((len(y_input)),dtype=np.int16)
	d1 = np.c_[y_input,y_input,y_input,y_input,zero1,zero1,y_input,y_input]
	d1.dtype="int16"

	scipy.io.wavfile.write(os.path.join(out_path,in_filename),16000,d1)

if __name__=="__main__":

#	to8('./','test.wav','./out')
	base_dir = "./data_thchs30" 
	out_dir = "./data_thchs30_sp"
	for path,pathname,filenames in os.walk(base_dir):
		for filename in filenames:
			if filename.endswith(".wav"):
				to8(path,filename,os.path.join(out_dir,path.split('/')[-1]))

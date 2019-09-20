import os
import sys

#base_dir = 'data1/'
base_dir = sys.argv[1]
#./cqlib_process_test  data/  org_input_online out/
for path,pathname,filenames in os.walk(base_dir):
	for filename in filenames:
		if filename.endswith('pcm') and not 'out1' in path:
			if not os.path.exists(os.path.join(path,'out1')):
				os.popen("mkdir %s"%os.path.join(path,'out1'))
			#os.popen("./cqlib_process_test '%s/' '%s'  out1/"%(path,filename.replace('.pcm','')))
			os.popen("./cqlib_process_test '%s/' '%s'  out1/"%(path,filename.replace('.pcm','')))

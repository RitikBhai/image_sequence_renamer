import os
path = input('FOLDER PATH:').replace("\\", "/")
os.chdir(path)
files = os.listdir(path)
print(f'>>{len(files)} files are found,[ {files[0]} - {files[-1]} ]')
print(">>newname_#.ext  [newanme= your new file name, _ = separator, # = sequence number, ext- extention]\n".upper())
new_name = input('New name:').strip(' ').rsplit("_",1)
seq_,ext_ =new_name[1].rsplit(".")

try:
	for x in range(len(files)):
		seq = int(seq_) + x
		os.rename(files[x],"{}_{}.{}".format(new_name[0],str(seq),ext_))
	print("DONE!")
except:
	print("something went wrong!".upper())


import os
path = input('FOLDER PATH:').replace("\\", "/").strip(' ')
os.chdir(path)
files = os.listdir(path)
print(f'>>{len(files)} files are found ||File name preview: {files[0]}||<<')
print(">>for new name fill the followings 4 steps<<\n".upper())
new_name = input('1-New name:').strip(' ')
sep_= input('2-Number separator:').strip(' ')
seq_ = input('3-Sequence number:').strip(' ')
ext_ = input('4-Extention:').strip(' ')
print(f'New file name preview: {new_name}{sep_}{seq_}.{ext_}')
f = input("proceed? [y/n]\n")
try:
	if f == "y" or "Y":
		for x in range(len(files)):
			seq = int(seq_) + x
			
			os.rename(files[x],"{}{}{}.{}".format(new_name,sep_,str(seq).zfill(len(seq_)),ext_))
		print("DONE!\n")
		print("credits RSUNDRIYAK")
	elif f == "n" or "N":
		print("Exited")
	else:
		print("Try agian")	

except:
	print("something went wrong!".upper())


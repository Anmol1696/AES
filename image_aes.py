import aes

def main(a,b,step):
	f = open(a,'r')
	r = f.readlines()
	f.close()
	key = ''
	o = ''
	for x in r:
		o += x
	if(step == 'e'):
		o = aes.Main_Encrypt(o,key)
	else:
		o = aes.Main_Decrypt(o,key)
	w = open(b,'w')
	w.write(o)
	w.close()

if __name__ == '__main__':
	step = raw_input('Enter the e or d ->')
	source_file = raw_input('Enter the location of the source file')
	target_file = raw_input('Enter the location of the target file')
	main(source_file,target_file,step)





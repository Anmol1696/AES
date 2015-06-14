import aes

def main(a,b,d):
	f = open(a,'r')
	r = f.readlines()
	f.close()
	key = 'hello'
	o = ''
	for x in r:
		o += x
	if(d == 'e'):
		o = aes.Main_Encrypt(o,key)
	else:
		o = aes.Main_Decrypt(o,key)
	w = open(b,'w')
	w.write(o)
	w.close()

if __name__ == '__main__':
	d = raw_input('Enter the e or d ->')
	a = raw_input('Enter the location of the source file')
	b = raw_input('Enter the location of the target file')
	main(a,b,d)





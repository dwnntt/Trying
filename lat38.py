teks = """ini adalah isi dari file
yang akan ditulis
menggunakan python"""

#membuka dengan mode tulis
f= open('coba.txt', 'w')
f.write(teks)
f.close()

#default membuka file dengan mode baca
f = open('coba.txt')
while True:
	baris = f.readline()
	if len(baris) ==0:
		#EOF
		break
		print baris,
f.close()
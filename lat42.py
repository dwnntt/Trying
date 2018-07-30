import time

try:
	f=open('coba.txt')
	while True:
		baris = f.readLine()
		if len(baris) == 0:
			#EOF
			break
		print baris,
		time.sleep(2) #delay 2 detik
except KeyboardInterrupt:
	print '\nAnda membatalkan operasi'
finally:
	f.close()
	print '\nfile ditutup'
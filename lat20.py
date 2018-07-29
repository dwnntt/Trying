def total(*bilangan, **keywords):
	hitung = 0
	for bil in bilangan:
		hitung +=bil
	for key in keywords:
		hitung += keywords[key]
	return hitung

print total (1,2,3,4,5)
print total(daging=2, sayur=10, buah= 3)
print total(7,8,5, daging =2, sayur =10, buah=3)
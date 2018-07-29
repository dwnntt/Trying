# lat10.py
# acak looping

nomor_acak = 77
berjalan = True

print 'tebak nomor acak dari 1 - 100'

while berjalan:
    tebakan = int(raw_input('Tebakan anda (bil bulat): '))

    if tebakan == nomor_acak:
        print 'Selamat! tebakan anda benar'
        print 'tapi tidak ada hadiah untuk anda :('
        berjalan = False
    elif tebakan < nomor_acak:
        print 'tebakan anda terlalu kecil'
    else:
        print 'tebakan anda terlalu besar'
else:
    print 'selesai'
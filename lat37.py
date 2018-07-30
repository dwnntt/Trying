def balik_string(teks):
    return teks[::-1]

def apakah_palindrom(teks):
    return teks == balik_string(teks)

inputan = raw_input('Masukkan teks: ')

if apakah_palindrom(inputan):
    print 'Ya, inputan berupa palindrom'
else:
    print 'Tidak, inputan bukan palindrom'
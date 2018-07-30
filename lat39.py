import pickle

daftar_belanja_file= 'daftar.data'
daftar_belanja = ['apel', 'mangga', 'wortel', 'pisang']

#membuka file penyimpanan object dengan mode tulis binary
f= open(daftar_belanja_file.'wb')

#dumb objek ke file
pickle.dump(daftar_belanja, f)
f.close()

#hapus daftar_belanja dari memori
del daftar_belanja
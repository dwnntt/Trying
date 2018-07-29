# lat17.py

x = 50

def fungsi(x):
    print 'x = ', x
    x = 2
    print 'merubah lokal variabel x = ', x

fungsi(100)

print 'nilai x masih %s' % x
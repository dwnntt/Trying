# lat17.py

x = 50

def fungsi():
    print 'x = ', x

def fungsi2():
    x = 100  # menulis ke lokal variabel
    print 'x = ', x

def fungsi3():
    global x
    x = 100
    print 'x = ', x

fungsi()
print 'nilai x = ', x

fungsi2()
print 'nilai x = ', x

fungsi3()
print 'nilai x = ', x
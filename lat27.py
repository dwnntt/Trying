ba = {'ona': 'ona@python.org',
    'ani': 'ani@rhodesmill.org',
    'una': 'una@domain.com'}

print 'alamat email ona:', ba['ona']

# menghapus item
del ba['ani']

print 'ada %s kontak di buku alamat' % len(ba)

for nama, email in ba.items():
    print '%s, email: %s' % (nama, email)

# tambah entri
ba['unina'] = 'uni@jacobian.org'

if 'unina' in ba:
    print 'Email unina di', ba['unina']
try:
	teks = raw_input('ketikkan sesuatu:')
except EOFError:
	print '\nKenapa sudah EOF?'
except KeyBoardInterrupt:
	print '\nAnda membatalkan operasi'
else:
	print 'Anda mengitikkan "%s"' % teks
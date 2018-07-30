class InputPendekErorror(Exception):
	"exception jika input terlalu pendek"

	def __init__(self, panjang, minimal):
		Exception.__init__(self)
		self.panjang = panjang
		self.minimal = minimal


try:
	teks= raw_input('ketikkan sesuatu: ')
	panjang = len(teks)
	minimal_panjang = 3

	if panjang < minimal_panjang:
		raise InputPendekErorror(panjang, minimal_panjang)
except EOFError:
	print '\nkenapa sudah EOF?'
except KeyboardInterrupt:
	print '\nAnda membatalkan operasi'
except InputPendekErorror as e:
	print 'input terlalu pendek: panjang input: %s ' % (e.panjang, e.minimal)
else:
	print 'Anda mengetikkan "%s"' %teks
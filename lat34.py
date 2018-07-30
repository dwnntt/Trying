class Orang:
    def __init__(self, nama):
        self.nama = nama

    def katakanHalo(self):
        print 'Halo, nama saya %s, apa kabar?' % self.nama

org = Orang('budi')
org.katakanHalo()
class Mobil:
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.kecepatan = 0

    def klakson(self):
        print("Beep! Beep!")
    def akselerasi(self, jumlah):
        self.kecepatan += jumlah
        print(f"Kecepatan mobil sekarang: {self.kecepatan} km/jam")

    def rem(self, jumlah):
        self.kecepatan -= jumlah
        if self.kecepatan < 0:
            self.kecepatan = 0
        print(f"Kecepatan mobil sekarang: {self.kecepatan} km/jam")


# Membuat objek mobil
mobil_saya = Mobil("Toyota", "Camry", 2020)

# Menjalankan metode klakson
mobil_saya.klakson()

# Menjalankan metode akselerasi dan rem
mobil_saya.akselerasi(20)
mobil_saya.rem(10)

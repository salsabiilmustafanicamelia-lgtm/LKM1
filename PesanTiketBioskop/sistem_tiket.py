class Movie:
    def __init__(self, judul, genre, durasi, harga):
        self.judul = judul
        self.genre = genre
        self.durasi = durasi
        self.harga = harga
        
class Snack:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        
class Tiket:
    def __init__(self, nama, member=False):
        self.nama = nama
        self.daftar_tiket = []
        self.daftar_snack = []
        self.tiket_sdh_bayar = []
        self.snack_sdh_bayar = []
        self.member = member

    def tambah_tiket(self, movie, jumlah=1):
        self.daftar_tiket.append([movie, jumlah])
        print(f"({self.nama}) Berhasil menambah: Tiket {movie.judul} x{jumlah}")
    
    def hapus_tiket(self, movie_hapus):
        for tiket in self.daftar_tiket:
            if tiket[0] == movie_hapus:
                self.daftar_tiket.remove(tiket)
                print(f"({self.nama}) Berhasil menghapus: Tiket {movie_hapus.judul}")
                return
        if self.daftar_tiket != movie_hapus:
            print(f"({self.nama}) Tiket {movie_hapus.judul} tidak ditemukan di daftar tiket.")
            
    def hitung_total(self):
        total = 0
        if self.daftar_tiket == []:
            for tiket in self.tiket_sdh_bayar:
                total += tiket[0].harga * tiket[1]
        else:
            for tiket in self.daftar_tiket:
                total += tiket[0].harga * tiket[1]
        return total
    
    def pesan_snack(self, snack, jumlah=1):
        self.daftar_snack.append([snack, jumlah])
        print(f"({self.nama}) Berhasil menambah: {snack.nama} x{jumlah}")
    
    def hapus_snack(self, snack_hapus):
        for snack in self.daftar_snack:
            if snack[0] == snack_hapus:
                self.daftar_snack.remove(snack)
                print(f"({self.nama}) Berhasil menghapus: {snack_hapus.nama}")
                return
        if self.daftar_snack != snack_hapus:
            print(f"({self.nama}) Snack {snack_hapus.nama} tidak ditemukan di daftar snack.")

    def hitung_total_snack(self):
        total = 0
        if self.daftar_snack == []:
            for snack in self.snack_sdh_bayar:
                total += snack[0].harga * snack[1]
        else:
            for snack in self.daftar_snack:
                total += snack[0].harga * snack[1]
        return total
    
    def bayar(self, uang_diterima):
        if self.daftar_tiket == []:
            total_snack = self.hitung_total_snack()
            total_bayar = total_snack
        elif self.daftar_snack == []:
            total_tiket = self.hitung_total()
            total_bayar = total_tiket
        else:
            total_tiket = self.hitung_total()
            total_snack = self.hitung_total_snack()
            total_bayar = total_tiket + total_snack
        
        if self.daftar_tiket == [] and self.daftar_snack == []:
            print(f"Belum ada pesanan!")
        
        elif uang_diterima >= total_bayar:
            kembalian = uang_diterima - total_bayar
            if self.member == True:
                diskon = total_bayar * 0.1
                total_bayar -= diskon
                print(f"({self.nama}) Anda mendapatkan diskon 10% sebagai member! Diskon: Rp{diskon}")
            if self.daftar_tiket == [] and self.daftar_snack != []:
                print(f"({self.nama}) Terima kasih telah memesan snack!")
            elif self.daftar_tiket != [] and self.daftar_snack == []:
                print(f"({self.nama}) Terima kasih telah memesan tiket!")
            else:
                print(f"({self.nama}) Terima kasih telah memesan tiket dan snack!")
            print(f"({self.nama}) Total bayar: Rp{total_bayar}")
            print(f"({self.nama}) Kembalian: Rp{kembalian}")
            for tiket in self.daftar_tiket:
                self.tiket_sdh_bayar.append(tiket)
                self.daftar_tiket.remove(tiket)
            for snack in self.daftar_snack:
                self.snack_sdh_bayar.append(snack)
                self.daftar_snack.remove(snack)
        else:
            print(f"({self.nama}) Uang yang diterima kurang. Total bayar: Rp{total_bayar}")
            
    def cetak_struk(self):
        print(f"\n=== Struk Pembelian {self.nama} ===")
        print("Tiket:")
        for tiket in self.tiket_sdh_bayar:
            print(f"- Tiket {tiket[0].judul} : Rp{tiket[0].harga} \n    x{tiket[1]} = Rp{tiket[0].harga * tiket[1]}")
        print("Snack:")
        for snack in self.snack_sdh_bayar:
            print(f"- {snack[0].nama} : Rp{snack[0].harga} \n    x{snack[1]} = Rp{snack[0].harga * snack[1]}")
        total = self.hitung_total() + self.hitung_total_snack()
        if self.member == True:
            diskon = total * 0.1
            total -= diskon
            print(f"Diskon Member: Rp{int(diskon)}")
        print(f"Total bayar: Rp{int(total)}")
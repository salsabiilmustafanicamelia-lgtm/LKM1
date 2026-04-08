class Produk:
  def __init__(self, nama, harga, stok):
    self.nama = nama
    self.harga = harga
    self.stok = stok
    
class Keranjang:
  def __init__(self, member=False):
    self.daftar_barang = []
    self.member = member
    
  def cek_stok(self, produk):
      print(f"{produk.nama} : {produk.stok}")
  
  def tambah_produk(self, produk_baru, jumlah=1):
    if produk_baru.stok >= jumlah:
      self.daftar_barang.append([produk_baru, jumlah])
      print(f"Berhasil menambah: {produk_baru.nama} x{jumlah}")
    else:
      print(f"Maaf, stok {produk_baru.nama} habis.")
      
  def hapus_produk(self, produk_hapus):
    for barang in self.daftar_barang:
      if barang[0] == produk_hapus:
        self.daftar_barang.remove(barang)
        print(f"Berhasil menghapus: {produk_hapus.nama}")
        return
    if self.daftar_barang != produk_hapus:
      print(f"Produk {produk_hapus.nama} tidak ditemukan di keranjang.")
    
  def hitung_total(self):
    total = 0
    for barang in self.daftar_barang:
      total += barang[0].harga * barang[1]
    return total
  
  def bayar(self, uang_diterima):
    total = self.hitung_total()
    if uang_diterima >= total:
      if self.member == True:
        diskon = total * 0.05
        total -= diskon
        print(f"Diskon Member (5%): Rp{diskon}")
        
      total += total * 0.11
      print(f"Total setelah PPN (11%): Rp{total}")
      
      kembalian = uang_diterima - total
      
      
      if kembalian > 0:
        print(f"Kembalian: Rp{kembalian}")
        print("Terima kasih telah berbelanja!")
      elif uang_diterima == self.hitung_total():
        print("Pembayaran tepat, terima kasih!")
        
  def cetak_struk(self):
    print("\n=== Struk Belanja ===")
    for barang in self.daftar_barang:
      print(f"- {barang[0].nama} : Rp{barang[0].harga} \n    x{barang[1]} = Rp{barang[0].harga * barang[1]}")
      
    total_akhir = self.hitung_total() #293000
    if self.member == True:
      diskon = total_akhir * 0.05
      print(f"\nDiskon (5%) \t: -Rp{diskon}")
      total_akhir -= diskon
      
    total_akhir += total_akhir * 0.11
    print(f"PPN (11%)      \t: Rp{total_akhir * 0.11}")
    print(f"Total Akhir \t: Rp{total_akhir}")
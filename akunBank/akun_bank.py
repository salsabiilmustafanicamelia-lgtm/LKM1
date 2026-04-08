class AkunBank:
  def __init__(self, nomor, pemilik, saldo_awal):
    self.nomor = nomor 
    self.pemilik = pemilik
    self.saldo = saldo_awal
    self.riwayat = []
  
  def cek_saldo(self):
    print(f"Saldo {self.pemilik}: Rp{self.saldo}")
    
  def tarik_tunai(self, jumlah):
    if jumlah <= 0:
      print("Jumlah tarik tunai harus lebih dari 0.")
    else:
      if jumlah <= self.saldo:
        self.saldo -= jumlah
        print(f"{self.pemilik} menarik Rp{jumlah}")
        self.riwayat.append(f"Tarik Tunai: -Rp{jumlah}")
      else:
        print("Saldo tidak cukup!")
  
  def transfer(self, tujuan, jumlah):
    if jumlah <= 0:
      print("Jumlah transfer harus lebih dari 0.")
    elif self.saldo >= jumlah:
      self.saldo -= jumlah
      tujuan.saldo += jumlah
      self.saldo -= 2500
      print(f"Transfer Rp{jumlah} ke {tujuan.pemilik} Berhasil!")
      self.riwayat.append(f"Transfer: -Rp{jumlah} \n Biaya Admin: -Rp2500")
      tujuan.riwayat.append(f"Transfer: +Rp{jumlah}")
    else:
      print("Transfer Gagal: Saldo tidak cukup.")
    
  def cek_riwayat(self):
    print(f"== Riwayat {self.pemilik} ==")
    num = 1
    for r in self.riwayat:
      print(f"{num}. {r}")
      num += 1
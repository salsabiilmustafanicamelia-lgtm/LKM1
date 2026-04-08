from akun_bank import AkunBank

akun1 = AkunBank("123", "Hafidz", 200000)
akun2 = AkunBank("234", "Almira", 500000)
# akun1 = AkunBank()
# akun1.nomor = "123"
# akun1.pemilik = "Hafidz"
# akun1.saldo = "200000"

akun1.tarik_tunai(300000)
akun2.transfer(akun1, 200000)
akun2.transfer(akun1, 0)
akun1.transfer(akun2, 50000)
akun1.tarik_tunai(0)
akun1.tarik_tunai(100000)
akun2.tarik_tunai(100000)

akun1.cek_saldo()
akun2.cek_saldo()

akun1.cek_riwayat()
akun2.cek_riwayat()
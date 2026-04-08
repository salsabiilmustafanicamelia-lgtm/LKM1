from sistem_kasir import Produk, Keranjang

p1 = Produk("Kopi Kenangan", 25000, 300)
p2 = Produk("Susu UHT", 18000, 250)
p3 = Produk("Keyboard Gaming", 250000, 50)

# del p3

keranjang_saya = Keranjang(True)
keranjang_saya.cek_stok(p1)
keranjang_saya.cek_stok(p2)
keranjang_saya.cek_stok(p3)

keranjang_saya.tambah_produk(p1)
keranjang_saya.tambah_produk(p2)
keranjang_saya.tambah_produk(p3)

keranjang_saya.hapus_produk(p2)

keranjang_saya.bayar(500000)
keranjang_saya.cetak_struk()
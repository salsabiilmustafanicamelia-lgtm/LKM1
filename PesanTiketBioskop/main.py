from sistem_tiket import Movie, Snack, Tiket

movie1 = Movie("Avengers: Endgame", "Action", 181, 50000)
movie2 = Movie("The Lion King", "Animation", 118, 40000)
movie3 = Movie("Joker", "Thriller", 122, 45000)

snack1 = Snack("Popcorn", 20000)
snack2 = Snack("Soda", 15000)
snack3 = Snack("Hot Dog", 25000)

p1 = Tiket("Ron", True)
p2 = Tiket("Jane")

p2.bayar(30000)

p1.tambah_tiket(movie1, 2)
p1.tambah_tiket(movie2, 1)
p1.pesan_snack(snack1, 2)
p1.pesan_snack(snack2, 1)

p1.hapus_tiket(movie2)

p2.tambah_tiket(movie3, 1)
p2.bayar(50000)

p2.pesan_snack(snack3, 1)
p2.bayar(50000)

p1.bayar(200000)

p1.cetak_struk()
p2.cetak_struk()
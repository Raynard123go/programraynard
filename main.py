meme_dict = {
    "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
    "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
    "ROFL": "Tanggapan terhadap lelucon",
    "SHEESH": "Sedikit ketidaksetujuan",
    "CREEPY": "menakutkan, tidak menyenangkan",
    "AGGRO": "untuk menjadi agresif/marah"
}

for i in range(5):
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

    if word in meme_dict.keys():
        # Apa yang harus kita lakukan jika kata itu ditemukan?
         print(meme_dict[word])
    else:
        # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
        print("Kata tidak ditemukan silakan coba lagi")

# Data dari soal
data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 400
        }
    }
}

# 1. Tampilkan seluruh data dari data_panen
print("Seluruh Data Panen:")
for lokasi, info in data_panen.items():
    print(f"Lokasi: {info['nama_lokasi']}")
    for komoditas, jumlah in info['hasil_panen'].items():
        print(f"  {komoditas.capitalize()}: {jumlah} kg")
    print()

# 2. Tampilkan jumlah hasil panen jagung dari lokasi2
jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Jumlah hasil panen jagung di lokasi2: {jagung_lokasi2} kg\n")

# 3. Tampilkan nama lokasi dari lokasi3
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3: {nama_lokasi3}\n")

# 4. Masukkan jumlah hasil panen padi dan kedelai ke dalam variabel
padi_per_lokasi = {lokasi: info['hasil_panen']['padi'] for lokasi, info in data_panen.items()}
kedelai_per_lokasi = {lokasi: info['hasil_panen']['kedelai'] for lokasi, info in data_panen.items()}

print("Jumlah hasil panen padi per lokasi:", padi_per_lokasi)
print("Jumlah hasil panen kedelai per lokasi:", kedelai_per_lokasi, "\n")

# 5. Percabangan untuk perhatian khusus atau kondisi baik
print("Status Lokasi Berdasarkan Hasil Panen:")
for lokasi, info in data_panen.items():
    padi = info['hasil_panen']['padi']
    jagung = info['hasil_panen']['jagung']
    status = "Memerlukan perhatian khusus" if padi > 1300 or jagung > 800 else "Kondisi baik"
    print(f"Lokasi: {info['nama_lokasi']} - {status}")

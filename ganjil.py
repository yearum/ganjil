# Data gaji pokok dan upah lembur per bagian
gaji_pokok = {
    'Produksi': 2500000,
    'Packing': 2450000,
    'Distribusi': 2350000
}

upah_lembur = {
    'Produksi': 25000,
    'Packing': 20000,
    'Distribusi': 25000
}

# Fungsi untuk menghitung tunjangan istri
def hitung_tunjangan_istri(gaji_pokok, status):
    if status == 'Menikah':
        return 0.15 * gaji_pokok
    return 0

# Fungsi untuk menghitung tunjangan anak (maksimal 3 anak)
def hitung_tunjangan_anak(gaji_pokok, jumlah_anak):
    if jumlah_anak > 3:
        jumlah_anak = 3
    return 0.10 * gaji_pokok * jumlah_anak

# Fungsi untuk menghitung gaji lembur
def hitung_gaji_lembur(upah_lembur, jam_lembur):
    gaji_lembur = upah_lembur * jam_lembur
    # Tambahan 10% jika jam lembur lebih dari 10 jam
    if jam_lembur > 10:
        gaji_lembur += 0.10 * gaji_lembur
    return gaji_lembur

# Fungsi utama untuk menghitung total gaji
def hitung_total_gaji(nama, status, bagian, jumlah_anak, jam_lembur):
    gaji_pokok_bagian = gaji_pokok[bagian]
    upah_lembur_bagian = upah_lembur[bagian]
    
    tunjangan_istri = hitung_tunjangan_istri(gaji_pokok_bagian, status)
    tunjangan_anak = hitung_tunjangan_anak(gaji_pokok_bagian, jumlah_anak)
    gaji_lembur = hitung_gaji_lembur(upah_lembur_bagian, jam_lembur)
    
    total_gaji = gaji_pokok_bagian + tunjangan_istri + tunjangan_anak + gaji_lembur
    
    return {
        'Nama': nama,
        'Bagian': bagian,
        'Gaji Pokok': gaji_pokok_bagian,
        'Tunjangan Istri': tunjangan_istri,
        'Tunjangan Anak': tunjangan_anak,
        'Gaji Lembur': gaji_lembur,
        'Total Gaji': total_gaji
    }

# Contoh input dan output
nama = input("Masukkan nama pegawai: ")
status = input("Masukkan status (Menikah/Belum Menikah): ")
bagian = input("Masukkan bagian (Produksi/Packing/Distribusi): ")
jumlah_anak = int(input("Masukkan jumlah anak: "))
jam_lembur = int(input("Masukkan jumlah jam lembur: "))

hasil = hitung_total_gaji(nama, status, bagian, jumlah_anak, jam_lembur)

# Output hasil
for k, v in hasil.items():
    print(f"{k}: {v}")

import re
import csv
import glob
from datetime import datetime

# === 1. Cari file .txt di folder ===
txt_files = glob.glob("*.txt")

if not txt_files:
    print("❌ Tidak ada file .txt di folder ini!")
    exit()

input_file = txt_files[0]
print(f"📄 Memproses file: {input_file}")

# === 2. Baca isi file ===
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# === 3. Regex untuk SUKSES dan GAGAL ===
pattern_sukses = re.compile(r"(\d+\.\d+)\s+SUKSES.*?(?:SN/Ref:)?(\d+)#")
pattern_gagal = re.compile(r"GAGAL\.(\d+\.\d+)#")

data_sukses = pattern_sukses.findall(text)
data_gagal = pattern_gagal.findall(text)

if not data_sukses and not data_gagal:
    print("⚠️ Tidak ditemukan data SUKSES maupun GAGAL di file ini.")
    exit()

# === 4. Hilangkan duplikat dan pisahkan data ===
seen = set()
unique_sukses = []
duplicates = []

for nominal, ref in data_sukses:
    key = (nominal, ref)
    if key not in seen:
        seen.add(key)
        unique_sukses.append((nominal, ref))
    else:
        duplicates.append((nominal, ref))

# === 5. Nama file hasil otomatis berdasarkan tanggal ===
tanggal = datetime.now().strftime("%Y-%m-%d")
output_file = f"rekap_sukses_{tanggal}.csv"

# === 6. Simpan hasil ke CSV (bisa dibuka Excel) ===
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Hasil"])

    # Bagian 1: SUKSES unik
    for nominal, ref in unique_sukses:
        writer.writerow([f"{nominal} SUKSES. SN/Ref:{ref}#"])

    # Bagian 2: Data duplikat
    if duplicates:
        writer.writerow([])
        writer.writerow(["=== DATA DUPLIKAT ==="])
        for nominal, ref in duplicates:
            writer.writerow([f"{nominal} SUKSES. SN/Ref:{ref}#"])

    # Bagian 3: Data GAGAL
    if data_gagal:
        writer.writerow([])
        writer.writerow(["=== DATA GAGAL ==="])
        for nominal in data_gagal:
            writer.writerow([f"GAGAL.{nominal}#"])

# === 7. Informasi ringkas di terminal ===
print(f"✅ Selesai! {len(unique_sukses)} data SUKSES unik disimpan ke '{output_file}'")

if duplicates:
    print(f"⚠️ {len(duplicates)} data duplikat ikut disimpan di bagian bawah.")
if data_gagal:
    print(f"❌ {len(data_gagal)} data GAGAL ikut disimpan di bagian paling bawah.")

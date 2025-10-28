import re
import csv
import glob
from datetime import datetime
from collections import defaultdict

# === 1. Cari file .txt di folder ===
txt_files = glob.glob("*.txt")

if not txt_files:
    print("❌ Tidak ada file .txt di folder ini!")
    exit()

input_file = txt_files[0]
print(f"📄 Memproses file: {input_file}")

# === 2. Baca isi file (per baris agar akurat) ===
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# === 3. Regex untuk SUKSES dan GAGAL (alfanumerik di SN/Ref) ===
pattern_sukses = re.compile(
    r"(\d+\.\d+)\s+SUKSES(?:\s*\.?)\s*(?:SN/Ref:)?\s*([A-Za-z0-9]+)#",
    flags=re.IGNORECASE,
)
pattern_gagal = re.compile(r"GAGAL\.(\d+\.\d+)#")

# === 4. Ambil data dari tiap baris ===
data_sukses = []
data_gagal = []

for line in lines:
    line = line.strip()
    if not line:
        continue
    m = pattern_sukses.search(line)
    if m:
        nominal = m.group(1)
        ref = m.group(2)
        data_sukses.append((nominal, ref))
        continue
    mg = pattern_gagal.search(line)
    if mg:
        data_gagal.append(mg.group(1))

# === 5. Jika kosong ===
if not data_sukses and not data_gagal:
    print("⚠️ Tidak ditemukan data SUKSES maupun GAGAL di file ini.")
    exit()

# === 6. Hilangkan duplikat (tetap untuk keamanan) ===
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

# === 7. Analisis relasi (anomali) ===
nominal_to_ref = defaultdict(set)
ref_to_nominal = defaultdict(set)

for nominal, ref in unique_sukses:
    nominal_to_ref[nominal].add(ref)
    ref_to_nominal[ref].add(nominal)

anomali = set()

# Nomor sama tapi SN/Ref beda
for nominal, refs in nominal_to_ref.items():
    if len(refs) > 1:
        for ref in refs:
            anomali.add((nominal, ref))

# SN/Ref sama tapi nomor beda
for ref, nominals in ref_to_nominal.items():
    if len(nominals) > 1:
        for nominal in nominals:
            anomali.add((nominal, ref))

# === 8. Pisahkan data sukses & perlu tindak lanjut ===
data_tindak = []
data_final_sukses = []

for nominal, ref in unique_sukses:
    if (nominal, ref) in anomali:
        data_tindak.append((nominal, ref))
    else:
        data_final_sukses.append((nominal, ref))

# === 9. Nama file hasil otomatis ===
tanggal = datetime.now().strftime("%Y-%m-%d")
output_file = f"rekap_sukses_{tanggal}.csv"

# === 10. Simpan ke CSV (format tetap satu kolom 'Hasil') ===
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Hasil"])

    # Bagian 1: DATA SUKSES
    writer.writerow(["=== DATA SUKSES ==="])
    for nominal, ref in data_final_sukses:
        writer.writerow([f"{nominal} SUKSES. SN/Ref:{ref}#"])

    # Bagian 2: DATA PERLU TINDAK LANJUT
    if data_tindak:
        writer.writerow([])
        writer.writerow(["=== DATA PERLU TINDAK LANJUT (Nomor sama SNRef beda atau Nomor beda SNRef sama) ==="])
        for nominal, ref in data_tindak:
            writer.writerow([f"{nominal} SUKSES. SN/Ref:{ref}#"])

    # Bagian 3: DATA GAGAL
    if data_gagal:
        writer.writerow([])
        writer.writerow(["=== DATA GAGAL ==="])
        for nominal in data_gagal:
            writer.writerow([f"GAGAL.{nominal}#"])

print(f"✅ Selesai! {len(data_final_sukses)} data sukses unik disimpan ke '{output_file}'")

if data_tindak:
    print(f"⚠️ {len(data_tindak)} data perlu tindak lanjut (anomali).")
if data_gagal:
    print(f"❌ {len(data_gagal)} data gagal ditemukan.")

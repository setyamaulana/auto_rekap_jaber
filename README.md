# 🧾 Jabber Log Rekap Bot

Bot Python otomatis untuk **merekap data transaksi dari log Jabber (Pidgin)** ke dalam file **Excel/CSV**.  

---

## 🚀 Fitur Utama

✅ Otomatis mendeteksi file `.txt` log Jabber di folder (tanpa perlu nama file tertentu)  
✅ Mengambil hanya baris **SUKSES** dari log (format nominal `5.` atau `15.`)  
✅ Menghapus data **duplikat** secara otomatis  
✅ Memisahkan data yang **perlu tindak lanjut (anomali)**:  
 - Nomor sama tapi SN/Ref berbeda  
 - SN/Ref sama tapi Nomor berbeda  
✅ Menambahkan **data GAGAL** di bagian paling bawah hasil  
✅ Menyimpan hasil ke file `.csv` yang bisa langsung dibuka di Excel  
✅ Nama file hasil otomatis berdasarkan tanggal (misal `rekap_sukses_2025-10-28.csv`)  
✅ 100% menggunakan modul bawaan Python (tidak perlu install apa pun)  

---

## ⚙️ Cara Menggunakan

1️⃣ **Clone repo ini atau salin script Python-nya ke folder kosong.**  
2️⃣ **Letakkan file log Jabber (`.txt`) di folder yang sama.**  
 Nama file bebas, contoh: `jaber.txt` atau `loghariini.txt`.  
3️⃣ **Jalankan script**  
   ```bash
   python auto_rekap_jaber.py
   ```

4️⃣ Bot akan otomatis memproses file .txt pertama di folder, lalu menghasilkan file .csv
Contoh: rekap_sukses_2025-10-28.csv

---

📊 Contoh Output (Hasil di Excel / CSV)

| Hasil                                                                               |
| ----------------------------------------------------------------------------------- |
| === DATA SUKSES ===                                                                 |
| 5.085234695380 SUKSES. SN/Ref:03946500000446713915#                                 |
| 5.087882925410 SUKSES. SN/Ref:20101028403476#                                       |
| *(kosong)*                                                                          |
| === DATA PERLU TINDAK LANJUT (Nomor sama SNRef beda atau Nomor beda SNRef sama) === |
| 5.083878759186 SUKSES. SN/Ref:28102164#                                             |
| 5.083878759186 SUKSES. SN/Ref:TKXL28102164CB#                                       |
| *(kosong)*                                                                          |
| === DATA GAGAL ===                                                                  |
| GAGAL.5.085600017994#                                                               |


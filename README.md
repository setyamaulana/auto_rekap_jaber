# 🧾 Jabber Log Rekap Bot

Bot Python otomatis untuk **merekap data transaksi dari log Jabber (Pidgin)** ke dalam file **Excel/CSV**.  
Dirancang agar bekerja sepenuhnya otomatis tanpa perlu library tambahan seperti `pandas`.

---

## 🚀 Fitur Utama

✅ Otomatis mendeteksi file `.txt` log Jabber di folder (tanpa perlu nama file tertentu)  
✅ Mengambil hanya baris **SUKSES** dari log  
✅ Menghapus data **duplikat** secara otomatis  
✅ Menampilkan **data duplikat** di bagian bawah hasil  
✅ Menambahkan **data GAGAL** di bagian paling bawah hasil  
✅ Menyimpan hasil ke file `.csv` yang bisa langsung dibuka di Excel  
✅ Nama file hasil otomatis berdasarkan tanggal (misal `rekap_sukses_2025-10-27.csv`)  
✅ 100% menggunakan modul bawaan Python (tidak perlu install apa pun)

---

## 📂 Contoh Input Log

Contoh isi file `.txt` hasil salinan log dari Jabber (Pidgin):

(9:19:02 AM) apanhost3@jabb.im
: 5.085234695380 SUKSES. SN/Ref:03946500000446713915#
(9:20:51 AM) apanhost3@jabb.im
: 5.082269076083 SUKSES. SN/Ref:03946700000446746907#
(9:35:15 AM) apanhost3@jabb.im
: GAGAL.5.085600017994#

---

## ⚙️ Cara Menggunakan

### 1 Clone repo
### 2 Copas data jaber ke txt
### 3 Run Bot


---

## 📊 Contoh Output (Hasil di Excel / CSV)

| Hasil |
|-------|
| 5.085234695380 SUKSES. SN/Ref:03946500000446713915# |
| 5.082269076083 SUKSES. SN/Ref:03946700000446746907# |
| *(kosong)* |
| === DATA DUPLIKAT === |
| 5.082269076083 SUKSES. SN/Ref:03946700000446746907# |
| *(kosong)* |
| === DATA GAGAL === |
| GAGAL.5.085600017994# |

---


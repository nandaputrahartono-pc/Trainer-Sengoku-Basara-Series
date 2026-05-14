# 🎮 Sengoku Basara HD Collection - Trainer

Trainer / Cheat Engine untuk game **Sengoku Basara HD Collection** yang berjalan di emulator **RPCS3** (PlayStation 3 Emulator).

Program ini dibuat menggunakan Python dengan GUI **CustomTkinter** dan memory editing menggunakan **Pymem**.

> ⚠️ **Khusus Windows** — Program ini hanya bisa berjalan di sistem operasi Windows karena menggunakan Windows API untuk membaca dan menulis memori proses RPCS3.

---

## ✨ Fitur

### Sengoku Basara 2 Heroes
- **Playable Matsunaga Hisahide** — Mainkan karakter Matsunaga Hisahide yang biasanya terkunci
- **Change Element** — Ganti elemen serangan karakter (Fire, Thunder, Ice, Dark, Wind, Light, Physical) dengan fitur freeze
- **Ganti Senjata** — Ubah senjata karakter sesuka hati (Weapon 1-8)
- **Ganti Kostum** — Ganti kostum karakter (Costume 1-3)
- **Cheat Duit** — Masukkan jumlah uang (Ryo) sesuai keinginan

### Coming Soon
- Sengoku Basara 1
- Sengoku Basara 2

---

## 📦 Instalasi (Dari Source Code)

### Prasyarat
- Python 3.10+ terinstall
- RPCS3 Emulator sudah berjalan dengan game Sengoku Basara HD Collection

### Langkah-langkah

1. Clone repository ini:
   ```bash
   git clone https://github.com/nandaputrahartono-pc/Trainer-Sengoku-Basara-Series.git
   cd Trainer-Sengoku-Basara-Series
   ```

2. Install library yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan program:
   ```bash
   python main.py
   ```

---

## 📚 Library yang Digunakan

| Library | Kegunaan |
|---------|----------|
| `customtkinter` | Framework GUI modern berbasis Tkinter |
| `Pillow` | Memuat gambar/logo untuk tampilan |
| `pymem` | Membaca & menulis memori proses (RPCS3) |

---

## 🕹️ Cara Pakai

1. Buka **RPCS3** dan jalankan game **Sengoku Basara HD Collection**
2. Buka **Trainer** (`main.py` atau file `.exe`)
3. Klik tombol **"RPCS3 Disconnected"** di sidebar untuk menghubungkan ke RPCS3
4. Pilih tab **Sengoku Basara 2 Heroes**
5. Aktifkan cheat yang kamu inginkan!

---

## 📁 Struktur File

```
├── main.py          # Entry point - GUI utama (CustomTkinter)
├── trainer.py       # Logic trainer - baca/tulis memori RPCS3
├── cheat.py         # Versi CLI (command line) dari trainer
├── c.py             # Versi GUI alternatif / prototype
├── logo.png         # Logo aplikasi
└── requirements.txt # Daftar library Python
```

---

## 👤 Author

**Nanda Putra Hartono**

---

*Dibuat untuk keperluan edukasi dan eksplorasi memory editing.*

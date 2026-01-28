# 🛡️ SSH Log Analyzer (SOC Analyst Simulation)

Proyek ini adalah sarana gue buat latihan Python sekaligus nyimulasikan kerja seorang SOC Analyst. Gue pengen tau gimana cara ngubah ribuan baris log berantakan jadi data keamanan yang berguna.

> [!IMPORTANT]  
> **PURE LOGIC - NO EXTERNAL LIBRARIES!**  
> Proyek ini sengaja gue bikin tanpa library tambahan kayak Pandas atau Regex buat pengolahan datanya. Semua proses parsing, sorting, sampai correlation logic murni pake algoritma Python dasar. Library eksternal cuma pake Flask buat nampilin dashboard web.

## 🚀 Fitur yang Udah Gue Buat

Bagian ini ngejelasin fitur utama yang udah gue bangun sampai sekarang. Semua fitur fokus ke analisis log SSH dan simulasi kerja SOC.

- **Advanced Log Parsing**  
  Ekstraksi data IP, user, jam, dan status login secara manual tanpa bantuan regex.

- **Real-time Brute Force Detector**  
  Sistem bakal nge-trigger ALARM kalau ada IP yang gagal login berkali-kali dalam 60 detik. Mekanismenya pake sliding window logic manual.

- **Session Correlation**  
  Fitur paling sakti. Bisa ngelacak IP yang tadinya gagal berkali-kali tapi akhirnya berhasil masuk sebagai indikasi breach.

- **Target Profiling**  
  Sistem bisa nunjukkin user mana aja yang paling sering jadi target serangan.

- **Dual Interface**  
  Lo bisa lihat laporan via terminal mode CLI atau lewat web dashboard berbasis Flask.


## ⚠️ Known Issues & Future Improvements
Gue sadar proyek ini masih jauh dari sempurna, beberapa hal yang pengen gue improve nanti:
- **Optimization**: Parsing manual string splitting masih berat kalau log-nya jutaan baris.
- **Data Persistence**: Data blacklist masih ilang kalau program dimatiin (belum pake Database).
- **Real-time**: Masih baca file statis, belum *live stream* log yang baru masuk.
- **False Positives**: Belum ada mekanisme bedain user yang typo sama serangan bot asli.

## 🛠️ Installation & Usage

Bagian ini jelasin cara setup proyek sama cara jalaninnya. Flask jadi satu-satunya library eksternal yang perlu lo install.

### Clone & Prepare

Lakuin langkah ini dulu buat nyiapin project di mesin lo.

```bash
git clone https://github.com/MRizkiii/practice-soc-analyst.git
cd practice-soc-analyst
```

### Install Flask (The only library I use)

Flask dipake buat nampilin dashboard web yang nunjukin hasil analisis log.

```bash
pip install flask
```

### Run the Dashboard (Web Mode)

Mode ini cocok kalau lo pengen lihat hasil analisis lewat browser.

```bash
python app.py
```

Lalu buka URL berikut di browser lo:

```text
http://127.0.0.1:5000
```

### Run the Terminal (CLI Mode)

Mode ini cocok kalau lo pengen langsung interaksi via terminal.

```bash
python main.py
```

## 🤝 Contribution & Feedback

Karena gue masih tahap belajar dan eksplorasi, kodingan ini mungkin belum sempurna. Masukan dan kontribusi dari lo bakal sangat ngebantu peningkatan proyek ini.

- **Pull Requests sangat welcome**  
  Sikat aja kalau lo mau bantu rapiin logic gue atau nambahin fitur baru.

- **Diskusi dan Bug Report**  
  Kalau lo mau diskusi, ngasih ide, atau nemu bug, langsung aja buka Issue di repo ini.
	
	
	
## 📝 Learning Journey (The Scribbles)

Gue sengaja lampirin catatan coretan tangan gue pas lagi nyusun logika proyek ini. Ini bukti kalau semuanya murni hasil mikir dan coret-coret di buku, bukan cuma asal copas kode.

<details>
<summary><b>📖 Klik buat liat catatan belajar gue</b></summary>
<br>

| | |
|:---:|:---:|
| <img src="https://app.docuwriter.ai/storage/5Vnl8eNXJ7p6kOT4iN3pKCfm2Ysh2LIBSDfVY0yU.jpg" width="100%"> | <img src="https://app.docuwriter.ai/storage/VJvWsEZ8IND8sN0wc16gqPi4z8iWSnFvcn86BXyx.jpg" width="100%"> |
| <img src="https://app.docuwriter.ai/storage/fOP6i9zapl9V6hOOwXyfctjyJs1sGQG3cpLAhfJa.jpg" width="100%"> | <img src="https://app.docuwriter.ai/storage/tk5u5sS6xJJqvmygNyCWHKrejvXXfyMqcAs4gwiE.jpg" width="100%"> |
| <img src="https://app.docuwriter.ai/storage/LuJeBgeGPAKPLEtO6zjSPIjwhaoH1jHRgWb9ekJu.jpg" width="100%"> | <img src="https://app.docuwriter.ai/storage/pUxo6xio2XS91FtYE1h8NaPvnmMglamF8JLfYZ7a.jpg" width="100%"> |
| <img src="https://app.docuwriter.ai/storage/9WnR2cugozhTWqzX1uBdVIj1aYVm1jrX0qAzIGxv.jpg" width="100%"> | <img src="https://app.docuwriter.ai/storage/NHnZXikN2jfqx5x7xTiSveRiiWcY8tfE8o3ZYVuU.jpg" width="100%"> |
| <img src="https://app.docuwriter.ai/storage/I875X3acXPqr26xitL0hRuauxPmmClHxxvboxw7G.jpg" width="100%"> | |

</details>
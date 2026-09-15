# portfolio-aliyushedri

Website statis default bahasa Inggris dengan sakelar EN/ID. Buka melalui server lokal:

```powershell
python -m http.server 4173 --bind 127.0.0.1
```

Kunjungi http://127.0.0.1:4173. Hentikan server dengan Ctrl+C.

## Mengubah konten

- `tools/build_site.py`: konten beranda dan detail proyek; jalankan `python tools/build_site.py` untuk menghasilkan ulang HTML.
- `styles.css`: tampilan desktop dan mobile.
- `app.js`: menu mobile dan filter proyek.
- `index.html` dan `index-id.html`: beranda Inggris dan Indonesia. Halaman proyek dengan akhiran `-id.html` adalah padanan bahasa Indonesia.
- Sertifikat dibuka dalam dialog di website, tanpa tautan unduh PDF. Bagian CV menyediakan dua versi bahasa.
- `assets/`: foto WebP, font lokal, CV dan sertifikat yang ditautkan.
- File CV dan folder aset asli tetap menjadi sumber, bukan output generator.

## GitHub Pages

Repositori: https://github.com/aliyushedri/portfolio-aliyushedri

Alamat website: https://aliyushedri.github.io/portfolio-aliyushedri/

Sumber publikasi: branch `main`, folder `/` (root), dengan `.nojekyll` untuk website statis. Setelah mengedit konten, jalankan generator lalu commit dan push perubahan:

```powershell
python tools/build_site.py
git add .
git commit -m "Update portfolio"
git push
```

Bahan mentah, catatan lokal, dan PDF sertifikat tidak disertakan. CV yang tersedia untuk diunduh dan gambar sertifikat untuk dialog tetap berada dalam `assets`. Domain Name.com belum dihubungkan.

## Catatan konten

Target RMSE pada proyek SLAM bukan hasil yang telah dicapai. Rincian instalasi magang dibatasi pada informasi CV dan dokumentasi yang tersedia. Tidak ada angka benchmark, publikasi, atau testimoni yang dibuat-buat.

# Bouncing Ball in Spinning Hexagon

## Deskripsi
Program ini adalah simulasi fisika sederhana yang menampilkan sebuah bola memantul di dalam segi enam (hexagon) yang berputar. Program ini menggunakan library `pygame` untuk menggambar grafis 2D dan menerapkan fisika seperti gravitasi, gesekan, serta pantulan realistis.

Fitur utama:
- **Segi Enam Berputar**: Segi enam berputar secara terus-menerus.
- **Bola Memantul**: Bola bergerak di dalam segi enam dan memantul saat bertabrakan dengan dinding.
- **Gravitasi dan Gesekan**: Gravitasi menarik bola ke bawah, sedangkan gesekan mengurangi kecepatan bola seiring waktu.
- **Pantulan Realistis**: Bola memantul dengan arah yang sesuai berdasarkan sudut tabrakan.

## Cara Menjalankan Program

### Prasyarat
1. Pastikan Python sudah terinstal di komputer Anda. Versi Python 3.6 atau lebih tinggi direkomendasikan.
2. Instal library `pygame` dengan menjalankan perintah berikut:
   ```bash
   pip install pygame
   ```

### Langkah-langkah
1. Simpan kode program ke dalam file bernama `bouncing_ball.py`.
2. Jalankan program menggunakan perintah berikut:
   ```bash
   python bouncing_ball.py
   ```
3. Jendela simulasi akan muncul, menampilkan bola yang memantul di dalam segi enam yang berputar.

## Kontrol
- Program akan berjalan secara otomatis setelah dijalankan.
- Untuk keluar dari program, klik tombol **Close** pada jendela simulasi atau tekan kombinasi tombol **Ctrl + C** di terminal.

## Penjelasan Kode
1. **Segi Enam**:
   - Segi enam digambar menggunakan rumus trigonometri untuk menghitung posisi titik-titik sudutnya.
   - Sudut rotasi segi enam diperbarui setiap frame untuk menciptakan efek berputar.

2. **Fisika Bola**:
   - Gravitasi diterapkan dengan menambahkan nilai tetap ke komponen vertikal kecepatan bola.
   - Gesekan mengurangi kecepatan bola secara bertahap untuk mensimulasikan hilangnya energi.

3. **Deteksi Tabrakan**:
   - Jarak antara pusat bola dan garis tepi segi enam dihitung untuk mendeteksi tabrakan.
   - Jika bola menyentuh tepi segi enam, kecepatannya dipantulkan berdasarkan normal permukaan.

4. **Pantulan**:
   - Saat terjadi tabrakan, vektor kecepatan bola dipantulkan menggunakan rumus refleksi vektor.

5. **Penanganan Kasus Ekstrem**:
   - Jika bola keluar dari segi enam karena kesalahan perhitungan, bola akan didorong kembali ke dalam dan kecepatannya disesuaikan.

## Kontribusi
Jika Anda ingin berkontribusi atau memiliki saran untuk meningkatkan program ini, silakan buat _pull request_ atau ajukan _issue_ di repositori GitHub.

## Lisensi
Program ini dilisensikan di bawah lisensi MIT. Lihat file `LICENSE` untuk informasi lebih lanjut.

## Penulis
Program ini dibuat oleh [Rahmat mulia]. Silakan hubungi saya melalui email: [Rahmatzkk10@gmail.com] jika ada pertanyaan atau masalah.

---

Semoga Anda menikmati simulasi ini! 😊

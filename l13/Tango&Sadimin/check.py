#checks if all chapters are in markdown file

#opens file
with open("tango&sadimin_Clean.md", "r", encoding="utf8") as f1:
    text = f1.read()

#table of content of novel
toc = """Bagian 1
Nini Randa & Satun Sadat
Tungku
Dia Tidak Lahir, Tetapi Muncul
Orok
Sungai Dasar Laut
Fase Ikan Kecil Terjebak di Kolam Lumpur
Fase Kuburan dan Pohon Pisang
Fase Bulan Tenggelam di Sungai
Satun Sadat
Rumah dan Bayi
Mandor
Hal Seperti Kopi dan Singkong
Fase Ikan Melompat Sendiri Ke Jaring
Sandera
Melepaskan Sadimin
Kepergian Cainah
Permainan
Tragedi Kasep
Dana
Bagian 2
Tango & Sadimin
Firasat
Toko Kelontong Menjelang Subuh
Mengapa Bunglon Berubah Warna\?
Udan Kethek Ngilo
Malam Gusaran
Gerandong
Perumpamaan Kodok
Geng Tutup Botol
Perempuan Paket 20 Ribu
Sebuah Cerita
Sebuah Fakta
Cemani
Buruh Sehari
Pembicaraan di Rumah Miring
Nama yang Lain
Bagian 3
Nah & Dana
Bangkai
Ibu Bernama Setan
Ibu Bernama Lumbung
Kelas Para Janda
Pelajaran Tentang Laki-laki
Pencarian Pertama
Hari-Hari Meminta
Nira
Perayaan yang Sedih
Dan Dia pun Mengumpat
Perbincangan dengan Pingki
Sejarah Ayah dan Anak
Sejarah Ibu dan Anak
Bagian 4
Ozog & Sipon
Bulan Mata Kucing
Keluarga Peniup Seruling
OM. Perawania
Lubang Hidung
Permainan Domino Paling Membahagiakan
Anak-anak Memipihkan Paku
Hutan Hujan Madu
Harkat Pengemis
Mawar Bodas 
Bagian 5
Misbah & Nyai
Kronologi Kehilangan
Tiga Kamar
Laku
Ujung Dunia
Semua yang Terbang ke Langit"""

#splits string at new lines
tocList = toc.split("\n")

#iterates through each splitted line
for i in tocList:
    #gets activated when there pattern not in the text
    if "## " + i not in text:
        #prints the chapter which is not found in the markdown file
        print(i)
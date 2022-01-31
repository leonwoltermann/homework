import re
import pandas as pd
import itertools

#table of content string
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

#splits string by lines
tocList = toc.split("\n")


#opens file
with open("tango&sadimin.txt", "r", encoding="utf8") as f1:
    textRaw = f1.read()
    #cleanes indentations
    textRaw = textRaw.replace("", "")
    
    #iterates through table of content list
    for t in tocList:
        #replaces every new line or beginig of a new line before element t (chapter name) with the pattern below
        textRaw = re.sub(r"(\n|^)%s\n" % t, "\n\n\n## %s.\n\n" % t, textRaw)

    #text cleaning
    textRaw = re.sub("\n+", "\n", textRaw)
    textRaw = re.sub(r"\n([A-Z])", r"\n\n\1", textRaw)
    textRaw = re.sub("\n([\d]+)\n", r"\n", textRaw)
    textRaw = re.sub(r"([a-z])-\n([a-z])", r"\1\2", textRaw)
    textRaw = re.sub(r"\n([a-z])", r" \1", textRaw)
    textRaw = re.sub(" +", " ", textRaw)
    textRaw = re.sub(" +\n", "\n", textRaw)
    textRaw = re.sub(r"([a-z])\n+", r"\1 ", textRaw)
    textRaw = re.sub(r"\[[0-9]*\]", "", textRaw)
    textRaw = re.sub(r"\n##", r"\n\n\n##", textRaw)

    #converts characters into lower case
    textRaw = textRaw.lower()

#assigns new var name
textClean = textRaw

#writes the string in var to file
with open("tango&sadimin_Clean.md", "w", encoding="utf8") as f9:
    f9.write(textClean)
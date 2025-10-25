"""
========================================
CATATAN QUERYSET DJANGO
========================================

File ini berisi catatan penting tentang Django QuerySet
untuk referensi cepat. Simpan sebagai file .py untuk referensi.

Asumsi: Model yang digunakan bernama 'Artikel'.
(Misal: from nama_app.models import Artikel)


--- 1. Perintah Dasar & Pengambilan Data ---

Perintah                     Fungsi Utama
---------------------------  -------------------------------------------------------
python manage.py shell       Memulai shell interaktif Django.

Artikel.objects.all()        Mengambil SEMUA objek (semua baris) dari model 'Artikel'.

Artikel.objects.get(...)     Mengambil TEPAT SATU objek.
                             (Akan ERROR jika 0 atau >1 data ditemukan).
                             Contoh: Artikel.objects.get(id=5)

Artikel.objects.first()      Mengambil objek PERTAMA dari hasil query.

Artikel.objects.last()       Mengambil objek TERAKHIR dari hasil query.


--- 2. Memfilter QuerySet (Filter, Exclude, dan Lookup __) ---

* Artikel.objects.filter(...)
    Fungsi: Mengambil SEMUA objek yang COCOK (hasil bisa banyak).
    Contoh: Artikel.objects.filter(kategori="blog")

* Artikel.objects.exclude(...)
    Fungsi: Mengambil SEMUA objek KECUALI yang cocok.
    Contoh: Artikel.objects.exclude(kategori="gibah")


Memahami Sintaks __ (Dua Underscore)
-------------------------------------------
Digunakan untuk Tipe Pencocokan (Lookup) atau Mengakses Relasi (Foreign Key).

A. Tipe Pencocokan (Lookup)

Sintaks Lookup               Arti / Fungsi
---------------------------  -------------------------------------------------------
field="nilai"                Sama dengan field__exact="nilai". (Paling umum)
                             Contoh: Artikel.objects.get(judul="hebu")

field__exact="nilai"         Sama dengan (Persis, case-sensitive / sensitif huruf).
                             Contoh: Artikel.objects.get(judul__exact="hebu")

field__iexact="nilai"        Sama dengan (IGNORE case / TIDAK sensitif huruf).
                             Contoh: Artikel.objects.get(judul__iexact="channel sumantris...")

field__contains="kata"       Mengandung kata (case-sensitive).
                             Contoh: Artikel.objects.filter(judul__contains="Django")

field__icontains="kata"      Mengandung kata (IGNORE case).
                             Contoh: Artikel.objects.filter(judul__icontains="django")


B. Mengakses Relasi (Foreign Key)

Contoh: Artikel.objects.filter(kategori__nama="blog")

Penjelasan:
1.  'kategori' adalah field Foreign Key di model 'Artikel'.
2.  '__nama'   berarti "akses field 'nama' di dalam model 'kategori'".
3.  '="blog"'   adalah nilainya.
Arti: "Cari semua 'Artikel' yang 'kategori'-nya punya 'nama' = 'blog'."


--- 3. Mengurutkan & Mengubah Format Hasil ---

Perintah                     Fungsi Utama
---------------------------  -------------------------------------------------------
.order_by("field")           Mengurutkan hasil (Ascending / A-Z).
                             Contoh: Artikel.objects.order_by("judul")

.order_by("-field")          Mengurutkan hasil (Descending / Z-A).
                             (Tanda minus '-' berarti terbalik).
                             Contoh: Artikel.objects.order_by("-judul")

...filter(...).order_by(...) Chaining (Rantai): Menggabungkan beberapa metode.
                             Contoh: Artikel.objects.filter(kategori__nama="blog").order_by("-judul")

.values("f1", "f2")          Mengembalikan hasil sebagai daftar Dictionary Python.
                             Contoh: Artikel.objects.values("id", "judul")

.values_list("f1", "f2")     Mengembalikan hasil sebagai daftar Tuple Python.
                             Contoh: Artikel.objects.values_list("id", "judul")

"""

# --- Contoh Kode (bisa di-uncomment untuk testing di shell) ---

# Baris ini HANYA akan berfungsi jika dijalankan di dalam 'python manage.py shell'
# dan kamu sudah punya model 'Artikel' dan 'Kategori' di 'nama_app'
#
# from nama_app.models import Artikel, Kategori
#
# def test_queries():
#     print("--- Menjalankan Tes Query ---")
#
#     # 1. Mengambil semua
#     semua_artikel = Artikel.objects.all()
#     print(f"Semua Artikel: {semua_artikel}")
#
#     # 2. Get satu objek
#     try:
#         artikel_spesifik = Artikel.objects.get(id=1)
#         print(f"Artikel ID 1: {artikel_spesifik}")
#     except Artikel.DoesNotExist:
#         print("Artikel ID 1 tidak ditemukan.")
#
#     # 3. Filter (case-insensitive) dan akses relasi
#     artikel_blog = Artikel.objects.filter(kategori__nama__iexact="blog")
#     print(f"Artikel Blog: {artikel_blog}")
#
#     # 4. Exclude dan Order By
#     selain_gibah = Artikel.objects.exclude(kategori__nama="gibah").order_by('-judul')
#     print(f"Selain Gibah (Z-A): {selain_gibah}")
#
#     # 5. Values (Dictionary)
#     judul_saja = Artikel.objects.values('judul')
#     print(f"Judul (dict): {judul_saja}")
#
#     print("--- Tes Selesai ---")

# Untuk menjalankan fungsi tes di atas:
# 1. python manage.py shell
# 2. from catatan_django import test_queries  (ganti 'catatan_django' dengan nama file .py kamu)
# 3. test_queries()

if __name__ == "__main__":
    # Bagian ini tidak akan berjalan di 'shell',
    # tapi hanya jika kamu menjalankan 'python nama_file.py'
    print("Ini adalah file catatan Django QuerySet.")
    print("Buka file ini untuk melihat catatan lengkap di bagian atas.")
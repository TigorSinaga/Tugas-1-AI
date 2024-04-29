data_mahasiswa = [
  { 'nim': '22.11.4725', 'nama': 'Tigor Sinaga', 'prodi': 'Informatika', 'semester': 4},
  { 'nim': '22.11.4733', 'nama': 'Raditya Dias', 'prodi': 'Sistem Informasi', 'semester': 2 },
  { 'nim': '22.11.4719', 'nama': 'Azhar Firdaus', 'prodi': 'Informatika', 'semester': 1 },
  { 'nim': '22.11.4715', 'nama': 'Alvin Amba', 'prodi': 'Sistem Informasi', 'semester': 1 },
]

kata_kunci_pencarian = ''
pilihan_kolom = ['NIM', 'Nama', 'Prodi', 'Semester']
index_kolom = None

def merge_sort(lst) :
  if len(lst) <= 1 : return lst
  
  mid = len(lst) // 2
  
  left = merge_sort(lst[:mid])
  right = merge_sort(lst[mid:])

  return merge(left, right)

def merge(left, right) :
  result = []
  i, j = 0, 0

  while i < len(left) and j < len(right) :
    if left[i][pilihan_kolom[index_kolom].lower()] < right[j][pilihan_kolom[index_kolom].lower()] :
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result += left[i:]
  result += right[j:]
  
  return result

def fungsi_pencarian_mahasiswa(mahasiswa) :
  kata_kunci_sesuai_nim = kata_kunci_pencarian in mahasiswa['nim']
  kata_kunci_sesuai_nama = kata_kunci_pencarian in mahasiswa['nama']
  kata_kunci_sesuai_prodi = kata_kunci_pencarian in mahasiswa['prodi']
  kata_kunci_sesuai_semester = kata_kunci_pencarian in str(mahasiswa['semester'])

  return kata_kunci_sesuai_nim or kata_kunci_sesuai_nama or kata_kunci_sesuai_prodi or kata_kunci_sesuai_semester

def ambil_data_mahasiswa() :
  data_mahasiswa_yang_dicari = list(filter(fungsi_pencarian_mahasiswa, data_mahasiswa))
  
  if index_kolom is not None:
    data_mahasiswa_yang_diurutkan = merge_sort(data_mahasiswa_yang_dicari)
  else:
    data_mahasiswa_yang_diurutkan = data_mahasiswa_yang_dicari

  return data_mahasiswa_yang_diurutkan

def menu_cari_mahasiswa() :
    global kata_kunci_pencarian, index_kolom

    kata_kunci_pencarian = input('\nSilakan masukan kata kunci untuk mencari mahasiswa:\n> ')

    mahasiswa_yang_dicari = ambil_data_mahasiswa()

    if mahasiswa_yang_dicari:
        print(f"Mahasiswa dengan kata kunci '{kata_kunci_pencarian}' yang ditemukan:")
        for mahasiswa in mahasiswa_yang_dicari :
            print('NIM           :', mahasiswa['nim'])
            print('Nama          :', mahasiswa['nama'])
            print('Program Studi :', mahasiswa['prodi'])
            print('Semester      :', mahasiswa['semester'], '\n')
    else:
        print(f"Mahasiswa dengan kata kunci '{kata_kunci_pencarian}' tidak ditemukan.\n")

    return app()



def pilih_menu() :
  print('[1] Cari mahasiswa')
  print('[2] Keluar')

  return input('Pilih menu:\n> ')


def app(show_title=False) :
  if show_title :
    print("\nAplikasi Data Mahasiswa")
    print('- ' * 15, '\n')

  try :
    index_menu = int(pilih_menu())

    if index_menu == 1 :
      return menu_cari_mahasiswa()
    elif index_menu == 2 :
      print('Sampai jumpa :)')
      exit()
  except KeyboardInterrupt :
    exit()

app(show_title=True)

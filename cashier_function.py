"""
File ini berisikan kumpulan function yang nantinya akan digunakan di main.py 
"""

# import tabulate untuk print table dalam format tabulate 
from tabulate import tabulate

# mendeklarasikan dictionary kosong, supaya dapat diinput data pembelian kedalamnya, dan dapat diedit nantinya 
dict_barang = {} 

# fungsi 1; Input barang 
def input_barang(): 
    """
    Fungsi ini dibuat untuk memasukkan item-item baru kedalam dictionary kosong yang tadi sudah dibuat
    Input yang diharapkan kedalam dictionary diatas adalah: nama_item: string; total_item: integer; harga_item: integer. 
    """

    global dict_barang 

    try: 
        # menggunakan loop untuk menampung inputan user
        while True: 
            nama_barang = input("Masukkan nama barang: ").strip().title() 
            jumlah_barang = int(input("Masukkan jumlah barang: ").strip())
            harga_barang = int(input("Masukkan harga barang: ").strip())

            # statement ini untuk mengecek nama_barang yang sama tidak bisa diinput dua kali 
            if nama_barang in dict_barang: 
                print("Barang yang anda masukkan sudah di keranjang: ")
            # statement ini untuk memastikan jumlah_barang dan harga_barang adalah bilangan positif 
            else: 
                if jumlah_barang > 0 and harga_barang > 0: 
                    pass 
                else: 
                    print("Silakan masukkan bilangan positif untuk 'Jumlah Barang' dan 'Harga Barang'.")
                    continue

                # Bila nama barang belum pernah diinput sebelumnya, lalu total barang dan harga barang bernilai positif
                dict_barang[nama_barang] = [jumlah_barang, harga_barang]
            print("==================================================")

            # statement ini digunakan apabila user ingin menambahkan barang lain 
            while True: 
                yn = input("Ingin menambahkan barang lainnya: (y/n)").strip().lower()
                if yn == "y":
                    break 
                elif yn == "n":
                    print("==================================================")
                    print("Barang yang anda pesan berhasil ditambahkan.")
                    print("==================================================")
                    return                 
                else: 
                    print("\nSilakan input y atau n.")
                    continue 

            print("==================================================")
            print("Barang yang anda pesan berhasil ditambahkan.")
            print("==================================================")

            return dict_barang
    
    except: 
        print("\nSilakan masukkan angka ke 'total barang' dan 'harga barang'.\n")

# fungsi 2; Update barang 
def update_barang(): 
    """
    Fungsi ini dibuat untuk update data barang yang sudah dimasukkan kedalam dictionary
    Update yang dilakukan oleh user, tergantung dari pilihan menu yang mereka pilih 
    """

    global dict_barang 

    print("1. Ubah nama barang \n2. Ubah jumlah barang \n3. Ubah harga barang\n ")
    update = int(input("Silakan pilih nomor pada menu diatas: (1/2/3)").strip())

    # berdasarkan pilihan pada menu diatas, kita akan melakukan berapa update 
    # bila user memilih 1 
    if update == 1: 

        # menanyakan kepada user, barang mana yang akan di update 
        update_barang = input("Silakan masukkan nama barang yang akan diubah: ").strip().title() 

        # memastikan nama barang yang dimasukkan oleh user sudah ada didalam dictionary 
        if update_barang in dict_barang.keys():
            updated_barang = input("Silakan masukkan nama barang yang baru: ").strip().title() 

            # update keys
            dict_barang[updated_barang] = dict_barang[update_barang]

            # hapus nama barang lama 
            del dict_barang[update_barang] 
            print("==================================================")
            print("Nama barang berhasil diubah.")
            print("==================================================")
        else: 
            print(f"\nNama barang {update_barang} tidak ditemukan")
    # bila user memilih 2  
    elif update == 2: 

        # menanyakan kepada user, barang mana yang akan di update
        update_jumlah = input("Silakan masukkan nama barang yang jumlahnya akan diubah: ").strip().title() 

        if update_jumlah in dict_barang.keys():
            updated_jumlah = int(input("Masukkan jumlah barang yang baru: ").strip())

            # update jumlah barang
            dict_barang[update_jumlah][0] = updated_jumlah 
            print("==================================================")
            print("Jumlah barang berhasil diubah.")
            print("==================================================")

        else: 
            print(f"\nNama barang {update_jumlah} tidak ditemukan.")

    elif update == 3: 

        # menanyakan kepada user, barang mana yang akan di update
        update_harga = input("Silakan masukkan nama barang yang harganya akan diubah: ").strip().title()

        if update_harga in dict_barang.keys(): 
            updated_harga = int(input("Masukkan harga barang yang baru: ")).strip() 

            # update harga barang 
            dict_barang[update_jumlah][1] = updated_harga 
            print("==================================================")
            print("Harga barang berhasil diubah.")
            print("==================================================")

        else: 
            print(f"\nNama barang {update_harga} tidak ditemukan.")

    else: 
        print("Silakan masukkan nomor sesuai menu diatas.")

    return dict_barang

# fungsi 3; hapus barang 
def delete_barang(): 
    """
    Fungsi ini digunakan untuk menghapus beberapa barang atau
    reset transaksi yang dilakukan 
    """

    global dict_barang 

    print("\n1. Hapus barang \n2. Ulangi transaksi\n")
    delete = int(input("Silakan pilih tipe hapus yang mana: (1/2)"))

    # berdasarkan pilihan pada menu diatas, kita akan melakukan berapa update 
    # bila user memilih 1 
    if delete == 1: 

        # menanyakan kepada user, barang mana yang akan di update
        delete_barang = input("Silakan masukkan nama barang yang ingin dihapus: ").strip().title()

        if delete_barang in dict_barang.keys(): 
            
            del dict_barang[delete_barang]
            print("==================================================")
            print("Barang berhasil dihapus.")
            print("==================================================")

        else: 
            print(f"\nNama barang {delete_barang} tidak ditemukan.")
    
    elif delete == 2:

        dict_barang = {}
        print("==================================================")
        print("Semua barang berhasil dihapus.")
        print("==================================================")
        
    else: 
        print("Silakan masukkan nomor sesuai menu diatas.")

    return dict_barang 

# fungsi 4; chek orderan (keranjang)
def check_order(): 
    """ 
    Fungsi ini dibuat untuk melihat detail order menggunakan tabulate 
    """

    print_dict = {"Nama Barang" : [key for key in dict_barang.keys()],
            "Jumlah Barang": [value[0] for value in dict_barang.values()],
            "Harga Barang": [value[1] for value in dict_barang.values()],
            "Total Harga": [value[0]*value[1] for value in dict_barang.values()]}

    # menghitung jumlah harga yang harus dibayar user
    total = 0
    for key in dict_barang.keys():
        total = total+(dict_barang[key][0]*dict_barang[key][1])

    # print table menggunakan tabulate 
    print("\nOrder Details: \n")
    print(tabulate(print_dict, headers = "keys", tablefmt = "github", colalign = ("center",)))
    print("==================================================")
    print("Total belanja", " "*28, "Rp ", total)
    print("==================================================")

# fungsi 5; total harga
def total_price():
    """
    Fungsi ini digunakan untuk menghitung total harga yang harus user bayar. 
    Total harga bergantung pada beberapa kondisi, salah satunya diskon harga
    Diskon harga ada pada informasi dibawah ini: 
    
    Kondisi:
    -Diskon 5% untuk pembelian diatas Rp 200000
    -Diskon 6% untuk pembelian diatas Rp 300000
    -Diskon 7% untuk pembelian diatas Rp 500000
    """

    # menggunakan loop untuk menghitung total harga yang dipesan
    total = 0
    for key in dict_barang.keys():
        total = total+(dict_barang[key][0]*dict_barang[key][1])

    # menggunakan if statement, untuk melihat kondisi harga untuk mendapatkan diskon
    if total > 200000 and total <=300000:
        diskon = 5
        total = total*(100-diskon)/100
    elif total > 300000 and total <=500000:
        diskon = 8
        total = total*(100-diskon)/100
    elif total > 500000:
        diskon = 10
        total = total*(100-diskon)/100
    else: 
        diskon = 0
        total = total

    #Showing the discount the user get and the total discounted price
    print(f"Anda mendapatkan potongan {diskon}%, jumlah yang harus anda bayar Rp {int(total)}")
    print("==================================================")


# fungsi 6; melihat cart 
def show_cart():
    """
    Fungsi ini diperuntukkan bagi user apabila ingin melihat cart (keranjang)
    Fungsi ini akan dipakai saat user ingin update atau delete barang
    """

    #Adjusting the dictionary using list comprehension so it will fit the tabulate input format
    print_dict = {"Nama Barang" : [key for key in dict_barang.keys()],
            "Jumlah Barang": [value[0] for value in dict_barang.values()],
            "Harga Barang": [value[1] for value in dict_barang.values()]}

    #Printing the table of inputted order using tabulate
    print("\nKeranjang Belanja Anda: \n")
    print(tabulate(print_dict, headers = "keys", tablefmt = "github", colalign = ("center",)))
    print("==================================================")




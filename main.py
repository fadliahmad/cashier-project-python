"""
File ini adalah program utama, memiliki beberapa pilihan menu dan part untuk memanggil fungsi yang sudah dibuat
di dalam cashier_function.py tergantung dari pilihan user
Sebelum menjalankan file ini, pastikan Anda sudang menjalankan file cashier_function
"""

# import fungsi-fungsi dari cashier_function
from cashier_function import input_barang, update_barang, delete_barang, check_order, total_price, show_cart

# mendeklarasikan dictionary kosong, supaya dapat diinput data pembelian kedalamnya, dan dapat diedit nantinya 
dict_barang = {}

print("\n..........Selamat Datang!..........")

# gunakan loop dibawah ini untuk memanggil fungsi sesuai input yang dimasukkan user
while True:
    try:
        # print main menu 
        print("\nMENU UTAMA")
        print("============")
        print("1. Input barang \n2. Ubah barang \n3. Hapus barang \n4. Cek Pesanan Anda \n5. Checkout Pesanan Anda \n6. Keluar\n")
        menu = int(input("Apa yang ingin Anda lakukan? (Masukkan nomor sesuai nomor menu diatas): ").strip())
        print("==================================================")

        # statement if untuk mimilih fungsi yang akan dijalankan sesuai inputan user
        if menu == 1:
            dict_barang = input_barang()

        elif menu == 2:

            # cek apakah sudah ada barang di dictionary atau belum 
            if dict_barang == {}:
                print("\nTidak ada barang untuk diubah")

            # apabila sudah ada barang, kita akan run fungsi update_barang()
            else: 

                # menampilkan chart terlebih dahulu
                show_cart()
                print("")
                dict_barang = update_barang()

        elif menu == 3:

            # cek apakah sudah ada barang di dictionary atau belum
            if dict_barang == {}:
                print("\nTidak ada barang untuk dihapus")

            # apabila sudah ada barang, kita akan run fungsi delete_barang()
            else: 

                # menampilkan chart terlebih dahulu
                show_cart()
                print("")
                dict_barang = delete_barang()

        elif menu == 4:

            # cek apakah sudah ada barang di dictionary atau belum
            if dict_barang == {}:
                print("\nBelum ada pesanan!")

            # apabila sudah ada barang, kita akan run fungsi check_order()
            else: check_order()

        elif menu == 5: 

            # cek apakah sudah ada barang di dictionary atau belum
            if dict_barang == {}:
                print("\nBelum ada pesanan!")

            # apabila sudah ada barang, kita akan run fungsi total_price()
            else: 

                # menampilkan semua daftar belanjaan
                check_order()
                total_price()
                print("Terima kasih sudah berbelanja!\n")
                
                # break dari ketika cek order
                break

        elif menu == 6:

            # break dari main if dan main loop sebelum user check out
            print("\nTerima Kasih sudah berkunjung!\n")
            break 

    # peringatan error ketika inputan bukan 1,2,3,4,5, atau 6
    except:
        print("\nSilakan masukkan nomor sesuai menu diatas! (1/2/3/4/5/6)")


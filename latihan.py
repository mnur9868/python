# import only system from os 
from os import system, name 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
nama = input("Siapa nama anda ? : ")
def ulang():
    clear()
    print("\n\n====== Menu Utama ======\n")
    print("1. Operasi Matematika")
    print("2. Deret Fibonanci")
    print("\nSelamat datang, "+nama+"\n")
    apa = input("Silahkan pilih : ")
    if apa == "1":
        clear()
        def math():
            clear()
            def selesai():
                selesai = input("Apakah ingin melanjutkan ? y/n : ")
                if selesai== "y":
                    math()
                else:
                    print("program berakhir")
                    exit()
            def Operasi(tipe):
                try:
                    x = int(input("Masukan data 1 : "))
                    x2 = input("Masukan data 2 : ")
                    if tipe=="kali":
                        print("Hasil = "+ str(int(x) * int(x2)) +"")
                        selesai()
                    if tipe=="bagi":
                        print("Hasil = "+ str(int(x) / int(x2)) +"")
                        selesai()
                    if tipe=="tambah":
                        print("Hasil = "+ str(int(x) + int(x2)) +"")
                        selesai()
                    if tipe=="kurang":
                        print("Hasil = "+ str(int(x) - int(x2)) +"")
                        selesai()
                except ValueError as ve:
                    print("Error: tipe data selain integer tdk dapat diproses !")
                    Operasi(tipe)
            print("\n\n====== OPERASI MATEMATIKA ======\n")
            print("Operasi apa yang akan anda lakukan ? \n 1. Perkalian \n 2. Pembagian \n 3. Pertambahan \n 4. Pengurangan \n 5. Kembali")
            y = input("Silahkan pilih : ")
            if y == "1":
                clear()
                print("\n\n====== Perkalian ======\n")
                Operasi("kali")
            if y == "2":
                clear()
                print("\n\n====== Pembagian ======\n")
                Operasi("bagi")
            if y == "3":
                clear()
                print("\n\n====== Pertambahan ======\n")
                Operasi("tambah")
            if y == "4":
                clear()
                print("\n\n====== Pengurangan ======\n")
                Operasi("kurang")
            if y == "5":
                ulang()
                clear()
            else:
                print("Pilihan tidak tersedia")
                input("Tekan apapun untuk melanjutkan ...")
                math()
        math()
    if apa == '2':
        clear()
        def fibonanci():
            try:
                clear()
                def selesai():
                    selesai = input("Apakah ingin melanjutkan ? y/n : ")
                    if selesai== "y":
                        fibonanci()
                    else:
                        print("program berakhir")
                        exit()
                print("\n\n====== Deret Fibonanci ======\n")
                a = int(input("Silahkan masukan angka ke-1 :"))
                b = int(input("Silahkan masukan angka ke-2 :"))
                n = int(input("Silahkan masukan angka ke-n :"))
                while a <= n:
                    print(a,end = ' ')
                    a,b=b, a+b
                    print()
                selesai()
            except ValueError as e:
                print("Error: tipe data selain integer tdk dapat diproses !")
                input("Tekan apapun untuk melanjutkan ...")
                fibonanci()
        fibonanci()
    else:
        
        print("Pilihan tidak tersedia\n")
        input("Tekan apapun untuk melanjutkan ...")
        ulang()
ulang()
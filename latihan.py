# import only system from os 
from os import system, name 
# clear screen
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
nama = input("Siapa nama anda ? : ")


# awal
def awal():
    
    
    # menu utama
    clear()
    print("\n\n====== Menu Utama ======\n")
    print("1. Operasi Matematika")
    print("2. Deret Fibonanci")
    print("\nSelamat datang, "+nama+"\n")
    
    
    # input pilihan
    apa = input("Silahkan pilih : ")
    if apa == "1":
        
        
        # Operasi Matematika
        clear()
        def math():
            clear()
            
            
            # Operasi selesai
            def selesai():
                selesai = input("Apakah ingin melanjutkan ? y/n : ")
                if selesai== "y":
                    math()
                else:
                    print("program berakhir")
                    exit()
            
            
            # Operasi inti
            def Operasi(tipe):
                
                
                # try catch value error non integer
                try:
                    
                    # masukan data1
                    x = int(input("Masukan data 1 : "))
                    
                    
                    # masukan data2
                    x2 = input("Masukan data 2 : ")
                    
                    
                    # operasi perkalian
                    if tipe=="kali":
                        print("Hasil = "+ str(int(x) * int(x2)) +"")
                        selesai()
                        
                        
                    # operasi Pembagian
                    if tipe=="bagi":
                        print("Hasil = "+ str(int(x) / int(x2)) +"")
                        selesai()
                        
                        
                    # operasi Pertambahan
                    if tipe=="tambah":
                        print("Hasil = "+ str(int(x) + int(x2)) +"")
                        selesai()
                        
                        
                    # operasi Pengurangan
                    if tipe=="kurang":
                        print("Hasil = "+ str(int(x) - int(x2)) +"")
                        selesai()
                
                
                # catch value error dan mengulangi operasi
                except ValueError as ve:
                    print("Error: tipe data selain integer tdk dapat diproses !")
                    Operasi(tipe)
                    
                    
            # menu Operasi Matematika
            print("\n\n====== OPERASI MATEMATIKA ======\n")
            print("Operasi apa yang akan anda lakukan ? \n 1. Perkalian \n 2. Pembagian \n 3. Pertambahan \n 4. Pengurangan \n 5. Kembali")
            y = input("Silahkan pilih : ")
            if y == "1":
                
                
                # Perkalian
                clear()
                print("\n\n====== Perkalian ======\n")
                Operasi("kali")
            if y == "2":
                
                
                # Pembagian
                clear()
                print("\n\n====== Pembagian ======\n")
                Operasi("bagi")
            if y == "3":
                
                
                # Pertambahan
                clear()
                print("\n\n====== Pertambahan ======\n")
                Operasi("tambah")
            if y == "4":
                
                
                # Pengurangan
                clear()
                print("\n\n====== Pengurangan ======\n")
                Operasi("kurang")
            if y == "5":
                
                
                # kembali ke menu utama
                awal()
                clear()
            else:
                
                
                # pilihan tdk tersedia
                print("Pilihan tidak tersedia")
                input("Tekan apapun untuk melanjutkan ...")
                math()
        math()
    if apa == '2':
        
        
        # deret fibonanci
        clear()
        def fibonanci():
            
            
            # try catch ValueError non jnteger
            try:
                clear()
                
                
                # Operasi selesai
                def selesai():
                    selesai = input("Apakah ingin melanjutkan ? y/n : ")
                    if selesai== "y":
                        fibonanci()
                    else:
                        print("program berakhir")
                        exit()
                        
                
                
                print("\n\n====== Deret Fibonanci ======\n")
                
                
                # masukan angka ke-1
                a = int(input("Silahkan masukan angka ke-1 :"))
                
                
                # masukan angka ke-2
                b = int(input("Silahkan masukan angka ke-2 :"))
                
                
                # masukan angka ke-n
                n = int(input("Silahkan masukan angka ke-n :"))
                
                
                # pengulangan dari a sampai angka ke-n dan n = a + b
                while a <= n:
                    
                    
                    # cetak hasil pengulangan deret
                    print(a,end = ' ')
                    a,b=b, a+b
                    print()
                selesai()
                
            
            # catch ValueError non integer
            except ValueError as e:
                print("Error: tipe data selain integer tdk dapat diproses !")
                input("Tekan apapun untuk melanjutkan ...")
                fibonanci()
        fibonanci()
    else:
        
        
        # pilihan tdk tersedia
        print("Pilihan tidak tersedia\n")
        input("Tekan apapun untuk melanjutkan ...")
        awal()
awal()
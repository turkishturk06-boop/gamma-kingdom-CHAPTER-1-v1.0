from core import ekran_temizle

def library():
    while True:
        ekran_temizle()
        khninput = input("""Büyük Kütüphane'ye vardın hangi kitabı okuyacaksın ?
            1) Delta'nın Yükselişi
            2) Krallığın Yıkılışı
            3) Çürüme
            4) Huzur
            5) Denge
            6) Neon Yükselişi
            7) Şehir Kovalaması
            8) Yeraltı
            9) Dengenin Tekrar Bozulması
            10) Büyük Kütühane
            11) Küllere Parçalanma
            12) İntikam
            13) 3 Son
            14) Çıkış
            Seçimin: 
            """)
        if khninput == "1":
            ekran_temizle()
            ksinput = input("""             
                /..\                           (Çıkmak için entere basın)                                              
                                                   Deltanın Yükselişi:
                Uzun Zaman Önce Gamma Dünyayı yönetiyordu ama heryerde kaos vardı ve dünyanın 7 yanından bir kuvvet birleşti 
                adı ise Delta'ydı. Delta Uzun süre Dünyayı Huzurla Yönetti taki bir Kahraman Gelene Kadar...""")
            if ksinput == "":
                ekran_temizle()
                continue
        elif khninput == "14":
            ekran_temizle()
            break
        else:
            ekran_temizle()
            print("Bu Kitaba kimse hazır değil...")
            continue
kitaplar = [{'Kitap Adı': 'VADİDEKİ ZAMBAK', 'Yazar': 'HONORE DE BALZAC', 'Yayın Tarihi': '1835', 'Sayfa Sayısı': 328},
            {'Kitap Adı': 'ANNA KARENİNA', 'Yazar': 'TOLSTOY', 'Yayın Tarihi': 1878, 'Sayfa Sayısı': 1072}]

  
with open("bilgiler.txt", 'a',encoding="utf-8") as dosya:
  for i in kitaplar:
    dosya.write(f"Kitap Adı:{i['Kitap Adı']}, Yazar:{i['Yazar']}, Yayın Tarihi:{i['Yayın Tarihi']}, Sayfa Sayısı:{i['Sayfa Sayısı']}\n")
    dosya.close
          

class library:
    def __init__(self, kitap_adi, yazar, yayin_tarihi, sayfa_sayisi):
        self.kitap_adi = kitap_adi
        self.yazar = yazar  
        self.yayin_tarihi = yayin_tarihi
        self.sayfa_sayisi = sayfa_sayisi
        kitaplar.append({
            'Kitap Adı': kitap_adi,
            'Yazar': yazar,
            'Yayın Tarihi': yayin_tarihi,
            'Sayfa Sayısı': sayfa_sayisi})
        with open("bilgiler.txt", "a",encoding="utf-8") as dosya:
            dosya.write(f"Kitap Adı:{kitap_adi}, Yazar:{yazar}, Yayın Tarihi:{yayin_tarihi}, Sayfa Sayısı:{sayfa_sayisi}\n")
            dosya.close()
while True:
    print("******  Menü  ******")
    print("1-Kitap Ekle")
    print("2-Kitap Listesini Göster")
    print("3-Kitap Sil")
    print("4-Menüden Çıkış")
    a = int(input("İşlem Numarası Seçiniz:")) 
  
    if a == 1:
        kitap_adi = input("Kitap Adı: ").upper()
        yazar = input("Yazar: ").upper()
        yayin_tarihi = input("Yayınlanma Tarihi: ")
        sayfa_sayisi = input("Sayfa Sayısı: ")
        library(kitap_adi, yazar, yayin_tarihi, sayfa_sayisi)
        print("\n""Ekleme İşlem Başarılı""\n")
    elif a == 2:
        print("\n ****** Kitap Listesi ******")
        for i in kitaplar:
            
            print("Kitap Adı:", i["Kitap Adı"], ",", "Yazar:", i["Yazar"])
        print("\n")
    elif a == 3:
        silinecek_kitap = input("Silmek istediğiniz kitabın adını giriniz: ").upper()
        silinecek_yazar =input("Silmek istediğiniz kitabın yazarının adını giriniz: ").upper()
        gecici_liste = []

        for i in kitaplar:
            if i['Kitap Adı'] != silinecek_kitap or i['Yazar'] != silinecek_yazar:
                gecici_liste.append(i)
                
        if len(gecici_liste) == len(kitaplar):
            print("\n""Kitap bulunamadı.""\n")
        else:
            kitaplar = gecici_liste
            print("\n""Silme İşlemi Başarılı""\n")
            with open("bilgiler.txt", 'w',encoding="utf-8") as dosya:
                    for i in kitaplar:
                        dosya.write(f"Kitap Adı:{i['Kitap Adı']}, Yazar:{i['Yazar']}, Yayın Tarihi:{i['Yayın Tarihi']}, Sayfa Sayısı:{i['Sayfa Sayısı']}\n")
                        dosya.close

    elif a == 4:
      print("\n""Program Sonlandırıldı..""\n")
      break
    else:
        print("\n""Hatalı Seçim""\n")
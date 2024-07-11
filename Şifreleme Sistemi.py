from tkinter import *
import random
import string

# Kullanıcı bilgileri ve hoş geldin mesajları
bilgiler = {
    "ibrahim": "1234",
    "ayse": "5678",
    "mehmet": "abcd",
    "fatma": "efgh",
    "ali": "ijkl"
}
denemeHakki = 3
hosgeldin_mesajlari = {
    "ibrahim": "İbrahim Bey, hoşgeldiniz!",
    "ayse": "Ayşe Hanım, hoşgeldiniz!",
    "mehmet": "Mehmet Bey, hoşgeldiniz!",
    "fatma": "Fatma Hanım, hoşgeldiniz!",
    "ali": "Ali Bey, hoşgeldiniz!"
}

# Giriş yapma fonksiyonu
def girisYap(event=None):
    global denemeHakki
    if denemeHakki <= 0:
        pencere.destroy()
        return False

    kAdi = ad.get()
    parola = sifre.get()
    print(kAdi, "-", parola)
    print("Kontrol Ediliyor")

    if kAdi in bilgiler and bilgiler[kAdi] == parola:
        print("Girişiniz Onaylandı...")
        hosgeldin_mesaj = hosgeldin_mesajlari.get(kAdi, "Hoşgeldiniz!")
        sonuc.config(text=f"{hosgeldin_mesaj}")
        EkraniTemizle()
        if kAdi == "ibrahim":
            AdminEkraniOlustur()
        else:
            GirisEkraniOlustur()
    else:
        print("Bilgiler Yanlış")
        denemeHakki -= 1
        sonuc.config(text=f"Bilgiler Yanlış! Kalan Deneme : {denemeHakki}")
        ad.delete(0, END)  # Kullanıcı adı alanını temizler
        sifre.delete(0, END)  # Şifre alanını temizler
        ad.focus_set()  # Kullanıcı adı alanına odaklanır

        if denemeHakki <= 0:
            sonuc.config(text="Deneme hakkı bitti! 3 saniye sonra çıkış yapılacak.")
            pencere.after(3000, pencere.destroy)  # 3 saniye sonra pencereyi kapat

# Yönetici ekranını temizleme fonksiyonu
def EkraniTemizle():
    karsilama.config(text="İbrahim Bey, Sistemimize Hoşgeldiniz...")
    adsor.destroy()
    ad.destroy()
    sifresor.destroy()
    sifre.destroy()
    btn.destroy()

# Kullanıcı ekleme fonksiyonu
def KullaniciEkle(event=None):
    yeni_ad = ad_entry.get()
    yeni_sifre = sifre_entry.get()
    if yeni_ad and yeni_sifre:
        bilgiler[yeni_ad] = yeni_sifre
        hosgeldin_mesajlari[yeni_ad] = f"{yeni_ad.capitalize()} Bey/Hanım, hoşgeldiniz!"
        sonuc.config(text=f"{yeni_ad} başarıyla eklendi.")
    else:
        sonuc.config(text="Kullanıcı adı ve şifre boş olamaz.")

# Kullanıcı silme fonksiyonu
def KullaniciSil(event=None):
    silinecek_ad = ad_entry.get()
    if silinecek_ad in bilgiler:
        del bilgiler[silinecek_ad]
        del hosgeldin_mesajlari[silinecek_ad]
        sonuc.config(text=f"{silinecek_ad} başarıyla silindi.")
    else:
        sonuc.config(text=f"{silinecek_ad} bulunamadı.")

# Kullanıcı güncelleme fonksiyonu
def KullaniciGuncelle(event=None):
    guncellenecek_ad = ad_entry.get()
    yeni_sifre = sifre_entry.get()
    if guncellenecek_ad in bilgiler:
        bilgiler[guncellenecek_ad] = yeni_sifre
        sonuc.config(text=f"{guncellenecek_ad} başarıyla güncellendi.")
    else:
        sonuc.config(text=f"{guncellenecek_ad} bulunamadı.")

# Yönetici ekranı oluşturma fonksiyonu
def AdminEkraniOlustur():
    global ad_entry, sifre_entry, ekle_btn, sil_btn, guncelle_btn, sonuc, cikis_btn

    ad_label = Label(pencere, text="Kullanıcı Adı:")
    ad_label.pack()

    ad_entry = Entry(pencere)
    ad_entry.pack()
    ad_entry.bind('<Return>', lambda event: sifre_entry.focus_set())  # Kullanıcı adı girildiğinde "Enter" tuşuna basıldığında şifre alanına odaklanır

    sifre_label = Label(pencere, text="Şifre:")
    sifre_label.pack()

    sifre_entry = Entry(pencere)
    sifre_entry.pack()
    sifre_entry.bind('<Return>', lambda event: islemYap())  # Şifre girildiğinde "Enter" tuşuna basıldığında işlem yapılır

    ekle_btn = Button(pencere, text="Kullanıcı Ekle", command=KullaniciEkle)
    ekle_btn.pack()

    sil_btn = Button(pencere, text="Kullanıcı Sil", command=KullaniciSil)
    sil_btn.pack()

    guncelle_btn = Button(pencere, text="Kullanıcı Güncelle", command=KullaniciGuncelle)
    guncelle_btn.pack()

    cikis_btn = Button(pencere, text="Geri Dön", command=GeriDön)
    cikis_btn.pack()

    sonuc = Label(pencere, text="Henüz işlem yapılmadı")
    sonuc.pack()

def islemYap():
    if pencere.focus_get() == ad_entry:
        sifre_entry.focus_set()
    elif pencere.focus_get() == sifre_entry:
        if ekle_btn.focus_get():
            KullaniciEkle()
        elif sil_btn.focus_get():
            KullaniciSil()
        elif guncelle_btn.focus_get():
            KullaniciGuncelle()

# Giriş ekranı oluşturma fonksiyonu
def GirisEkraniOlustur():
    global cikis_btn
    cikis_btn = Button(pencere, text="Geri Dön", command=GeriDön)
    cikis_btn.pack()
    pencere.bind('<Control-r>', lambda event: GeriDön())

# Ana giriş ekranı oluşturma fonksiyonu
def GeriDön(event=None):
    for widget in pencere.winfo_children():
        widget.destroy()
    AnaGirisEkrani()

# Ana giriş ekranı oluşturma fonksiyonu
def AnaGirisEkrani():
    global karsilama, adsor, ad, sifresor, sifre, btn, sonuc
    karsilama = Label(pencere, text="Hoşgeldiniz, Lütfen Bilgilerinizi Giriniz...")
    karsilama.pack()

    adsor = Label(pencere, text="Kullanıcı Adı : ")
    adsor.pack()

    ad = Entry(pencere)
    ad.pack()
    ad.focus_set()
    ad.bind('<Return>', lambda event: sifre.focus_set())

    sifresor = Label(pencere, text="Şifre : ")
    sifresor.pack()

    sifre = Entry(pencere)
    sifre.pack()
    sifre.bind('<Return>', girisYap)

    btn = Button(pencere, text="Giriş Yap!", command=girisYap)
    btn.pack()

    sonuc = Label(pencere, text="Henüz Giriş Yapılmadı")
    sonuc.pack()

    pencere.bind('<Control-q>', lambda event: pencere.destroy())

pencere = Tk()
pencere.title("Giriş Ekranı")
pencere.geometry("400x400+100+100")

AnaGirisEkrani()  # Giriş ekranını başlatmak için

mainloop()

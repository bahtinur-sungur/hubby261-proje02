from tkinter import *
import tkinter as tk
import time
from dataURL import DataURL
from getURL import GetURL

pencere = tk.Tk()
pencere.title("Ana Pencere")
pencere.geometry("600x400")
pencere.configure(bg="purple")

def urlListele():
    pencere2 = Tk()
    pencere2.title("URL Listele")
    pencere2.geometry("600x400")
    with open("dataUrl.txt") as f:
        liste = f.read()
    etiket = Label(pencere2, text=liste, bg="light blue", fg="dark blue", font=("Arial", 12))
    etiket.pack()
    buton2 = Button(pencere2, text= "Kapat", fg="purple", bg="light grey", command=pencere2.destroy)
    buton2.config(font=("Arial", 8))
    buton2.pack()

def urlEkle():
    pencere3 = Tk()
    pencere3.title("URL Ekle")
    pencere3.geometry("600x400")
    etiket = Label(pencere3)
    etiket.pack()
    etiket2 = Label(pencere3, text="URL giriniz", bg="light blue", fg="dark blue", font=("Arial", 12))
    etiket2.pack()
    url = Entry(pencere3, width=25, borderwidth=1)
    url.pack()
    buton3 = Button(pencere3, text="Kaydet", fg="purple", bg="light grey", command=pencere3.destroy)
    buton3.config(font=("Arial", 8))
    buton3.pack()

def orumcekGoner():
    pencere4 = Tk()
    pencere4.title("Örümcek  Gönder")
    pencere4.geometry("600x400")
    with open("getURL.py") as f:
        liste = f.read()
    etiket = Label(pencere4, text=liste, bg="light blue", fg="dark blue", font=("Arial", 12))
    etiket.pack()
    buton4 = Button(pencere4, text="Kapat", fg="purple", bg="light grey", command=pencere4.destroy)
    buton4.config(font=("Arial", 8))
    buton4.pack()

def sonucListele():
    pencere5 = Tk()
    pencere5.title("Sonuçları Listele")
    pencere5.geometry("600x400")
    with open("getURL.txt") as f:
        liste = f.read()
    etiket = Label(pencere5, text=liste, bg="light blue", fg="dark blue", font=("Arial", 12))
    etiket.pack()
    buton5 = Button(pencere5, text="Kapat", fg="purple", bg="light grey", command=pencere5.destroy)
    buton5.config(font=("Arial", 8))
    buton5.pack()

def cikis():
    pencere6 = Tk()
    pencere6.title("Çıkış")
    pencere6.geometry("600x400")
    buton6 = Button(pencere6, text="Kapat", fg="purple", bg="light grey", command=pencere6.destroy)
    buton6.config(font=("Arial", 8))
    buton6.pack()

etiket = Label(pencere, text="---MİNİ ÖRÜMCEĞE HOŞ GELDİNİZ---", bg="pink", fg="purple", font=("Arial", 24))
etiket2 = Label(pencere, text="!!Lütfen yapmak istediğiniz işlemi seçiniz!!", bg="light blue", fg="dark blue", font=("Arial", 18))
etiket3 = Label(pencere, text="Menü",bg="light grey", fg="purple")
etiket3.config(font=("Arial", 20))

etiket.pack()
etiket2.pack()
etiket3.pack()

butonA = Button(pencere, text= "0) URL Lİstele", fg="purple", bg="light grey", command=urlListele)
butonA.config(font=("Arial", 16))
butonA.pack()

butonB = Button(pencere, text= "1) URL Ekle", fg="purple", bg="light grey", command=urlEkle)
butonB.config(font=("Arial", 16))
butonB.pack()

butonC = Button(pencere, text= "2) Örümcek Gönder", fg="purple", bg="light grey", command=orumcekGoner)
butonC.config(font=("Arial", 16))
butonC.pack()

butonD = Button(pencere, text= "3) Sonuçları Listele", fg="purple", bg="light grey", command=sonucListele)
butonD.config(font=("Arial", 16))
butonD.pack()

butonE = Button(pencere, text= "4) Çıkış", fg="purple", bg="light grey", command=cikis)
butonE.config(font=("Arial", 16))
butonE.pack()

pencere.mainloop()

useDataURL = DataURL()
useGetURL = GetURL()

while True:
    menuSecim = (input("Seçiminiz: "))
    if menuSecim.isdigit():
        menuSecim = int(menuSecim)
        if menuSecim == 0:
            print("Mini örümcek kapatılıyor...")
            time.sleep(1)
            break
        elif menuSecim == 1:
            useDataURL.dataRead()
        elif menuSecim == 2:
            useDataURL.dataWrite()
        elif menuSecim == 3:
            useGetURL.getWeb()
        elif menuSecim == 4:
            useGetURL.getList()

    else:
        print("Lütfen seçiminizi 0 ile 4 arasında tercih ediniz")
        print("Menüye yönlendiriliyorsunuz.Lütfen bekleyiniz")
        time.sleep(2)

import os
from tkinter import*
from tkinter import messagebox
from datetime import*
import locale
from random import *
from pandas import *
from tkcalendar import DateEntry
from openpyxl.workbook import Workbook


def uyg():
    ekran2.destroy()
    ekran.destroy()
    global master
    master = Tk()
    master.geometry('1200x650')
    master.title('Bilgi Giris Ekranı')
    canvas = Canvas(master, height=500,width=400)
    canvas.pack
    frame_ust = Frame(master,bg='#add8e6')
    frame_ust.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.1)
    global frame_alt
    frame_alt =Frame(master,bg='#add8e6')
    frame_alt.place(relx=0.1,rely=0.21,relheight=0.8,relwidth=0.8)
    takvim=Label(frame_ust,bg='#add8e6',text ="Takvim:",font="Verdana 12 bold")
    takvim.pack(padx=10,pady=10,side=LEFT)

    tarih=StringVar(frame_ust)
    tarih.set("\t")

    tarih_acilir_menu=OptionMenu(
        frame_ust,
        tarih,
        "Ayın birinci haftası",
        "Ayın ikinci haftası",
        "Ayın üçüncü haftası",
        "Ayın dördüncü haftası"
    )
    tarih_acilir_menu.pack(padx=10,pady=10,side=RIGHT)
    tarih_secici=DateEntry(frame_ust,width=12,background='orange',foreground='black',borderwidth=1,locale="tr_TR")
    tarih_secici._top_cal.overrideredirect(False)
    tarih_secici.pack(padx=10,pady=10,side=LEFT)

    tarih_secici_etiket=Label(frame_ust,bg='#add8e6',text="Planlanacak hafta:",font="Verdana 12 bold")
    tarih_secici_etiket.pack(padx=10,pady=10,side=RIGHT)

    Label(frame_alt, text="Öğrenim Düzeyinizi Seçiniz: ",bg='white', font=("Verdana 10 bold")).pack()
    options1 = ["İlkokul", "Ortaokul", "Lise"]
    global clicked
    clicked = StringVar(frame_alt)
    clicked.set(options1[0])
    drop = OptionMenu(frame_alt, clicked, *options1)
    drop.pack(anchor=CENTER)
    drop.config(height=1,width=7)
    Label(frame_alt, text="Okuldan Çıkış Saatiniz: ",bg='white', font=("Verdana 10 bold")).pack()
    global cikis
    cikis = StringVar(frame_alt)
    saat = Entry(frame_alt, textvariable=cikis)
    saat.pack()
    myButton = Button(frame_alt, text="Seç", command=sinifsec)
    myButton.pack(anchor=CENTER)
    myButton.config(height=1,width=5)


def sinifsec():
    saathesapla()
    Label(frame_alt, text="Sınıfınızı seçiniz: ",bg='white', font=("Verdana 10 bold")).pack(anchor=CENTER)
    if clicked.get()=="İlkokul":
        options = ["1", "2", "3", "4"]
        global c1
        c1 = StringVar(frame_alt)
        c1.set(options[0])
        drop = OptionMenu(frame_alt, c1, *options)
        drop.pack(anchor=CENTER)
        drop.config(height=1,width=5)
        global p
        p=IntVar(frame_alt)
        global sec
        sec = IntVar(frame_alt)
        c1 = Checkbutton(frame_alt, text="Kitap önerisi", variable=sec, onvalue=1, offvalue=0, command=kitap)
        c1.pack(anchor=CENTER)
        myButton = Button(frame_alt, text="Seç", command=derseklebuton,height=1,width=5)
        myButton.pack(anchor=CENTER)

    elif clicked.get()=="Ortaokul":
        options = ["5", "6", "7", "8"]
        global c2
        c2 = StringVar(frame_alt)
        c2.set(options[0])
        drop = OptionMenu(frame_alt, c2, *options)
        drop.pack(anchor=CENTER)
        p = IntVar(frame_alt)
        proje = Checkbutton(frame_alt, text="Proje ödevim var", variable=p, onvalue=1, offvalue=0)
        proje.pack(anchor=CENTER)
        sec = IntVar(frame_alt)
        c1 = Checkbutton(frame_alt, text="Kitap önerisi", variable=sec, onvalue=1, offvalue=0, command=kitap)
        c1.pack(anchor=CENTER)
        myButton = Button(frame_alt, text="Seç", command=derseklebuton)
        myButton.pack(anchor=CENTER)

    elif clicked.get()=="Lise":
        options = ["9", "10", "11", "12"]
        global c3
        c3 = StringVar(frame_alt)
        c3.set(options[0])
        drop = OptionMenu(frame_alt, c3, *options)
        drop.pack(anchor=CENTER)
        p = IntVar(frame_alt)
        proje = Checkbutton(frame_alt, text="Proje ödevim var", variable=p, onvalue=1, offvalue=0)
        proje.pack(anchor=CENTER)
        sec = IntVar(frame_alt)
        c1 = Checkbutton(frame_alt, text="Kitap önerisi", variable=sec, onvalue=1, offvalue=0, command=kitap)
        c1.pack(anchor=CENTER)
        myButton = Button(frame_alt, text="Seç", command=derseklebuton)
        myButton.pack(anchor=CENTER)


def saathesapla():
    cikissaati = str(cikis.get())
    global asilsaatliste
    asilsaatliste = []

    (h, m) = cikissaati.split(":")
    sum = timedelta()
    d = timedelta(hours=int(h),minutes=int(m))
    sum = d + timedelta(hours=1, minutes=30)
    saatliste = [str(sum)]
    global bolumsayi
    bolumsayi = 0
    ders = 0
    ara = 0
    if clicked.get()=="İlkokul":
        bolumsayi=3
        ders = 20
        ara = 20
    elif clicked.get()=="Ortaokul":
        bolumsayi=4
        ders = 30
        ara = 15
    elif clicked.get()=="Lise":
        bolumsayi=5
        ders = 40
        ara = 10

    sum+=timedelta(minutes=ders)
    saatliste.append(str(sum))
    for i in range(bolumsayi-1):
        sum += timedelta(minutes=ara)
        saatliste.append(str(sum))
        sum+=timedelta(minutes=ders)
        saatliste.append(str(sum))

    '''sum+=timedelta(minutes=ders)
    saatliste.append(str(sum))'''
    for j in range(0,len(saatliste),2):
        asilsaatliste.append(saatliste[j]+" - "+saatliste[j+1])


def derseklebuton():
    global e
    global e2
    global ders
    ders = StringVar(frame_alt)
    l1 = Label(frame_alt, text="Ders Adı",bg='white', font=("Verdana 10 bold"))
    l1.pack(anchor=CENTER)
    e = Entry(frame_alt, textvariable=ders)
    e.pack(anchor=CENTER)

    l2 = Label(frame_alt, text="Ağırlık",bg='white', font=("Verdana 10 bold"))
    l2.pack(anchor=CENTER)

    global agirlik
    agirlik = StringVar(frame_alt)
    e2 = Entry(frame_alt, textvariable=agirlik)
    e2.pack(anchor=CENTER)

    b1 = Button(frame_alt, text="Ekle", command=ekle)
    b1.pack(anchor=CENTER)

    b2 = Button(frame_alt, text="Tamamla", command=bitir)
    b2.pack(anchor=CENTER)
    if sec==1:
        kitap()


global l
l = []
global a
a = []


def ekle():
    l.append(ders.get().capitalize())
    a.append(int(agirlik.get()))
    e.delete(0,END)
    e2.delete(0,END)


def bitir():
    wb = Workbook
    writer = ExcelWriter("dersprog.xlsx")
    agirlikliliste = []
    asilliste = [[], [], [], [],[]]
    for i in range(len(l)):
        for j in range(a[i]):
            agirlikliliste.append(l[i])

    for k in range(0,5):
        for t in range(0,len(asilsaatliste)):
            rast = randrange(0,len(agirlikliliste))
            asilliste[k].append(agirlikliliste[rast])

    if p.get()==1:
        asilliste[1][2] = "Proje Çalışması"
        asilliste[3][2] = "Proje Çalışması"

    elif p.get()==0:
        pass

    dersProg = DataFrame(asilliste,
                         index=["Pazartesi", "Salı", "Çarşamba", "Persembe", "Cuma"],
                         columns=asilsaatliste,
                         )

    dersProg.to_excel(writer, sheet_name="Haftaici")

    for column in dersProg:
        column_width = max(dersProg[column].astype(str).map(len).max(),len(column))
        col_idx = dersProg.columns.get_loc(column)
        writer.sheets["Haftaici"].set_column(col_idx,col_idx,column_width)

    x = len(asilsaatliste)
    writer.sheets["Haftaici"].set_column(x,x,20)

    #---------------- sheet2 ->

    asilliste2=[[],[]]
    saatliste = []

    if clicked.get()=="İlkokul":
        saatliste = ["12:00:00 - 12:20:00", "13:00:00 - 13:20:00", "16:00:00 - 16:20:00", "17:00:00 - 17:20:00"]

    elif clicked.get()=="Ortaokul":
        saatliste = ["11:30:00 - 12:00:00", "12:30:00 - 13:00:00", "15:00:00 - 15:30:00", "16:00:00 - 16:30:00", "19:00:00 - 19:30:00",
                     "20:00:00 - 20:30:00"]

    elif clicked.get()=="Lise":
        saatliste = ["11:00:00 - 11:40:00", "12:00:00 - 12:40:00", "13:00:00 - 13:40:00", "15:00:00 - 15:40:00", "19:00:00 - 19:40:00",
                     "20:00:00 - 20:40:00"]

    for k in range(0,2):
        for t in range(0,len(saatliste)):
            rast = randrange(0,len(agirlikliliste))
            asilliste2[k].append(agirlikliliste[rast])

    if p.get()==1:
        asilliste2[0][3] = "Proje Çalışması"
        if clicked.get()=="Ortaokul":
            saatliste[3]="16:00:00 - 17:00:00"
        elif clicked.get()=="Lise":
            saatliste[3]="15:00:00 - 16:30:00"

    if clicked.get()=="Ortaokul" and int(c2.get())==8:
        saatliste = ["11:30:00 - 12:00:00", "12:30:00 - 13:45:00", "14:15:00 - 15:35:00", "18:00:00 - 18:30:00",
            "19:00:00 - 19:30:00", "20:00:00 - 20:30:00"]
        asilliste2[1][1]="Sözel Deneme"
        asilliste2[1][2]="Sayısal Deneme"

    if clicked.get()=="Lise" and int(c3.get())==12:
        saatliste = ["11:00:00 - 11:40:00", "12:00:00 - 14:15:00", "14:45:00 - 17:45:00", "19:00:00 - 19:40:00","20:00:00 - 20:40:00",
         "21:00:00 - 21:40:00"]
        asilliste2[1][1] = "TYT Deneme"
        asilliste2[1][2] = "AYT Deneme"

    dersProg2 = DataFrame(asilliste2,
                         index=["Cumartesi","Pazar"],
                         columns=saatliste,
                         )

    dersProg2.to_excel(writer, sheet_name="Haftasonu")

    for column2 in dersProg2:
        column_width2 = max(dersProg2[column2].astype(str).map(len).max(),len(column2))
        col_idx2 = dersProg2.columns.get_loc(column2)
        writer.sheets["Haftasonu"].set_column(col_idx2,col_idx2,column_width2)

    x = len(saatliste)
    writer.sheets["Haftasonu"].set_column(x, x, 20)

    writer.save()

    messagebox.showinfo("Başarılı", "Ders programı oluşturuldu")
    file = "dersprog.xlsx"
    os.startfile(file)
    master.destroy()


def kitap():
    if clicked.get()=="İlkokul":
        sayi = randint(0, 30)
        file = open("ilkokul.txt", "r")
        content = file.readlines()

    elif clicked.get()=="Ortaokul":
        sayi=randint(0,64)
        file = open("ortaokul.txt", "r")
        content=file.readlines()

    elif clicked.get()=="Lise":
        sayi=randint(0,52)
        file = open("lise.txt", "r")
        content = file.readlines()

    l1 = Label(frame_alt, text=content[sayi], font=("Arial",15)).pack()


def yaz():
    ka = ad.get()
    s = sifre.get()

    dosya = open("kullanicilar.txt", "a")
    dosya.write(ka)
    dosya.write(" ")
    dosya.write(s)
    dosya.write("\n")
    dosya.close()

    k1.delete(0,END)
    k2.delete(0, END)
    m1 = messagebox.showinfo("Kayıt işlemi", "Kayıt işlemi başarılı")
    ekran1.destroy()


def girisyap():
    global ekran2
    ekran2 = Toplevel(ekran)
    ekran2.title("GİRİŞ YAP")
    ekran2.geometry("300x250")

    Label(ekran2, text="Bilgilerinizi Giriniz: ").pack()
    Label(ekran2, text="").pack()

    global kullaniciadigiris
    global sifregiris

    kullaniciadigiris = StringVar()
    sifregiris = StringVar()

    global kull1
    global sifre1

    Label(ekran2, text="Kullanıcı Adı: ").pack()
    kullaniciadigiris1 = Entry(ekran2, textvariable=kullaniciadigiris)
    kullaniciadigiris1.pack()
    Label(ekran2, text="Şifre: ").pack()
    sifregiris1 = Entry(ekran2, textvariable=sifregiris, show="*")
    sifregiris1.pack()
    Button(ekran2, text="GİRİŞ", width=10, height=1, command=girisonayla).pack()


def girisonayla():
    kull1 = kullaniciadigiris.get()
    sifre1 = sifregiris.get()

    dosya = open("kullanicilar.txt", "r")
    onay = dosya.read().splitlines()
    tam = kull1+" "+sifre1
    if tam in onay:
        uyg()
    else:
        messagebox.showerror("Giriş Hatası", "Kullanıcı adı ya da şifre yanlış")
        girisyap()


def kayitol():
    global ekran1
    ekran1=Toplevel(ekran)
    ekran1.title("KAYIT OL")
    ekran1.geometry("300x250")

    global ad
    global sifre
    global k1
    global k2
    ad = StringVar()
    sifre = StringVar()

    Label(ekran1, text="Bilgilerinizi giriniz: ").pack()
    Label(ekran1, text="").pack()
    Label(ekran1, text="Kullanıcı adı: ").pack()
    k1 = Entry(ekran1, textvariable=ad)
    k1.pack()
    Label(ekran1, text="Şifre: ").pack()
    k2 = Entry(ekran1, textvariable=sifre, show="*")
    k2.pack()
    Button(ekran1, text="Kayıt Ol", width=10, height=1, command=yaz).pack()
    Label(ekran1)


def anaekran():
    global ekran
    ekran = Tk()
    ekran.config(bg="lavenderblush")
    ekran.geometry("600x600")

    tarih = datetime.now()
    nettarih = datetime.ctime(tarih)
    locale.setlocale(locale.LC_ALL, 'tr_TR')

    ekran.title("Giriş Ekranı")
    Label(text="HOŞ GELDİNİZ", bg="lavenderblush", width="300", height="2", font=("Calibri",25)).pack()
    Label(text=nettarih, bg="lavenderblush", width="150", height="2", font=("Calibri",12)).pack(anchor=NE)
    Button(text="Giriş Yap", height="3", width="30", command=girisyap,bg="white").place(x=190,y=200)
    Button(text="Kayıt Ol", height="3", width="30", command=kayitol,bg="white").place(x=190,y=300)
    ekran.mainloop()


anaekran()

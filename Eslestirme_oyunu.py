from tkinter import*
def Yanıtıkontrolet():
    m = sehir.index(sehirListesi.get(sehirListesi.curselection()))
    n = plaka.index(plakaListesi.get(plakaListesi.curselection()))
    if m == n:
        yanıt.set("DOĞRU")
    else:
        yanıt.set("YANLIŞ")
window = Tk()
window.title("ŞEHİR-PLAKA")
Label(window, text="Şehir").grid(row=0, column=0)
Label(window, text="Plaka Kodu").grid(row=0, column=1)
sehir = ["Kırıkkale", "Ankara", "Kırşehir", "İzmir", "İstanbul", "Adana"]
plaka = ["71", "06", "40", "35", "34", "01"]
plakaSirali = list(plaka)
plakaSirali.sort()

sehirler = StringVar()
sehirListesi = Listbox(window, width=14, height=6, exportselection=0, listvariable=sehirler)
sehirListesi.grid(row=1, column=0, padx=10)
sehirler.set(tuple(sehir))

plakalar = StringVar()
plakaListesi = Listbox(window, width=5, height=6, exportselection=0, listvariable=plakalar)
plakaListesi.grid(row=1, column=1, padx=10)
plakalar.set(tuple(plakaSirali))

Kararbutonu = Button(window, text="Doğru mu? Yanlış mı?", command=Yanıtıkontrolet)
Kararbutonu.grid(row=2, column=0, columnspan=2, pady=5)
Label(window, text="CEVAP:").grid(row=3, column=0, sticky=E)
yanıt = StringVar()
Yanıtgiriş = Entry(window, width=10, textvariable=yanıt, state="readonly")
Yanıtgiriş.grid(row=3, column=1, padx=10, pady=(0,5), sticky=W)
window.mainloop()

import pygame,os,time
from tkinter import *
pygame.init()

#insta : @canustun_software :)
class işlemler:
    
    def __init__(self):
        self.müzikler=[]
        self.konumlar=[]
        self.çalan_şarkı=0
        for klasöryol,klasörism,dosyaism in os.walk('C:/Users'):
            for i in dosyaism:
                if i.endswith('.mp3'):
                    self.müzikler.append(i)
                    klasöryol=str(klasöryol).replace("\\","/")
                    self.konumlar.append(klasöryol)
        self.pencere=Tk()
        self.pencere.title("Müzik Çalar")
        self.pencere.geometry("250x255")
        self.pencere.resizable(width=FALSE, height=FALSE)
        Label(text="Müzik Çalara Hoşgeldin :)",bg="Gray",fg="White").pack()

        self.çalan_şarkı_ne=Label(text="     "+(self.müzikler[self.çalan_şarkı][:-4]+"                                                                            "),bg="Orange",fg="white")
        self.çalan_şarkı_ne.place(x=0,y=40)

        self.geri=Button(text="<",bg="Cyan")
        self.geri.config(command = self.geri_şarkı)
        self.geri.place(x=30,y=90)

        self.dur_başla=Button(text="+",bg="Red",fg="White",width=3)
        self.dur_başla.config(command = self.dur_başla_işlem)
        self.dur_başla.place(x=105,y=90)
        self.dur_başla_göstericisi=Label(text="Şarkı Durumu : Oynatılmıyor...")
        self.dur_başla_göstericisi.place(x=50,y=145)

        self.ileri=Button(text=">",bg="Cyan")
        self.ileri.config(command = self.ileri_şarkı)
        self.ileri.place(x=195,y=90)
        self.müzik_çal("tüm")
        self.pencere.mainloop()
    
    def dur_başla_işlem(self):

        if self.dur_başla['text']=="+":
            self.dur_başla_göstericisi['text']="Şarkı Durumu : Oynatılıyor..."
            self.dur_başla['text']="-"
            self.müzik_çal("")

        else:
            self.dur_başla_göstericisi['text']="Şarkı Durumu : Duraklatıldı..."
            self.dur_başla['text']="+"
            self.müzik_çal("dur")
            
    def müzik_çal(self,a):
        if a=="tüm":
            pygame.mixer.music.load(self.konumlar[self.çalan_şarkı]+"/"+self.müzikler[self.çalan_şarkı])
            pygame.mixer.music.play()
            pygame.mixer.music.pause()
        elif a=="dur":
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def geri_şarkı(self):
        self.dur_başla['text']="+"
        self.çalan_şarkı-=1
        
        if self.çalan_şarkı==-1:self.çalan_şarkı=len(self.müzikler)-1

        self.çalan_şarkı_ne['text']="     "+(self.müzikler[self.çalan_şarkı][:-4]+"                                                                            ")
        self.müzik_çal("tüm")
        self.dur_başla_işlem()

    def ileri_şarkı(self):
        self.dur_başla['text']="+"
        self.çalan_şarkı+=1
        
        if self.çalan_şarkı==len(self.müzikler):self.çalan_şarkı=0        

        self.çalan_şarkı_ne['text']="     "+(self.müzikler[self.çalan_şarkı][:-4]+"                                                                            ")
        self.müzik_çal("tüm")
        self.dur_başla_işlem()
        
tüm_işlemler=işlemler()

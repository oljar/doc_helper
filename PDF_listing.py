import io
from tkinter import messagebox
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import threading
import tkinter.scrolledtext as ScrolledText
import sys
import webbrowser
from tkinter import filedialog as fd
import time
import get_data_module





########################################################################################################################




#####################################################################################################################
#-*- coding: utf-8 -*-


start =time.time()
wynik = str()
b=str()
path =str()
sciezka = ''
lista_plikow=str()
_is_running = 1

count =0

password =""




class WorkThread(threading.Thread):
    def __init__(self):
        super().__init__()
        but={}

        global count

        count=count+1
        self.count=count
        self.next_page=tk.StringVar()







    def next_move(self):
       self.next_page=1

       return self.next_page



    def  run(self) :

        text = str()
        d = ()

        res=None

        score_frame = tk.LabelFrame(window, text='Wyniki')
        score_frame.grid(column=2, row=7)




        lbl.set('szukanie trwa ...')
        wynik = str()
        lista=str()

        try:
            lista_plikow = os.listdir((entry02.get()))
        except:
            messagebox.showinfo('info','Nieprawidłowa ścieżka dostępu_01')
            window.destroy()

            #os.close(fd='wb')





        if self.count !=1 :
            res = messagebox.askquestion('Exit Applikation', 'Czy kontynuować')

        if res == 'yes':
           os.execl(sys.executable,sys.executable,*sys.argv)




        elif res=='no':


            window.destroy()

        def callback(event):
            # webbrowser.open_new(r"file://"+str(entry02.get()+"\\"+event.widget['text']))
            webbrowser.open_new(r"file://" + (os.path.join(entry02.get(), event.widget['text'])))

        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        converter = TextConverter(resource_manager, fake_file_handle)
        page_interpreter = PDFPageInterpreter(resource_manager, converter)


        for i in lista_plikow:


                pdf_path = os.path.join(entry02.get(), i)
                self.next_page=0

                lista = ''
                licznik = 1

#start##core#start##core#start##core#start##core#start##core#start##core#start##core#start##core#start##core

                if i[-3]=='p' and i[-2]=='d' and i[-1]=='f' :



                    try:
                        fh = open(pdf_path, 'rb')
                    except:

                        pass


                    for page in PDFPage.get_pages(fh,

                                                          caching=True,
                                                          check_extractable=True):
                            page_interpreter.process_page(page)
                            lista = fake_file_handle.getvalue()


                else :
                        pass

                            # close open handles





                if str(entry.get()) in str(i) or str(entry.get()).lower() in str(i) or str(entry.get()).upper() in str(i):
                        nazwa = i
                        t = tk.Label(score_frame, text=nazwa.upper())
                        t.pack()
                        t.bind("<Button-1>", callback)




                if  str(entry.get())in str(lista) or str(entry.get()).lower() in str(lista) or str(entry.get()).upper() in str(lista) :
                            messagebox.showinfo('hih',i)
                            wynik = i

                            t=tk.Label(score_frame,text=wynik.lower())
                            t.pack()
                            t.bind("<Button-1>",callback)




                            score_frame_height=score_frame.winfo_height()

                            if score_frame_height>=250 and score_frame_height%250<250:
                                    cont = tk.Button(score_frame, text='Dalej', command = self.next_move)
                                    cont.pack()



                                    while True:

                                        if self.next_page==1:
                                            score_frame.destroy()
                                            score_frame = tk.LabelFrame(window, text='Wyniki')

                                            score_frame.grid(column=2, row=7)

                                            break





#core##stop#core##stop#core##stop#core##stop#core##stop#core##stop#core##stop#core##stop#core##stop#core##stop

                # funkcja odpowiedzialna za otwieranie plików w f(event) - zdarzenia



        lbl.set('Koniec')
        stop = time.time()
        print (stop-start)


def dialog_window():
    sciezka = fd.askdirectory()
    entry02.delete(0, 'end')
    entry02.insert(tk.INSERT,sciezka)




def znajdz():


    thread = WorkThread()

    thread.daemon=True
    thread.start()


def info():
    wininfo=Toplevel()
    wininfo.geometry('661x410')
    wininfo.title('Info')
    scrollbar = ScrolledText.ScrolledText(wininfo)
    scrollbar.pack()
    scrollbar.insert(INSERT, 'Program WYSZUKIWARKA PDF  - OPIS DZIAŁANIA  \n'
                             '\n'
                             'autor  - Jarosław Olszewski KJ Klimor\n'
                             'email  - jolszewski@klimor.com\n'
                             '\n'
                             'Wyszukiwarka XLS/X -  wyszukuje nazwy plików które zawierają podane frazy \n'
                             'lub numery w plikach excel o rozszerzeniach -.xls oraz -.xlsx \n'
                             '\n'
                             'Opis :\n'
                             '\n'
                             'SCIEŻKA - podaj ścieżkę dostępu wybranego folderu\n'
                             'HASŁO   – podaj wyszukiwaną frazę lub numer - WPISZ RĘCZNIE\n'
                             'SZUKAJ/STOP – 1-click start  wyszukiwania/2-gi  click  otwarcie okna dialogowego\n'
                             'CZY KONTYNUOWAĆ ? - Komunikat okna dialogowego\n' 
                             'TAK – reset programu\n'
                             'NIE – zamknięcie programu\n'
                             '\n'
                             'Kliknięcie na wyniki powoduje otwarcie znalezionego pliku\n'
                             '\n'
                             'małymi literami - wyświetlane są nazwy plików gdzie wyszukiwana fraza jest\n'
                             '                  w ich zawartości\n' 
                             '(w nawiasie)    - wyświetlana jest nazwa zakładki\n'
                             'WIELKIMI LITERAMI - wyświetlane sa nazwy plików gdzie wyszukiwana fraza jest\n'
                             '                  w nazwie pliku'
                             '\n'
                             'Należy zwrócić uwage na poprawność wpisania hasła (wpisz ręcznie) , gdyż błąd \n'
                             'znacząco zmieni wynik wyszukiwania.')



def spread(self):

    return self



# okno
window = tk.Tk()
window.title('wyszukiwarka PDF')
window.geometry('500x530')

############################################

dist = tk.Label(window,width=3)
dist.grid(column=0,row=0)

############################################

lab01 = tk.Label(window,text ='Scieżka ST',width=10)
lab01.grid(column=1,row=1)

############################################

dist = tk.Label(window,width=3)
dist.grid(column=2,row=1)

###########################################
entry02= tk.Entry(window,width = 45)
entry02.grid(column=2,row=1)
entry02.insert(tk.INSERT,sciezka)

#state="readonly"
############################################

btn_sciezka = tk.Button(window, text="Scieżka", command = dialog_window,width= 9 )
btn_sciezka.grid(column=4,row=1)

#############################################

label = tk.Label(window, text = 'Hasło')
label.grid(column=1,row=3)

##############################################
entry = tk.Entry(window, width = 45)
entry.grid(column=2,row=3)
#a=entry

###############################################

dist = tk.Label(window,width=3)
dist.grid(column=3,row=1)

###############################################
#
btn = tk.Button(window, text="Szukaj/Stop", command = znajdz )
btn.grid(column=4,row=3)

################################################
lbl=tk.StringVar()
label = tk.Label(window, textvariable=lbl, font=("Helvetica", 16))
lbl.set('Wpisz hasło')
label.grid(column=2,row=5)
##################################################
btn_info= tk.Button(window,text = 'info',command = info,padx='21')
btn_info.grid(column=4,row=5)

pathinfo = tk.Label(window,text = str(sciezka))
pathinfo.grid(column=2,row=6)
#

#scrollbar = ScrolledText.ScrolledText(window, width=32, height=5, wrap=tk.WORD)
#scrollbar.grid(column=3, row=8)








tk.mainloop()







import io
import os
import sys
import threading
import time
import tkinter as tk
import tkinter.scrolledtext as ScrolledText
import webbrowser
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
import get_data_module
import re

#-*- coding: utf-8 -*-

def blade_runner():

    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)




# core ## core ## core ## core ## core ## core ## core ## core ## core ## core ## core ## core ## core #



    try:
        fh = open('Dobór.pdf', 'rb')
    except:

        pass


    for page in PDFPage.get_pages(fh,

                                          caching=True,
                                          check_extractable=True):
            page_interpreter.process_page(page)
            lista = fake_file_handle.getvalue() #z pdf


    for pattern in get_data_module.get_data():
        #print(f'Słowa kluczowe:{pattern}')
        pattern_parameter_object = (re.finditer(pattern, lista, re.IGNORECASE))
        print('##########################################')
        print(pattern_parameter_object)
        a=pattern_parameter_object.__next__()
        print (a.span())
        print (a)
        b = pattern_parameter_object.__next__()
        print(b.span())
        print(b)


        # pattern_parameter=pattern_parameter_object.span()   # współrzędne 1-go znalezionego wzoru
        # print (pattern_parameter)
        # print(lista[pattern_parameter[0]:pattern_parameter[1]])
   #     lista_a = list(a)
   #     score.append(lista_a)

   #
   #  score = str(score)
   #  score = score.replace(']','').replace('[', '')
   #  score = score.split('>, <')
   #
   # # print (score)
    #
    #for pattern in get_data_module.get_data():
    #    print(pattern)




#        result = re.findall(pattern,string,flags=re.IGNORECASE)
#       print (result)

# probe_1.5





if __name__ == '__main__':

    blade_runner()



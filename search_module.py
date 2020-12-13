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

    word_01_list = []
    word_02_list = []
    for  pattern  in get_data_module.get_data():
        #print(f'Słowa kluczowe:{pattern}')
        pattern_parameter_object = (re.finditer(pattern, lista, re.IGNORECASE))

        parameter_01=pattern_parameter_object.__next__()

        word_01= lista[parameter_01.span()[0]:parameter_01.span()[1]]

        word_01_list.append(word_01)



    return  word_01_list  # solution list first-cought word,  # solution list second-cought word


# (?<=Typ).+?(?=<Wielkość)

if __name__ == '__main__':

    print(blade_runner())



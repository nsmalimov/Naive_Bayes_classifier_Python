# -*- coding: utf-8 -*-
import re
import string
from nltk import regexp_tokenize
from Stemmer import Stemmer
from math import log


def unpack_line(line):
    line = string.replace(line, " ", " ")
    els = string.split(line, " ")
    categories = els[1]
    sitename = els[0]
    return sitename, categories


class Categories:
   def __init__(self): 
       self.name_categories = ""
       self.num_docs = 0
       self.num_words = 0   
       self.line_allword = "" 
       self.lst_allword = []
       self.num_wordsunic = 0
       self.c = 0


def train(name_file_dbase, way_to_dbase):
    stm = Stemmer('russian')
    file_base = open(name_file_dbase, 'r')
    Lines = file_base.readlines()
    num_all_docs = len(Lines) + 1

    mass = []
    iter1 = 0
    iter2 = 0

    for line in Lines:
        number1, address1 = unpack_line(line)
        number = number1.strip("\n")
        address = address1.strip("\n")
        if (number == "1"):
            mass.append(Categories())
            mass[iter1].name_categories = address1
            mass[iter1 - 1].num_docs = iter2
            iter1 = iter1 + 1                            
            iter2 = 0
        iter2 = iter2 + 1
    mass[len(mass)-1].num_docs = iter2
    while_iter = 0
    
    file_base.close()              
    number = 1

    while while_iter < len(mass):
        while number <= mass[while_iter].num_docs:
            file_forclass = open(way_to_dbase + mass[while_iter].name_categories 
                                 + '/' + str(number) + 'forclass.txt', 'r')      
            str_read = re.sub("^\s+|\n|\r|\s+$", ' ', file_forclass.read())
            mass[while_iter].line_allword = mass[while_iter].line_allword + str_read
            file_forclass.close()
            number = number + 1 
        while_iter = while_iter + 1
        number = 1

    while_iter = 0

    while while_iter < len(mass):
        forstemmer = mass[while_iter].line_allword.decode('UTF-8')
        str_read = stm.stemWords(regexp_tokenize(forstemmer.lower(), r"(?x) \w+ | \w+(-\w+)*"))
        mass[while_iter].num_words = len(str_read)
        mass[while_iter].lst_allword = str_read
        lst_unic_words = list(set(mass[while_iter].lst_allword))
        mass[while_iter].num_wordsunic = len(lst_unic_words)
        while_iter = while_iter + 1   

    all_words = 0
    num_words_unic = 0
    while_iter = 0

    while while_iter < len(mass):
        all_words = all_words + mass[while_iter].num_words
        num_words_unic = num_words_unic + mass[while_iter].num_wordsunic
        while_iter = while_iter + 1
    return mass, num_all_docs, num_words_unic


def classif(text, mass, num_all_docs, num_words_unic):
    stm = Stemmer('russian')
    text = stm.stemWords(regexp_tokenize((text.decode('UTF-8')).lower(), r"(?x) \w+ | \w+(-\w+)*"))
    num_povt_words = 0
    summa = 0
    while_iter = 0
    while while_iter < len(mass):
        summand_1 = log((mass[while_iter].num_docs + 0.0) / (num_all_docs + 0.0) + 0.0, 1.1)
        for i in text:
            for i1 in mass[while_iter].lst_allword:
                 if i == i1:
                     num_povt_words = num_povt_words + 1 
            summand_2 = log(((num_povt_words + 1) + 0.0) / ((num_words_unic + mass[while_iter].num_words) + 0.0), 1.1)
            num_povt_words = 0
            summa = summa + summand_2
        mass[while_iter].c = summand_1 + summa
        summa = 0
        while_iter = while_iter + 1

    max_c = -100000
    while_iter = 0
    number_max = 0

    while while_iter < len(mass):
        print mass[while_iter].c
        if mass[while_iter].c > max_c:
            max_c = mass[while_iter].c
            number_max = while_iter
        while_iter = while_iter + 1
    print mass[number_max].name_categories  


def main():
    text_for_classif = "Концепция «торсионных полей» неоднократно осуждалась Комиссией РАН по борьбе с лженаукой. Критиками утверждается, что ни один из заявленных эффектов воздействия торсионных полей на вещество не получил экспериментального подтверждения, а некоторые из них были экспериментально опровергнуты. Согласно заявлениям академиков РАН Е. Б. Александрова и Э. П. Круглякова, исследования, проведённые в Институте общей физики РАН и других, показали отсутствие каких-либо воздействий изучаемых торсионных генераторов на материю и свет. Согласно утверждению М. С. Бродина, директора Института Физики НАН Украины, во время изучения предоставленного институту генератора торсионных полей исследовавшая его комиссия сделала однозначный вывод, что для объяснения наблюдаемых эффектов не требуется привлечение каких-либо новых полей[17]. При изучении образца металла с якобы повышенной под воздействием торсионных полей проводимостью было обнаружено как полное отсутствие заявленного эффекта, так и грубые методологические ошибки в предыдущих измерениях, ставящие под сомнение научную и инженерную квалификацию проводивших их представителей МНТЦ «ВЕНТ»"
    mass, num_all_docs , num_words_unic= train("file_list", "way_to_the_dbase")
    classif(text_for_classif, mass, num_all_docs, num_words_unic)
if __name__ == "__main__":
    main()

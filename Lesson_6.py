#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Создайте класс Word.
class Word:

    txt = None #text
#    pos = None #part of speech

    def __init__(self, txt):
        self.txt = txt
        #self.pos = pos

#Создайте классы Noun и Verb и Adverb
class Noun(Word):   #Настройте наследование от Word.
    _gc = "сущ."    #Добавьте защищённое свойство "Грамматические характеристики"
    def part(self):
        return "существительное"

class Verb(Word):   #Настройте наследование от Word.
    _gc = "гл."     #Добавьте защищённое свойство "Грамматические характеристики"
    def part(self):
        return "глагол"

class Adverb(Word): #В нашем предложении будет наречие
    _gc = "нар."    #Тоже защитим
    def part(self):
        return "наречие"

#Создайте класс Sentence
class Sentence:
    def __init__(self, words):
        self.content=words

    def show(self):
        s=''
        max = len(self.content)
        for n in self.content:
            if n < max-1:
                s += words[n].txt + " "
            else:
                s += words[n].txt + "."
        return s

    def show_parts(self):
        li=[]
        for n in self.content:
            if not words[n].part() in li:
                li.append(words[n].part())
        return li

#words = [['кошка', 'сущ.'],['сидит','гл.'],['высоко','нар.']]
#print(words)

words=[]
words.append(Noun("Кошка"))
words.append(Verb("сидит"))
words.append(Adverb("высоко"))

#s=Sentence([0,1,2])
s=Sentence([1,0,2])


print(s.show())
print(s.show_parts())
#print(s.content)




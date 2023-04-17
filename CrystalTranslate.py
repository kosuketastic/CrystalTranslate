# [CrystalTranslate] - Main code

import json

with open('wordtable.json', encoding="utf-8", mode="r") as f:
    global wordtable
    wordtable = json.load(f)

DEFAULT = 100

def find(l,v):
    c = 0
    for i in l:
        if i == v:
            return c
        c += 1

def pfind(l,v,lang,default):
    c = 0
    for i in l:
        if find(i[lang]["word"], v) != None:
            return i[lang]["priority"]
        c += 1
    return default

def psort(l):
    frl = []
    for j in range(len(l)):
        p = 0
        for i in l:
            if pfind(wordtable, i[1], "ja", DEFAULT) > p:
                p = pfind(wordtable, i[1], "ja", DEFAULT)
                v = i
        frl.append(v)
        l.remove(v)
    return frl

def Translate(text):
    tli = text.split()
    mli = []
    rli = []
    for i in tli:
        for j in wordtable:
            if find(j["en"]["word"],i.lower()) != None:
                mli.append([j["ja"]["c_particle"],j["ja"]["word"][0],j["ja"]["e_particle"]])
                break
        else:
            mli.append(["",i,""])
    mli = psort(mli)
    for i in mli:
        rli.append("".join(i))
    return "".join(rli)


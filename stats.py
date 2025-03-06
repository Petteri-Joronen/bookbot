def Number_of_words(text):
    sanojen_lista=text.split()
    sanojen_maara=len(sanojen_lista)
    return sanojen_maara
def number_of_each_letter(text):
    kirjaimet={}
    for i in text.lower():
        if i not in kirjaimet:
            kirjaimet[i]=1
        else:    
            kirjaimet[i]+=1
    return kirjaimet
def lajittelu(d):
        return d["num"]
def list_of_dictionaries(sanakirja):
    lista=[]
    for kirjain in sanakirja:
        lista.append({"char": kirjain, "num": sanakirja[kirjain]})
    lista.sort(reverse=True,key=lajittelu)
    return lista

from math import *
import random

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 
'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'] 

all_BiGramm = []
for symbol1 in range(len(alphabet)):
    for symbol2 in range(len(alphabet)):
        all_BiGramm.append(symbol1 + symbol2)

War_and_world = ''
ciphrotext = ''

def read_WA(name_file):
    txt = ''
    with open(f'{name_file}.txt', 'r', encoding='utf-8') as file:
        txt = file.read().replace("\n", "")
    return txt

def read_ciphrotext(name_file):
    text = ''
    with open(f'{name_file}.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    return text

War_and_world = read_WA('WarAndWorld').lower().replace("\ufeff", "")
ciphrotext = read_ciphrotext('input').lower()

freq_dic_OneGramm_current = dict()
freq_dic_OneGramm_candidate = dict()

freq_dic_BiGramm_current = dict()
freq_dic_BiGramm_candidate = dict()

freq_reference_OneGramm = dict()
freq_reference_BiGramm = dict()

def frequency_dic_OneGramm(input_text) -> dict:
    frec_dic = dict()
    for i in alphabet:
        frec_dic[i] = 0
    
    for i in input_text:
        if frec_dic.__contains__(i):
            frec_dic[i] += 1
    
    frec_dic = dict(sorted(frec_dic.items(), key=lambda x: x[1], reverse=True))
    return frec_dic

def frequency_dic_BiGramm(input_text) -> dict:
    frec_dic = {}
    for i in range(len(all_BiGramm)):
        frec_dic[i] = 0
    
    for i in range(len(input_text) - 1):
        st = input_text[i] + input_text[i+1]
        if st in frec_dic:
            frec_dic[st] += 1
    
    frec_dic = dict(sorted(frec_dic.items(), key=lambda x: x[1], reverse=True))
    return frec_dic

def distance(item1: dict, item2: dict):
    lst1 = list(item1.values())
    lst2 = list(item2.values())
    
    min_size = min(len(lst1), len(lst2))
    
    sum = 0
    
    for i in range(min_size):
        sum += pow((lst1[i] - lst2[i]), 2)
        
    if min_size == len(lst1):
        for i in range(min_size, len(lst2)):
            sum += pow(lst2[i], 2)
    elif min_size == len(lst2): 
        for i in range(min_size, len(lst1)):
            sum += pow(lst1[i], 2)
    
    return sum

#запоминаем какие замены уже были
idx_in_idx_dic = dict()

def replacing_indexes_in_key(idx1, idx2, key):
    
    item = key[idx1]
    key[idx1] = key[idx2]
    key[idx2] = item
        
    return key

def decoding(text, key):
    candidate_text = ""
    
    dic_freq_reference = list(freq_reference_OneGramm.keys())
    for symbol in text:
        if symbol in key:
            candidate_text += dic_freq_reference[key.index(symbol)] 
               
    return candidate_text

freq_reference_OneGramm = frequency_dic_OneGramm(War_and_world)
freq_reference_BiGramm = frequency_dic_BiGramm(War_and_world)

freq_dic_OneGramm_current = frequency_dic_OneGramm(ciphrotext)
freq_dic_BiGramm_current = frequency_dic_BiGramm(ciphrotext)

#получаем первое расстояние по биграммам
distan = distance(freq_reference_BiGramm, freq_dic_BiGramm_current)

currentKey = list(freq_dic_OneGramm_current.keys())

count = 0
while(True):
    
    if count >= 2000: break
    
    for i in range(33):
        for j in range(33):
            candidateKey = list(freq_dic_BiGramm_current.keys()).copy()
            candidateKey = replacing_indexes_in_key(i, j, candidateKey)
            
            freq_dic_BiGramm_candidate = frequency_dic_BiGramm(decoding(ciphrotext, candidateKey))
            
            new_dist = distance(freq_reference_BiGramm, freq_dic_BiGramm_candidate)
            
            count += 1
            
            if new_dist < distan:
                distan = new_dist
                count = 0
                currentKey = candidateKey.copy()
                
                
print(decoding(ciphrotext, currentKey))
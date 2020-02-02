file = open('text', 'r', encoding='UTF-8')
text = file.read()

#1) методами строк очистить текст от знаков препинания;
#2) сформировать list со словами (split);

punctuation = ['.',',',';',':','"','(',')','?','!','!','»','..','-','«','«']

wordList = text.split()

for q in range(5):
    i = 0
    for word in wordList:
        if word[-1] in punctuation:
            wordList[i] = word[:-1]
            word = wordList[i]
        if word[0] in punctuation:
            wordList[i] = word[1:]
        if word[0] == '—':
            del wordList[i]
        i += 1

print(wordList)

#3) привести все слова к нижнему регистру (map);

lowlist = list(map(lambda x:x.lower(),wordList))
print(lowlist)

#3) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
c = 0
dict = {}

for word1 in lowlist:
    kolvo = 0
    for word2 in lowlist:
        if word1 == word2:
            kolvo = kolvo + 1
        else:
            continue
    dict[word1] = kolvo
print(dict)

#4) вывести 5 наиболее часто встречающихся слов (sort),

list_dict = list(dict.items())
list_dict.sort(key=lambda i: i[1])
print(list_dict[-5:])

#вывести количество разных слов в тексте (set).

unic = set(dict)
kol_unic = list(unic)
print(len(kol_unic))

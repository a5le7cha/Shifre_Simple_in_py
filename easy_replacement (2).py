import random

input = """чжщцстэфюгасядэкчсэюошцлфсэдюуссвйцюдсрмчйфш
чсжэчюэнйняыржэасфнсшкйжспдюфйамюрэрацйчсгасщцюяйжюдсас
дмнснжыцйеэчюлэшсжфэрасщцэечэьасрндюжсьцйррэхччсраюнйня
ыясдээрсрцэксастэччсьфонюржэащсфэцнрнсцсчсфонйсрайдйрмю
всрюфсжчйядлкйжпюьюювотйжпюьржсэшсщйуюэчайрсжрэффсдскыф
ейцсфасдмнстасчйтючйлзэшсщсдэтюжйамкснасцйрокюждэчюэфвй
фэаюджчэфрщцюбсксфцскчыбжфэрасцйксраюнйняыахеэдолрнцыао
лцэпюфсрамщэцэчэрамтйркцошсьщыанюнсасцсьчэдмвхоеювяэшчо
амсчжюкэдщсасфнйнщстаюнйексэрдсжсщсрдэксжйжпэшсцйвшсжсц
йастчсщцюнйрйдсрмннйнсьчюяокмцйчээшсщйуюэчайюяэцэкюдсээ
чсжасеэжцэфхсчющскюжюдрхсатйраюрэшскчхпчэфоофэчюлждйкэа
мрсясьюрнцыжйамржсютожражйжтэцйпчэшсфсчсфйчйюввйфйдэьпэ
шсрдсжйжщйкйжпэшсжтэцйтоамчэжяэпэчражс""".replace("\n", "")

A = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

letter_combinations = []
for i in A:
    for j in A:
        letter_combinations.append(i + j)


def f(decode_text):
    stat_of_decode_text = get_bigram_stat(decode_text)
    return sum([(i[1] - stat_of_decode_text[i[0]])**2 for i in bin_stat_of_real_text.items()])


def get_bigram_stat(input_text):
    d = {i: 0 for i in letter_combinations}
    for i in range(len(input_text) - 1):
        pair = input_text[i] + input_text[i + 1]
        if pair in letter_combinations:
            d[pair] += 1
    summ = sum(d.values())
    for i in d.keys():
        d[i] /= summ
    return {k: v for k, v in sorted(d.items(),
                                    key=lambda item: item[1], reverse=True)}


def get_stat(input_text):  # статистика по убыванию
    d = {i: 0 for i in A}
    for i in input_text:
        if i in A:
            d[i] += 1
    summ = sum(d.values())
    for i in d.keys():
        d[i] /= summ
    return {k: v for k, v in sorted(d.items(),
                                    key=lambda item: item[1], reverse=True)}


def decode(input_text, key):
    result = ""
    statistic = list(stat_of_real_text.keys())
    for i in input_text:
        if i in A:
            result += statistic[key.index(i)]
    return result


def change_random(key):
    i1 = random.randint(0, 31)
    i2 = random.randint(0, 31)
    c = key[i1]
    key[i1] = key[i2]
    key[i2] = c
    return key


def change_key(key, index1, index2):
    c = key[index1]
    key[index1] = key[index2]
    key[index2] = c
    return key


text = open('tet.txt', encoding='utf-8').read().lower()
stat_of_real_text = get_stat(text)
bin_stat_of_real_text = get_bigram_stat(text)
key = list(get_stat(input).keys())
v = f(decode(input, key))
c = 0
while c < 2000:
    for i in range(33):
        for j in range(33):
            new_key = key.copy()
            new_key = change_key(new_key, i, j).copy()
            new_v = f(decode(input, new_key))
            c += 1
            if new_v < v:
                key = new_key.copy()
                v = new_v
                c = 0

print(v)
print(decode(input, key))

# 0.003045

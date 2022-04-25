import csv
file = open('./data.csv', 'r')
csvReader = csv.reader(file)

word1=str(input('Write first word to find: '))
word2=str(input('Write second word to find: '))
word3=str(input('Write third word to find: '))

data = []
data_words=[]
data_total=[]
error = 0

for line in csvReader :
    data.append(line)

try:
    for i in range(0, len(data)):
        count = 0
        words = data[i][0].split(' ')
        for j in words :
            if word1 in j or word2 in j or word3 in j:
                count = count + 1
        list_words = [words[5]+(words[6].split(':')[0]), count]
        list_total = [words[5]+(words[6].split(':')[0]), 1]
        data_words.append(list_words)
        data_total.append(list_total)
except:
    error = error + 1
    pass



dic_words = {}
dic_total = {}
dic_ratio = {}
for i in range(1,13):
    dic_words.update({'오전'+str(i):0})
    dic_words.update({'오후'+str(i):0})
    dic_total.update({'오전'+str(i):0})
    dic_total.update({'오후'+str(i):0})
    dic_ratio.update({'오전'+str(i):0})
    dic_ratio.update({'오후'+str(i):0})

for k in data_words :
    if k[0] in dic_words :
        dic_words[k[0]] = dic_words[k[0]]+ k[1]
for k in data_total :
    if k[0] in dic_total :
        dic_total[k[0]] = dic_total[k[0]] + 1
for k in dic_ratio:
   dic_ratio[k] = dic_words[k]/dic_total[k]

import matplotlib.pyplot as plt

new_dic={'AM 1':dic_ratio['오전1'],'AM 2':dic_ratio['오전2'],'AM 3':dic_ratio['오전3'],'AM 4':dic_ratio['오전4'], 'AM 5':dic_ratio['오전5'],
         'AM 6':dic_ratio['오전6'],'AM 7':dic_ratio['오전7'],'AM 8':dic_ratio['오전8'],'AM 9':dic_ratio['오전9'],'AM 10':dic_ratio['오전10'],
         'AM 11':dic_ratio['오전11'],'AM 12':dic_ratio['오전12'],'PM 1':dic_ratio['오후1'],'PM 2':dic_ratio['오후2'],'PM 3':dic_ratio['오후3'],
         'PM 4':dic_ratio['오후4'],'PM 5':dic_ratio['오후5'],'PM 6':dic_ratio['오후6'],'PM 7':dic_ratio['오후7'],'PM 8':dic_ratio['오후8'],
         'PM 9':dic_ratio['오후9'],'PM 10':dic_ratio['오후10'],'PM 11':dic_ratio['오후11'],'PM 12':dic_ratio['오후12']}
time=['AM 12','AM 1','AM 2','AM 3','AM 4','AM 5','AM 6','AM 7','AM 8',
        'AM 9','AM 10','AM 11','PM 12','PM 1','PM 2','PM 3','PM 4',
        'PM 5','PM 6','PM 7','PM 8','PM 9','PM 10','PM 11']
num=[new_dic['AM 12'],new_dic['AM 1'],new_dic['AM 2'],new_dic['AM 3'],new_dic['AM 4'],new_dic['AM 5'],
   new_dic['AM 6'],new_dic['AM 7'],new_dic['AM 8'],new_dic['AM 9'],new_dic['AM 10'],new_dic['AM 11'],
   new_dic['PM 12'],new_dic['PM 1'],new_dic['PM 2'],new_dic['PM 3'],new_dic['PM 4'],new_dic['PM 5'],
   new_dic['PM 6'],new_dic['PM 7'],new_dic['PM 8'],new_dic['PM 9'],new_dic['PM 10'],new_dic['PM 11']]

plt.style.use('ggplot')
plt.subplot(211)
plt.bar(range(len(dic_ratio)), num, align='center')
plt.xticks(range(len(dic_ratio)), time)
plt.xlabel('time')
plt.ylabel('ratio')
plt.title('Ratio of words appeared per Time')

new_dic1={'AM 1':dic_words['오전1'],'AM 2':dic_words['오전2'],'AM 3':dic_words['오전3'],'AM 4':dic_words['오전4'], 'AM 5':dic_words['오전5'],
         'AM 6':dic_words['오전6'],'AM 7':dic_words['오전7'],'AM 8':dic_words['오전8'],'AM 9':dic_words['오전9'],'AM 10':dic_words['오전10'],
         'AM 11':dic_words['오전11'],'AM 12':dic_words['오전12'],'PM 1':dic_words['오후1'],'PM 2':dic_words['오후2'],'PM 3':dic_words['오후3'],
         'PM 4':dic_words['오후4'],'PM 5':dic_words['오후5'],'PM 6':dic_words['오후6'],'PM 7':dic_words['오후7'],'PM 8':dic_words['오후8'],
         'PM 9':dic_words['오후9'],'PM 10':dic_words['오후10'],'PM 11':dic_words['오후11'],'PM 12':dic_words['오후12']}
time1=['AM 12','AM 1','AM 2','AM 3','AM 4','AM 5','AM 6','AM 7','AM 8',
        'AM 9','AM 10','AM 11','PM 12','PM 1','PM 2','PM 3','PM 4',
        'PM 5','PM 6','PM 7','PM 8','PM 9','PM 10','PM 11']
num1=[new_dic1['AM 12'],new_dic1['AM 1'],new_dic1['AM 2'],new_dic1['AM 3'],new_dic1['AM 4'],new_dic1['AM 5'],
   new_dic1['AM 6'],new_dic1['AM 7'],new_dic1['AM 8'],new_dic1['AM 9'],new_dic1['AM 10'],new_dic1['AM 11'],
   new_dic1['PM 12'],new_dic1['PM 1'],new_dic1['PM 2'],new_dic1['PM 3'],new_dic1['PM 4'],new_dic1['PM 5'],
   new_dic1['PM 6'],new_dic1['PM 7'],new_dic1['PM 8'],new_dic1['PM 9'],new_dic1['PM 10'],new_dic1['PM 11']]

plt.subplot(212)
plt.bar(range(len(new_dic1)), num1, align='center')
plt.xticks(range(len(new_dic1)), time1)
plt.xlabel('time')
plt.ylabel('number')
plt.title('Number of words appeared per Time')
plt.show()

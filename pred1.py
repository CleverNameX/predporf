#1 номер
import codecs
f = codecs.open('products.csv','r','UTF-8') #открываем файл
#Передаем значения файла в массив s, разделяя по ;
s = []
for i in f:
    s.append(i.split(';'))

l = []
#В последних двух ячейках нашей строки убираем символы ".0", чтобы в дальнейшем нам это не мешало, после чего в массив l сохраняем строки с категорией "Закуски"
for i in s:
    if '.0' in i[3] or '.0' in i[4]:
        i[3] = i[3].replace('.0','',1)
        i[4] = i[4].replace('.0', '', 1)
    if i[0] == 'Закуски':
        l.append(i)

summ = 0
for i in l: #Суммируем все наши произведения в переменной summ
    summ += (int(i[3]) * int(i[4]))
print('Итоговая сумма по категории "Закуски" равна:', summ)

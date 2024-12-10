# Анализ удобства раскладок
> В современном мире существует множество различных раскладок. Многие считают Йцукен не самой удобной раскладкой для использования.
> Использование наиболее эргономичной раскладки может существенно ускорить набор текста и снизить количество ошибок.
> Неправильно подобранная раскладка увеличивает нагрузку на руки, что может привести к усталости или профессиональным заболеваниям, таким как синдром запястного канала.




В своей работе мы анализируем 4 раскладки:
* Йцукен
* Вызов
* Диктор
* Скоропись

Для всех 4 раскладок мы считаем нагрузку на каждый палец, используя файл full_text.txt и количество диграмм, нажатых "удобным" перебором, используя файл digrams.txt, состоящий из двухбуквенных сочетаний.
Более подробно мы рассматриваем раскладку Вызов и сравниваем количество штрафов на пальцы, а также количество диграмм и триграмм, нажатых "удобным" перебором, используя файл 1grams-3.txt


**Раскладка йцукен**

![Раскладка йцукен](https://st.overclockers.ru/legacy/v3/02/29/29/2016/04/10/0u4311987e-6f40b1c2-549b7887.png)

**Раскладка вызов**

![Раскладка вызов](https://sun9-35.userapi.com/impg/MA8uqTjVNU8NyTRoinvH8OJBnxIP8Eke5m4GLA/YD33B3uGVAM.jpg?size=1728x576&quality=95&sign=ebf334233bddaa58f6ede4e2e23baf5e&type=album)

**Раскладка диктор**

![раскладка диктор](https://sun9-54.userapi.com/impg/l8jpSm6nDYG_80EUwio_EbE0ijSewHzH1LkdFw/cSANdY32a7o.jpg?size=742x256&quality=95&sign=adbbb76d316f284d7d3ea0b6f1a755ad&type=album)

**Раскладка скоропись**

![раскладка скоропись](https://sun9-77.userapi.com/impg/_qiS-UbsM_U3DgoxK-yPLOAfGEM0VMJvGqhG4g/VZrc0FOXDWk.jpg?size=710x245&quality=95&sign=430bc5534cf9e508e03e4f1c184b6ae3&type=album)




## Установка


```sh
git clone https://github.com/mar1naaa/keyboard.git
```

Запустить лабу 

### Для переключения между лабораторными работами:  

```sh
python3 main.py
```

Лабораторная №1 "Подсчёт нагрузок на пальцы в различных раскладках" :
```sh
git checkout master
```
Лабораторная №3 "Подсчёт штрафов на пальцы в раскладках *Вызов* и *Йцукен*":
```sh
git checkout lab3
```
Лабораторная №4 "Подсчёт диграмм, нажатых удобным перебором в различных раскладках":
```sh
git checkout lab4
```
Лабораторная №5 "Подсчёт диграмм и триграмм, нажатых удобным перебором в раскладках *Вызов* и *Йцукен*":
```sh
git checkout lab5
```
## Результаты работы программы

**Лабораторная №1 "Подсчёт нагрузок на пальцы в различных раскладках":**

![лабораторная 1](https://sun83-2.userapi.com/impg/oiojL25YSTuk5HL_9l4Hb1EJ3EvQ_0u77QlRMQ/vz3aaGkvufo.jpg?size=1000x600&quality=96&sign=5123301d6a68f5b4263a0c0ee207599e&type=album)

**Лабораторная №3 "Подсчёт штрафов на пальцы в раскладках *Вызов* и *Йцукен*":**

![лабораторная 3](https://sun9-75.userapi.com/impg/LoNv6hDQHHcfDP7R2Ss1MyP9zlvy6bg9JDBByg/n4zxCHhx8uc.jpg?size=1000x600&quality=95&sign=3b75ffe9835befe5653755c54f7a30ab&type=album)

**Лабораторная №4 "Подсчёт диграмм, нажатых удобным перебором в различных раскладках":**

![лабораторная 4](https://sun9-67.userapi.com/impg/I1FIfOCDN0w83oy9mBy_WOWOj8zKRl4jSpWv4w/V-qTFpTyGsM.jpg?size=1000x600&quality=95&sign=c85e61406f64c8fb00c99bd4e3e06029&type=album)

**Лабораторная №5 "Подсчёт диграмм и триграмм, нажатых удобным перебором в раскладках *Вызов* и *Йцукен*":**

![лабораторная 5](https://sun9-25.userapi.com/impg/aBzTWkaiCiCODhCz2WMMFhFGFbJJfupsSMDCoA/lH9oFlF4j14.jpg?size=1440x600&quality=95&sign=be04780a4b556388591079242bf2194a&type=album)


## Вывод

  Так как более подробно мы рассматривали раскладку *Вызов* и сравнивали её с привычным всем *Йцукеном*, вывод хотелось бы сделать, акцентируя внимание имеено на них.  
  Проведенные исследования и результаты программного анализа демонстрируют явное преимущество раскладки *вызов* перед традиционной *Йцукен*.  
  Оптимальное расположение клавиш, особенно часто встречающихся диграмм и триграмм, достаточно неплохо снижает количество ошибок и повышает скорость набора текста. Это подтверждается данными, полученными в ходе моделирований, где раскладка *Вызов* показала существенно меньшее количество штрафов по сравнению с *Йцукен*. Несмотря на несколько большую нагрузку на средний палец левой руки, характерную для данной раскладки, ее эргономичность и эффективность делают *Вызов* предпочтительным выбором для пользователей, стремящихся повысить свою производительность при работе с текстом. Таким образом, результаты нашего исследования позволяют сделать вывод, что раскладка *Вызов* является более эффективной и удобной для набора текста на русском языке, нежели столь популярная *Йцукен*.    
Если смотреть на количество нажатий в других раскладках, то раскладки *Диктор* и *Скоропись* имеют примерно одинаковое количество нажатий каждым пальцем. Кроме того, количество диграмм, набранных "удобным" перебором, тоже имеют одинаковые значения.   
  
> "Удобный" перебор: на левой руке - слева направо, на правой руке - справа налево, то есть от мизинца до большого пальца





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
#Для переключения между лабораторными работами:
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



## Вывод

  Так как более подробно мы рассматривали раскладку *Вызов* и сравнивали её с привычным всем *Йцукеном*, вывод хотелось бы сделать, акцентируя внимание имеено на них.  
  Проведенные исследования и результаты программного анализа демонстрируют явное преимущество раскладки *вызов* перед традиционной *Йцукен*.  
  Оптимальное расположение клавиш, особенно часто встречающихся диграмм и триграмм, достаточно неплохо снижает количество ошибок и повышает скорость набора текста. Это подтверждается данными, полученными в ходе моделирований, где раскладка *Вызов* показала существенно меньшее количество штрафов по сравнению с *Йцукен*. Несмотря на несколько большую нагрузку на средний палец левой руки, характерную для данной раскладки, ее эргономичность и эффективность делают *Вызов* предпочтительным выбором для пользователей, стремящихся повысить свою производительность при работе с текстом. Таким образом, результаты нашего исследования позволяют сделать вывод, что раскладка *Вызов* является более эффективной и удобной для набора текста на русском языке, нежели столь популярная *Йцукен*.    
Если смотреть на количество нажатий в других раскладках, то раскладки *Диктор* и *Скоропись* имеют примерно одинаковое количество нажатий каждым пальцем. Кроме того, количество диграмм, набранных "удобным" перебором, тоже имеют одинаковые значения.   
  
> "Удобный" перебор: на левой руке - слева направо, на правой руке - справа налево, то есть от мизинца до большого пальца





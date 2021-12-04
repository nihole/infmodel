Если вы любите математические задачи, возможно, вам будет интересно это небольшое математическое исследование. Примитивность рассматриваемой математической модели конечно же указывает на то,  что реальность будет отличаться от наших выводов, но все же этот расчет позволяет увидеть некоторые закономерности и не является, на мой взгляд, настолько уж оторванным от жизни.

Эта задача пришла ко мне как предположение, и мне захотелось обосновать его математически. Т.к. математика и рассуждения элементарны, мы не будем ссылаться ни на какие источники и просто решим задачу с нуля.

Вопрос, который явился триггером для меня, совершенно не математическим,  житейским языком, в самом общем виде можно сформулировать следующим образом:

"Как лучше пережить эпидемию короновируса - вводя ограничения, вакцинацию и весь спектр борьбы с распространением инфекции или позволить ситуации развиваться естественным путем?"

Конечно, в рамках этой статьи, мы не ответим на этот вопрос математически. В действительности, я не уверен, что сейчас эта задача в принципе решаема. Слишком много неизвестных факторов, которые могут еще проявиться. 

Что касается меня, то я являюсь сторонником ограничений и вакцинации, хотя бы потому что эта позиция мне понятна и кажется логичной в отличии от обычной аргументации оппонентов. Но я так же понимаю, что во многом это субъективно и все не так уж и однозначно. 

И вот об этой неоднозначности, или точнее об одном аспекте этой неоднозначности я бы и хотел поговорить на языке математики.

Попробуем понять, как меры борьбы с эпидемией влияют на длительность эпидемии.

Это не так очевидно, как может показаться на первый взгляд. Давайте сначала рассмотрим этот вопрос на качественном уровне. Что для нас важно, это то, что все меры прежде всего нацелены на понижение индекса (коэффициента) базовой репродукции - $R_0$. Этот коэффициент - усредненное количество людей, которых заражает заболевший.

Давайте предположим, что изначально коэффициент был довольно большой и количество заразившихся быстро дошло до 10000. После этого были приняты меры (любой набор мер) и коэффициент снизился. Если коэффициент меньше 1, то эпидемия побеждена. Но если нет.

Если коэффициент низкий, но все же больше или равен единице, то это значит, что эпидемия вяло развивается или держится на том же уровне. Переболевшие и вакцинированные люди получают иммунитет, но он не вечен, а это значит, что если эпидемия длится долго, то действие иммунитета может закончиться, что может теоретически привести к "вечному" циклу.

С другой стороны если коэффициент не сбивать, то очень быстро все могут переболеть и получить иммунитет, и это может быть настолько быстро, что иммунитет еще будет действовать, а это значит - конец эпидемии. Но при этом, количество  переболевших будет большим (теоретически, при большом коэффициенте, все человечество ), количество жизненных циклов и соответсвенно возможных мутаций вируса будет также большим, что приведет к повышенной вероятности возникновения нового штамма, который сможет обойти имунную защиту переболевших, что опять-таки может привести к ситуации бесконечной эпидемии.

Здесь надо понимать, что я намеренно выделяю лишь один фактор - продолжительность эпидемии, и не рассматриваю другие факторы, например, такие, как перегруженность системы здравоохранения и смертность, что безусловно важно, но это не является предметом данного анализа.

Теперь давайте рассмотрим все это с точки зрения математики.

Начнем с модели.

1. Однородность. Мы считаем, что все люди имеют равную вероятность заразиться и заразить, если они инфицированы.

2. Инфицированный является заразным только в течении времени  $T$. Это число является константой и одинаково для всех людей.

3. Переболев человек не может заболеть второй раз.

4. Мы будем пренебрегать фактором смертности.

5. Мы будем считать, что вакцинированный человек не может заболеть пока действует вакцина.

6. Для простоты вычислений мы будем считать, что люди заражаются синхронно, с интервалом $T/2$.
   То есть, в начале эпидемии (когда были введены меры) количество зараженных людей было $n_0$. В течении времени $T/2$ они заразили $n_1$ людей. Потом эти $n_1$ заразили $n_2$ через следующий интервал $T/2$ и т.д. Таким образом в точках $0, T/2, T, 2T/3, 2T, ..., kT/2..$ мы имеем число инфицированных. $n_0, n_1, n_2, n_3, n_4 ..., n_k, ...$

   ![inf](/Users/Roman/Desktop/inf.png)

   Пока не учитывая фактор вакцинации, и конечного времени действия иммунитета,  с учетом п.3 мы можем составить рекуррентное выражение:

$n_{k+1} = n_k R_0 \displaystyle\frac{N- \sum_{i=1}^kn_i}{N}$

Где $N = 7.5 * 10^9$ - это приблизительное число всех людей. 

О коэффициенте $R$ мы поговорим на 

Теперь учтем тот факт, что иммунитет не действует бесконечно. 

$n_{k+1} = n_k R_0 \displaystyle\frac{N- \sum_{i-w}^kn_i}{N}$

$w = int(2*imm\_time/T)$ , где $imm\_time$ - время действия иммунитета, а функция $int()$ отражает тот факт, что нам нужно выделить целую часть. В коде число $w$ будет обозначено как $iwin$.

Остался один параметр. Давайте предположим, что мы все время удерживаем количество провакцинированных как $\sigma$ от $N$. Что это дает? Конечно, это уменьшает $R_0$, но мы считаем, что это уже заложено в $R_0$. Но это также меняет и количество людей, которые подвержены этой инфекции на данный момент. С учетом этого последнего факта, нашу формулу можно записать в виде:

$n_{k+1} = n_k R_0 \displaystyle\frac{(1-\sigma) N- \sum_{i-w}^kn_i}{(1-\sigma) N}$

Замечание. Важно понимать, что такое $R_0$ в данной формуле. $R_0$ - это коэффициент репродукции вируса, в момент начала эпидемии, при условии что все меры борьбы уже приняты, в том числе провакцинировано $\sigma N$ человек.

Теперь все готово, чтобы продолжить наше исследование численными методами.

Эта небольшая функция написанная на Python рекуррентно находит все $n_i$ в зависимости от $R_0$. 

При этом концом эпидемии мы считаем момент, когда количество инфицированных в становится меньше $n\_end$ (в примере $n\_end = 1000$). Если же количество циклов становится равным 2400 (что соответствует 100 годам), то мы считает эпидемию вечной.

```python
from cfractions import Fraction
  
# Population
N = 7500000000

# Ratio of vaccinated from all people
sigma = 0.7

# Start of pandemic - number of infected people in the beginning of the pandemic
n0 = 10000

# End of the pandemic. Number of infected people that we consider as the end of the pandemic
n_end = 1000

# Immunity window. If T = one month, then iwin = 24 corresponds to 1 year of immunity
iwin = 24

# Max number of itterations (cicles). If T = one moths then macx = 2400 corresponds to 100 years. We consider this time as infinity
maxc = 2400

def pandemic(R0):
  R0 = Fraction(R0)
  n = [n0, int(R0 * n0)]
  # The number of people who retained natural immunity after an illness
  S = n0
  # The total number of infected since the beginning of the pandemic
  S_total = n0
  for i in range(2, maxc + 1):
    if i > iwin:
      S = S + n[i-1] - n[i - iwin -1 ]
    else:
      S = S + n[i-1]
    n.append(int(n[i-1]*R0*Fraction((int((1-sigma) * N) - S),int((1-sigma) * N))))
    S_total = S_total + n[i-1]
    # End of the pandemic
    if (n[i] < n_end):
      n.pop()
      break
    # All people are infected
    elif (S + n[i]) > (1-sigma) * N:
      n[i] = (1-sigma) * N - S
      S_total = S_total + n[i]
      break
  return (n, S_total)


```

Первое, давайте посмотрим, как продолжительность эпидемии зависит от $R_0$.

```python
from pandemic import pandemic

for j in range (1,30):

 # R0 is changing from 0.5 to 2.0 with step = 0.05
 R0 = 0.5 + 0.05 * j
 (n, Sum) = pandemic(R0)
 if len(n) == 2401:
  l = 'infinity'
 else:
  l = ("%0.1f months" % (len(n) / 2))
 print ("R0 = %0.2f pandemic duration = %s" % (R0, l))
```

Что дает:

```
R0 = 0.55 pandemic duration = 2.0 months
R0 = 0.60 pandemic duration = 2.5 months
R0 = 0.65 pandemic duration = 3.0 months
R0 = 0.70 pandemic duration = 3.5 months
R0 = 0.75 pandemic duration = 4.0 months
R0 = 0.80 pandemic duration = 5.5 months
R0 = 0.85 pandemic duration = 7.5 months
R0 = 0.90 pandemic duration = 11.0 months
R0 = 0.95 pandemic duration = 22.5 months
R0 = 1.00 pandemic duration = infinity
R0 = 1.05 pandemic duration = infinity
R0 = 1.10 pandemic duration = infinity
R0 = 1.15 pandemic duration = infinity
R0 = 1.20 pandemic duration = infinity
R0 = 1.25 pandemic duration = infinity
R0 = 1.30 pandemic duration = infinity
R0 = 1.35 pandemic duration = infinity
R0 = 1.40 pandemic duration = infinity
R0 = 1.45 pandemic duration = infinity
R0 = 1.50 pandemic duration = infinity
R0 = 1.55 pandemic duration = infinity
R0 = 1.60 pandemic duration = infinity
R0 = 1.65 pandemic duration = 21.0 months
R0 = 1.70 pandemic duration = 19.5 months
R0 = 1.75 pandemic duration = 18.5 months
R0 = 1.80 pandemic duration = 17.5 months
R0 = 1.85 pandemic duration = 16.5 months
R0 = 1.90 pandemic duration = 16.0 months
R0 = 1.95 pandemic duration = 15.0 months

```

Мы видим, что все хорошо, когда $R_0 <1$, что ожидаемо. 

Но мы также видим, что есть некоторое окно, в данном случае с точностью 0.05 это $1 \leq R_0 \leq 1.60 $, когда  пандемия становится бесконечной. Может показаться, что большой коэффициент спасает от этого. Но здесь мы должны вспомнить еще об одном параметре, который не был учтен в нашей модели - о возможности мутации вируса. Вероятность этой мутации зависит от количества новых поколений вируса в организме человека и тем их больше чем больше суммарное число инфицированных. 

Давайте предположим, что мы решили не применять никаких мер, понижающих $R_0$ в том числе и вакцинацию ($\sigma = 0$).

Давайте рассмотрим в этом случае как выглядит продолжительность эпидемии и суммарное количество заражений.

```python
from pandemic import pandemic

for j in range (1,30):

 # R0 is changing from 1.5 to 3.0 with step = 0.05
 R0 = 1.5 + 0.05 * j
 (n, Sum) = pandemic(R0)
 if len(n) == 2401:
  l = 'infinity'
 else:
  l = ("%0.1f months" % (len(n) / 2))
 print ("R0 = %0.2f pandemic duration = %s total number of infected = %i" % (R0, l, Sum))
```

Результат:

```
R0 = 1.55 pandemic duration = infinity total number of infected = 220677815238
R0 = 1.60 pandemic duration = infinity total number of infected = 226811933605
R0 = 1.65 pandemic duration = 23.5 months total number of infected = 5370663038
R0 = 1.70 pandemic duration = 21.5 months total number of infected = 5576536938
R0 = 1.75 pandemic duration = 20.5 months total number of infected = 5766191369
R0 = 1.80 pandemic duration = 19.0 months total number of infected = 5941026595
R0 = 1.85 pandemic duration = 18.0 months total number of infected = 6102298423
R0 = 1.90 pandemic duration = 17.0 months total number of infected = 6251123149
R0 = 1.95 pandemic duration = 16.5 months total number of infected = 6388501089
R0 = 2.00 pandemic duration = 15.5 months total number of infected = 6515326099
R0 = 2.05 pandemic duration = 15.0 months total number of infected = 6632350267
R0 = 2.10 pandemic duration = 14.5 months total number of infected = 6740402465
R0 = 2.15 pandemic duration = 14.0 months total number of infected = 6839848643
R0 = 2.20 pandemic duration = 13.5 months total number of infected = 6931809975
R0 = 2.25 pandemic duration = 13.0 months total number of infected = 7015592149
R0 = 2.30 pandemic duration = 12.5 months total number of infected = 7093938104
R0 = 2.35 pandemic duration = 12.0 months total number of infected = 7163933404
R0 = 2.40 pandemic duration = 11.5 months total number of infected = 7227716019
R0 = 2.45 pandemic duration = 11.0 months total number of infected = 7290611131
R0 = 2.50 pandemic duration = 10.5 months total number of infected = 7339160188
R0 = 2.55 pandemic duration = 10.0 months total number of infected = 7381860825
R0 = 2.60 pandemic duration = 9.5 months total number of infected = 7437276401
R0 = 2.65 pandemic duration = 9.0 months total number of infected = 7476194427
R0 = 2.70 pandemic duration = 9.0 months total number of infected = 7480251053
R0 = 2.75 pandemic duration = 7.5 months total number of infected = 7500000000
R0 = 2.80 pandemic duration = 7.5 months total number of infected = 7500000000
R0 = 2.85 pandemic duration = 7.5 months total number of infected = 7500000000
R0 = 2.90 pandemic duration = 7.5 months total number of infected = 7500000000
R0 = 2.95 pandemic duration = 7.0 months total number of infected = 7500000000
```

Это вполне ожидаемо. При большом коэффициенте инфекция распространяется очень быстро и теоретически (в рамках нашей модели) вся популяция должна переболеть. 

Всего на данным момент по официальным данным короновирусом переболело около 250 миллионов человек (https://index.minfin.com.ua/reference/coronavirus/geography/). Трудно сказать насколько это соответствует реальности, но т.к. мы просто ищем закономерности, не сильно оторванные от жизни, то давайте предположим, что переболело уже полмиллиарда. Штамм Омикрон вызывает опасение относительно эффективности существующих вакцин. Поэтому давайте предположим, что миллиард заболевших однозначно приводит к появлению нового штамма. А это значит, что большой коэффициент распространения без вакцинации нам не поможет.

Давайте посмотрим как влияет вакцинация на число зараженных.

$\sigma = 0.8$:

```
R0 = 1.55 pandemic duration = infinity  total number of infected = 44137208862
R0 = 1.60 pandemic duration = 22.0 months  total number of infected = 1029394126
R0 = 1.65 pandemic duration = 20.5 months  total number of infected = 1074129174
R0 = 1.70 pandemic duration = 19.0 months  total number of infected = 1115307417
R0 = 1.75 pandemic duration = 18.0 months  total number of infected = 1153240860
R0 = 1.80 pandemic duration = 17.0 months  total number of infected = 1188209267
R0 = 1.85 pandemic duration = 16.0 months  total number of infected = 1220463757
R0 = 1.90 pandemic duration = 15.5 months  total number of infected = 1250229539
R0 = 1.95 pandemic duration = 14.5 months  total number of infected = 1277703833
R0 = 2.00 pandemic duration = 14.0 months  total number of infected = 1303067348
R0 = 2.05 pandemic duration = 13.5 months  total number of infected = 1326478329
R0 = 2.10 pandemic duration = 13.0 months  total number of infected = 1348075345
R0 = 2.15 pandemic duration = 12.5 months  total number of infected = 1367982809
R0 = 2.20 pandemic duration = 12.0 months  total number of infected = 1386359330
R0 = 2.25 pandemic duration = 11.5 months  total number of infected = 1403121016
R0 = 2.30 pandemic duration = 11.0 months  total number of infected = 1418750454
R0 = 2.35 pandemic duration = 10.5 months  total number of infected = 1432952521
R0 = 2.40 pandemic duration = 10.0 months  total number of infected = 1445393497
R0 = 2.45 pandemic duration = 10.0 months  total number of infected = 1457620528
R0 = 2.50 pandemic duration = 9.5 months  total number of infected = 1469009415
R0 = 2.55 pandemic duration = 9.0 months  total number of infected = 1477033180
R0 = 2.60 pandemic duration = 9.0 months  total number of infected = 1483959184
R0 = 2.65 pandemic duration = 8.5 months  total number of infected = 1494021596
R0 = 2.70 pandemic duration = 7.0 months  total number of infected = 1499999999
R0 = 2.75 pandemic duration = 7.0 months  total number of infected = 1499999999
R0 = 2.80 pandemic duration = 7.0 months  total number of infected = 1499999999
R0 = 2.85 pandemic duration = 6.5 months  total number of infected = 1499999999
R0 = 2.90 pandemic duration = 6.5 months  total number of infected = 1499999999
R0 = 2.95 pandemic duration = 6.5 months  total number of infected = 1499999999
```

Все значения больше миллиарда.

$\sigma = 0.9$

```
R0 = 1.55 pandemic duration = infinity  total number of infected = 22069505976
R0 = 1.60 pandemic duration = 20.5 months  total number of infected = 514695999
R0 = 1.65 pandemic duration = 19.0 months  total number of infected = 537065667
R0 = 1.70 pandemic duration = 18.0 months  total number of infected = 557656577
R0 = 1.75 pandemic duration = 17.0 months  total number of infected = 576623650
R0 = 1.80 pandemic duration = 16.0 months  total number of infected = 594107704
R0 = 1.85 pandemic duration = 15.0 months  total number of infected = 610234454
R0 = 1.90 pandemic duration = 14.5 months  total number of infected = 625117358
R0 = 1.95 pandemic duration = 14.0 months  total number of infected = 638854827
R0 = 2.00 pandemic duration = 13.0 months  total number of infected = 651535454
R0 = 2.05 pandemic duration = 12.5 months  total number of infected = 663240413
R0 = 2.10 pandemic duration = 12.0 months  total number of infected = 674041084
R0 = 2.15 pandemic duration = 11.5 months  total number of infected = 683987977
R0 = 2.20 pandemic duration = 11.0 months  total number of infected = 693185108
R0 = 2.25 pandemic duration = 11.0 months  total number of infected = 701578547
R0 = 2.30 pandemic duration = 10.5 months  total number of infected = 709309436
R0 = 2.35 pandemic duration = 10.0 months  total number of infected = 716540143
R0 = 2.40 pandemic duration = 9.5 months  total number of infected = 722855799
R0 = 2.45 pandemic duration = 9.5 months  total number of infected = 728466650
R0 = 2.50 pandemic duration = 9.0 months  total number of infected = 734227840
R0 = 2.55 pandemic duration = 8.5 months  total number of infected = 739475703
R0 = 2.60 pandemic duration = 8.5 months  total number of infected = 742763124
R0 = 2.65 pandemic duration = 8.0 months  total number of infected = 745075411
R0 = 2.70 pandemic duration = 7.5 months  total number of infected = 749150918
R0 = 2.75 pandemic duration = 6.5 months  total number of infected = 749999999
R0 = 2.80 pandemic duration = 6.5 months  total number of infected = 749999999
R0 = 2.85 pandemic duration = 6.5 months  total number of infected = 749999999
R0 = 2.90 pandemic duration = 6.0 months  total number of infected = 749999999
R0 = 2.95 pandemic duration = 6.0 months  total number of infected = 749999999
```

Это уже неплохо. При этом, если $1 < R_0 \leq 1.55$ то мы получаем бесконечную пандемию.

А что, если $\sigma = 0.95$

```
R0 = 1.50 pandemic duration = infinity  total number of infected = 10670873250
R0 = 1.55 pandemic duration = 21.0 months  total number of infected = 245188791
R0 = 1.60 pandemic duration = 19.0 months  total number of infected = 257349433
R0 = 1.65 pandemic duration = 18.0 months  total number of infected = 268536232
R0 = 1.70 pandemic duration = 17.0 months  total number of infected = 278831999
R0 = 1.75 pandemic duration = 16.0 months  total number of infected = 288315365
R0 = 1.80 pandemic duration = 15.0 months  total number of infected = 297056971
R0 = 1.85 pandemic duration = 14.5 months  total number of infected = 305120690
R0 = 1.90 pandemic duration = 13.5 months  total number of infected = 312561088
R0 = 1.95 pandemic duration = 13.0 months  total number of infected = 319429784
R0 = 2.00 pandemic duration = 12.5 months  total number of infected = 325770312
R0 = 2.05 pandemic duration = 12.0 months  total number of infected = 331622342
R0 = 2.10 pandemic duration = 11.5 months  total number of infected = 337023483
R0 = 2.15 pandemic duration = 11.0 months  total number of infected = 341994871
R0 = 2.20 pandemic duration = 10.5 months  total number of infected = 346591089
R0 = 2.25 pandemic duration = 10.0 months  total number of infected = 350806484
R0 = 2.30 pandemic duration = 10.0 months  total number of infected = 354637786
R0 = 2.35 pandemic duration = 9.5 months  total number of infected = 358230933
R0 = 2.40 pandemic duration = 9.0 months  total number of infected = 361532237
R0 = 2.45 pandemic duration = 9.0 months  total number of infected = 364310607
R0 = 2.50 pandemic duration = 8.5 months  total number of infected = 366808895
R0 = 2.55 pandemic duration = 8.0 months  total number of infected = 369494043
R0 = 2.60 pandemic duration = 7.5 months  total number of infected = 372023933
R0 = 2.65 pandemic duration = 7.5 months  total number of infected = 373494263
R0 = 2.70 pandemic duration = 7.5 months  total number of infected = 373945921
R0 = 2.75 pandemic duration = 7.0 months  total number of infected = 374826496
R0 = 2.80 pandemic duration = 6.0 months  total number of infected = 375000000
R0 = 2.85 pandemic duration = 6.0 months  total number of infected = 375000000
```

Это уже вполне хороший результат.

Прежде чем озвучить выводы, хочу еще раз подчеркнуть, что 

Выводы

1. Самым эффективным способом является уменьшение усредненного по всем странам коэффициента распространения $R_0$ до значения меньше 1. Нет смысла делать это в отдельно взятой стране. Важно именно среднее значение.
2. Если предложенные меры не снижаютБез вакцинации при данных параметрах эпидемии (в рамках рассматриваемой математической модели) невозможно избежать вечной пандемии. Процент вакцинации должен быть высоким
   Замечание: конечно же есть надежда на то, что вирус мутирует до неопасных форм или параметры распространения изменятся. Но, если оставить все как есть (опять таки в рамках предложенной математической модели) мы получаем вечный цикл.
3. Этот пункт немного неожиданный. При высоком проценте вакцинации

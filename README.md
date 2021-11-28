# infmodel

Let's denote the sequence of the number of infected people as __n[0], n[1], n[2], ... n[k] ...__

__l = n[1] / n[0]__

__N__ - the population

__m = l / N__

__r[k+1] = n[k+1] / n[k]__

Then we have the following recursive dependencies: 

__r[k+1] = -m * n[k] + r[k]

__n[k] = n[k-1] * r[k]



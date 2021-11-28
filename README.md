# infmodel

Let's denote the sequence of the number of infected people as n[0], n[1], n[2], ... n[k] ....

- <img src="https://latex.codecogs.com/gif.latex?O_t=\text { Onset event at time bin } t " /> 

l = n[1] / n[0]

N - the population

m = l / N

r[k+1] = n[k+1]/n[k]

Then we have the following recursive dependencies: 

r[k+1] = -m * n[k] + r[k]

n[k] = n[k-1] * r[k]



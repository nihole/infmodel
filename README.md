# infmodel


__n[0]__ - some initial essential number of infected people. We consider this number as a beginning of pandemic.

__n[0], n[1], n[2], ... n[k] ...__ - the sequence of the number of infected people in time 

__R0 = n[1] / n[0]__ - basic reproduction number in the beginning of pandemic. This index is decreasing due to the increase in the number of people with immunity and anti-pandemic measures.

__N__ - the population, number of all people

__m = R0 / N__

__r[k+1] = n[k+1] / n[k]__

Then we have the following recursive dependencies: 

__r[k+1] = -m * n[k] + r[k]__

__n[k] = n[k-1] * r[k]__

This recursive dependencies permit us to find the sequence __n[0], n[1], n[2], ... n[k] ...__ 

When for some number i_stop n[i_stop] is less than an arbitrary sufficiently small number, we assume that the pandemic is over. For definiteness, we took a number equal to 100.

This means that i_stop is an estimation of a number of virus transmissions. The higher this number 

- the higher the probability of mutation
- the logner pandemic continues and as result the higher probability of critical weakening of immunity 

So this is quite an important index, and if this number is large enough it could lead to an “endless” pandemic.

This script calculates the dependency of i_stop from the R0

We see that maximum is when R0 is around 1.0. It means that if we wanted to increase the likelihood of an "eternal" pandemic, we should keep the transmission index around 1.0!

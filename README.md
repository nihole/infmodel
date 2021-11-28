# infmodel


___n[0]___ - some initial essential number of infected people. We consider this number as a beginning of pandemic.

___n[0], n[1], n[2], ... n[k] ...___ - the sequence of the number of infected people in time 

___R0 = n[1] / n[0]___ - basic reproduction number in the beginning of pandemic. This index is decreasing due to the increase in the number of people with immunity and anti-pandemic measures.

___N___ - the population, number of all people

___m = R0 / N___

___r[k+1] = n[k+1] / n[k]___

Then we have the following recursive dependencies: 

___r[k+1] = -m * n[k] + r[k]___

___n[k] = n[k-1] * r[k]___

This recursive dependencies permit us to find the sequence ___n[0], n[1], n[2], ... n[k] ...__+ 

When for some number ___i_stop___, ___n[i_stop]___ is less than an arbitrary sufficiently small number, we assume that the pandemic is over. For definiteness, we took a number equal to 100.

This means that ___i_stop___ is an estimation of a number of virus transmissions. The higher this number 

- the higher the probability of mutation
- the logner pandemic continues and as result the higher probability of critical weakening of immunity 

So this is quite an important index, and if this number is large enough it could lead to an “endless” pandemic.

This script calculates the dependency of ___i_stop___ from the ___R0___

We see that maximum is when R0 is around 1.0. It means that if we wanted to increase the likelihood of an "eternal" pandemic, we should keep the transmission index around 1.0!

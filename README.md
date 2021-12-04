# infmodel

## How to use 

___python3 pduration.py___  - returns duration of pandemic depending on __R0__

___python3 pmutation.py___  - returns dusation and total number of infected dependong on __R0__

## Parameters

Parameters may be adjusted in the file __pandemic.py__

___n[0]___ - some initial essential number of infected people. We consider this number as a beginning of pandemic

__n_end__ - the number of infected people that we consider as the end of the pandemic

___n[0], n[1], n[2], ... n[k] ...___ - the sequence of the number of infected people in time 

___R0 = n[1] / n[0]___ - basic reproduction number in the beginning of pandemic. This index is decreasing due to the increase in the number of people with immunity and anti-pandemic measures.

___N = 7500000000___ - the population, approximate number of all people

__sigma__ - the ratio of vaccinated from all people

  __iwin__ - immunity window. The number of iterations while immunity is still active. If T = one month, then iwin = 24 corresponds to 1 year of immunity.

## Model

__S[i] = S[i-1] + n[i-1] - n[i-iwin-1]__

__n[i+1] = R0 * n[i] * ((1-sigma) * N - S[i]))/((1-sigma) * N)__ 

This recursive dependencies permit us to find the sequence ___n[0], n[1], n[2], ... n[k] ...___

Script __pduration.py__ calculates duration of pandemic depending on __R0__



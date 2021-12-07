from cfractions import Fraction

# Population
N = 7500000000

# Ratio of vaccinated from all people
sigma = 0

# Start of pandemic - number of infected people in the beginning of the pandemic
n0 = 10000

# End of the pandemic. Number of infected people that we consider as the end of the pandemic
n_end = 1000

# Immunity window. If T = one month, then iwin = 24 corresponds to 1 year of immunity
iwin = 24

# Max number of itterations (cicles). If T = one moths then macx = 2400 corresponds to 100 years. We consider this time as infinity
maxc = 2400

def pandemic(R0):
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


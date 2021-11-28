
# Population
N = 7500000000.0

# Start of pandemic
n0 = 100000

def trnsm(R0):
  k_stop = 1000
  m = R0 / N
  n = [n0]
  r = [1,R0]
  for i in range(2, 100000):
    n.append(n[i-2] * r [i-1])
    r.append(-m * n[i-1] + r[i-1])
    if n[i-1] < 100:
      i_stop = i
      break
  return i_stop

for j in range (0,100):
## R0 is changing from 0.5 to 1.5  
  R0 = 0.5 + 0.01 * j
  number = trnsm(R0)
  print ("R0 = %s; number of virus transmissions  =  %d" % (R0, number))


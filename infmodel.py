
# Population
N = 7500000000.0

# Start of pandemic
n0 = 10000

def trnsm(R0):
  m = R0 / N
  n = [n0]
  S = n0
  r = [1.0,R0]
  for i in range(2, 100000):
    n.append(n[i-2] * r [i-1])
    r.append(-m * n[i-1] + r[i-1])
    S = S + n[i-1]
    if n[i-1] < 100:
      i_stop = i-1
      n.pop()
      break
    elif S > N:
      i_stop = i
      S = N
      n.pop()
      break
    else:
      continue
  return (i_stop, S)

for j in range (1,200):
## R0 is changing from 0.5 to 1.5  
  R0 = 0.5 + 0.01 * j
  (number, Sum) = trnsm(R0)
  index = float(number)/50 + float(Sum) / 100000000
  print ("index = %s R0 = %s; number of virus transmissions  =  %d, all infected = %d" % (index, R0, number, Sum))


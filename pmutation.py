from pandemic import pandemic

for j in range (1,30):
  # R0 is changing from 1.5 to 3.0 with step = 0.05
  R0 = 1.4 + 0.05 * j
  
  (n, Sum) = pandemic(R0)

  if len(n) == 2401:
    l = 'infinity'
  else:
    l = ("%0.1f months" % (len(n) / 2))

  print ("R0 = %0.2f pandemic duration = %s  total number of infected = %i" % (R0, l, Sum))

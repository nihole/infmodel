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

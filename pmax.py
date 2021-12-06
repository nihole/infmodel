from pandemic import pandemic

for j in range (0,30):
  # R0 is changing from 1.5 to 3.0 with step = 0.05
  R0 = 1.0 + 0.05 * j
  
  (n, Sum) = pandemic(R0)

  if len(n) == 2401:
    l = 'infinity'
  else:
    l = ("%0.1f months" % (len(n) / 2))
  
  maximum = max(n)
  print ("R0 = %0.2f, duration = %s, max = %i" % (R0, l, maximum))
#  print (maximum)
#  print ("%0.2f" % R0)

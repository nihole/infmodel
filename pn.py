from pandemic import pandemic

R0 = 1.30
(n, Sum) = pandemic(R0)
for i in range(2, 240):
  r = n[i]/n[i-1]
  print("%0.2f" % r)



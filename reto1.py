def edades(p):
  h=int(2*p+4)
  l=int((h+p)/5)
  if l<=20:
    reg=[p,h,l,'uno']
  elif l<=30:
    reg=[p,h,l,'dos']
  elif l<=50:
    reg=[p,h,l,'tres']
  else:
    reg=[p,h,l,'cuatro']
  return reg
p=78
[p1,h,l,etapa]=edades(p)
print(p1,h,l)
print(etapa)
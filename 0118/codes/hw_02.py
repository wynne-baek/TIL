odd_num = []

#range는 ()
for x in range(1,51,1):
  if x % 2 == 1 :
    odd_num.append(x)
  else:
    continue
  x = x + 1

print(odd_num)
#6 task 04


from time import perf_counter

def get_prime_divs(n):
  res = []
  for i in range(2, int(n ** 0.5) + 1):
    while not n % i:
      if not i in res:
        res.append(i)
      n //= i
    if n < i:
      break
  if n > 1:
     res.append(n)
  return res

n = 1000_000_000
start = perf_counter()
print(get_prime_divs(n))
print(perf_counter() - start)
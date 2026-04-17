import sys

def pangkat(a, b):
  hasil = 1
  for i in range(1, b + 1):
    hasil = a * hasil
    print("hasil %d pangkat %d adalah %d" % (a, i, hasil))

def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

def deretfibo(n):
  total = 0.0
  for i in range(1, n + 1):
    pembilang = float(fibonacci(2 * i - 1))
    penyebut = float(fibonacci(2 * i))
    suku = pembilang / penyebut
    
    if(i % 2 == 0):
      total -= suku
    else:
      total += suku
  return total

_tokens = []

def _scanf_next():
    global _tokens
    while not _tokens:
        line = sys.stdin.readline()
        if not line:
            return None
        _tokens = line.split()
    return _tokens.pop(0)

def main():
  print("1. A pangkat B\n2. Hitung 1 - 2/3 + 5/8 + 13/21\n0. Keluar")
  
  option_str = _scanf_next()
  if option_str is None:
    return 0
  option = int(option_str)

  if(option == 1):
    a_str = _scanf_next()
    b_str = _scanf_next()
    if a_str is not None and b_str is not None:
      a = int(a_str)
      b = int(b_str)
      pangkat(a, b)
  elif(option == 2):
    print("Masukkan jumlah N : ")
    n_str = _scanf_next()
    if n_str is not None:
      n = int(n_str)
      sys.stdout.write("hasil deret : %.6f" % deretfibo(n))
  elif(option == 0):
    return 0
  
  return 0

if __name__ == "__main__":
  main()

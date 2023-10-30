def CaesarCipherChar(c, k):
  if (k == 0 or not c.isalpha()):
      return c
  x = 'abcdefghijklmnopqrstuvwxyz'
  if (c.isupper()):
      x = x.upper()
  w, q = x.index(c) + k, len(x)
  if (w >= q):
      w %= q
  if (w < 0):
      w += q
  return x[w]
def CaesarCipher(s, k):
    a = ""
    for c in s:
        a += CaesarCipherChar(c, k)
    return a
s = input()
print(CaesarCipher(s, 3))
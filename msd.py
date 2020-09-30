class radix_MSD:
  R = 26 #26 caracteres, posicao 0 a 25
  M = 15
  aux = []
  def __init__(self):
    return None

  def charAt(self, string, d):
    if(d < len(string)):
      return ord(string[d])-65
    else:
      return -1

  def insertion_sort(self, C, first, end):
    if(end < first or first > len(C)):
      return C
    for i in range(first+1, end+1):
      j = i-1
      key = C[i]
      while(j >= first and C[j] > key):
        C[j+1] = C[j]
        j -= 1
      C[j+1] = key
    return C
  
     
  def sort(self, A, low, hi, d, B):
    C = [0] * (self.R+2)
    if(hi <= low + self.M):
      B = self.insertion_sort(A, low, hi)
      return B
    for i in range(low, hi+1):
      c = self.charAt(A[i], d)
      C[c+2] += 1
    for i in range(0, self.R-1):
      #ord retorna o codigo ascii do char
      #como só temos 26 chars, alinhando os caracteres
      # a = indice 0
      # b = indice 1...
      C[i+1] += C[i]
    for i in range(low, hi+1):
      c = self.charAt(A[i], d)
      B[C[c+1]] = A[i]
      C[c+1] += 1
    for j in range(low, hi+1):
      A[j] = B[j-low]
    for i in range(0, self.R):
      B = self.sort(A, low+C[i], low+C[i+1] - 1, d+1, B)

  def radix_sort(self, palavras):
    N = len(palavras)
    #Criando uma lista de Tamanho N vazia
    aux = [''] * N
    aux = self.sort(palavras, 0, N-1, 0, aux)
    return aux

test = ['HOW', 'TO', 'HELP', 'PRODUCE', 'OUR', 'NEW', 'EBOOKS', 'AND', 'HOW', 'TO', 'SUBSCRIBE', 'TO', 'OUR', 'EMAIL', 'NEWSLETTER', 'TO', 'HEAR', 'ABOUT', 'NEW', 'EBOOKS']
readx = radix_MSD()
print(len(test))
test = readx.radix_sort(test)
print(test)
##Counting sort funciona para strings
##Mas não para lista de strings
##Corrigir isso

class radix_MSD:
  R = 25 #26 caracteres, posicao 0 a 25
  M = 15
  aux = ''
  def __init__(self):
    return None

  def insertion_sort(self, C, first, end):
    key = 0
    biggest = C[0]
    i = 0
    j = 0
    for i in range(first+1, end):
      key = C[i]
      j = i - 1 
      while(j >= first and C[j] > key):
        C[j+1] = C[j]
        j -= 1 
      C[j+1] = key
    return "".join(C)
  
  
  def counting_sort(self, A, low, hi, d):
    C = [None] * (self.R +2) 
    A = list(A)
    B = [None] * len(A)
    for i in range(low, hi+1):
      C[i] = 0
    for i in range(0, self.R+1):
      #ord retorna o codigo ascii do char
      #como só temos 26 chars, alinhando os caracteres
      # a = indice 0
      # b = indice 1...
      C[ord(A[i])-65] += 1
    for i in range(low, hi+1):
      B[C[ord(A[i])-65]] = A[i]
    for j in range(len(A)-1, -1, -1):
      B[C[ord(A[j])-65]-1] = A[j]
      C[ord(A[j])-65] -= 1
    return "".join(B)
     
  def sort(self, palavras, low, hi, d):
    palavras = list(palavras)
    if(hi <= low + self.M):
      self.insertion_sort(palavras, low, hi)
      return
    palavras = self.counting_sort(palavras, low, hi, d)

  def radix_sort(self, palavras):
    N = len(palavras)
    #Criando uma lista de Tamanho N vazia
    self.aux = [None] * N
    self.sort(palavras, 0, N-1, 0)

radix = radix_MSD()
teste = ['ABACAXI', 'PATETA']

teste = radix.counting_sort(teste,0, len(teste)-1, 0)
print(teste)

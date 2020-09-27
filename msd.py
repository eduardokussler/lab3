class radix_MSD:
  R = 256
  M = 15
  aux = ''
  def __init__(self):
    return None

  def insertion_sort(self, C, first, end):
    key = 0
    biggest = C[0]
    C = list(C)
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

  def sort(self, palavras, low, hi, d):
    if(hi <= low + self.M):
      insertion_sort(palavras, low, hi)

  def radix_sort(self, palavras):
    N = len(palavras)
    #Criando uma lista de Tamanho N vazia
    self.aux = [None] * N
    sort(palavras, 0, N-1, 0)

radix = radix_MSD()
teste = 'wqdaasasahasasasa'

teste = radix.insertion_sort(teste,0,len(teste))
print(teste)


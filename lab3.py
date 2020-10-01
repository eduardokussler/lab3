# Foi usado o algoritmo MSD pois as palavras possuem tamanhos variáveis
# assim o radix-sort MSD é mais eficiente

class radix_MSD:
  R = 256 # 256 caracteres asc, posicao 0 a 25
  M = 15
  aux = []
  def __init__(self):
    return None

  def charAt(self, string, d):
    if(d < len(string) and d >=0):
      return ord(string[d])
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
      A = self.insertion_sort(A, low, hi)
      if(B is None):
        print("DEU RUIM")
      return A
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
      if(B is None):
        print("DEU RUIM")
      A = self.sort(A, low+C[i], low+C[i+1] - 1, d+1, B)
    return A



  def radix_sort(self, palavras):
    N = len(palavras)
    #Criando uma lista de Tamanho N vazia
    aux = [''] * N
    aux = self.sort(palavras, 0, N-1, 0, aux)
    return aux



def main():
  #abrindo e criando os arquivos de saída
  frankestein = open('frankestein_clean.txt', 'r')
  war_and_peace = open('war_and_peace_clean.txt', 'r')
  frankestein_ordenado = open('frankenstein_ordenado.txt', 'w+')
  frankestein_ocorrencias = open('frankestein_ocorrencias.txt', 'w+')
  war_and_peace_ordenado = open('war_and_peace_ordenado.txt', 'w+')
  war_and_peace_ocorrencias = open('war_and_peace_ocorrencias.txt', 'w+')
  
  #Caracteres a serem considerados
  caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  

  frankestein_array = leArq(frankestein)
  war_and_peace_array = leArq(war_and_peace)
  #Chamando a ordenacao
  msd = radix_MSD()
  frankestein_array = msd.radix_sort(frankestein_array)
  checkCorrectness(frankestein_array)
  escreveArq(frankestein_ordenado ,frankestein_array)

  war_and_peace_array = msd.radix_sort(war_and_peace_array)
  checkCorrectness(war_and_peace_array)
  escreveArq(war_and_peace_ordenado, war_and_peace_array)
  

  frankestein.close()
  war_and_peace.close()
  frankestein_ordenado.close()
  frankestein_ocorrencias.close()
  war_and_peace_ordenado.close()
  war_and_peace_ocorrencias.close()
  
#Le o arquivo file e copia cada palavra para uma posicao de arr
def leArq(file):
  arr = file.read()
  arr = arr.split(' ')
  return arr

def escreveArq(file, arr):
  for i in arr:
    file.write(i)
    file.write("\n")
  

def checkCorrectness(palavras):
  n = len(palavras)
  for i in range(0, n-1):
    if(palavras[i] > palavras[i+1]):
      print("*** INCORRECT ORDERING ***")
      print(f"Palavra {palavras[i]} deveria estar depois de {palavras[i+1]}")
      return
  print("*** CORRECT ORDERING ***")
main()
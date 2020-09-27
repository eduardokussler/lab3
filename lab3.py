# Foi usado o algoritmo MSD pois as palavras possuem tamanhos variáveis
# assim o radix-sort MSD é mais eficiente

def main():
  #abrindo e criando os arquivos de saída
  frankestein = open('frankestein_clean.txt', 'r')
  war_and_peace = open('war_and_peace_clean.txt', 'r')
  frankestein_ordenado = open('frankenstein_ordenado.txt', 'w')
  frankestein_ocorrencias = open('frankestein_ocorrencias.txt', 'w')
  war_and_peace_ordenado = open('war_and_peace_ordenado.txt', 'w')
  war_and_peace_ocorrencias = open('war_and_peace_ocorrencias.txt', 'w')
  
  #Caracteres a serem considerados
  caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  

  frankestein_array = leArq(frankestein)
  war_and_peace_array = leArq(war_and_peace)
  #Chamando a ordenacao
  
  


  frankestein.close()
  war_and_peace.close()
  frankestein_ordenado.close()
  frankestein_ocorrencias.close()
  war_and_peace_ordenado.close()
  war_and_peace_ocorrencias.close()
  
#Le o arquivo file e copia cada palavra para uma posicao de arr
def leArq(file):
  arr = file.read()
  #arr = arr.split(' ')
  return arr
main()
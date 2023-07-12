#import multiprocessing
from spellchecker import SpellChecker
import numpy as np

#variaveis globais
palavras_corrigidas = {} #dicionario contendo as palavras corrigidas como keys e qtd de erros como valores
arquivos_corretos = [] #lista de listas para cada arquivo processado
dicionarios_corretos = [] #lista de dicionarios


def corrigir_texto(texto):
    # Criar uma instância do corretor ortográfico
    spell = SpellChecker(language='pt')
    # Lista para armazenar as palavras corrigidas
    texto_corrigido = []
  

    for i in texto:
        correcao_palavra = []
        palavras = i.split() #separa cada linha por palavra e põe num vetor
        print(palavras)
        for palavra in palavras: #para cada palavra no meu vetor, faça:
   
            if not spell.correction(palavra) == palavra: #se não está escrita corretamente:
                palavra_certa = spell.correction(palavra) #corrige a palavra
                correcao_palavra.append(palavra_certa) #adiciona no vetor de texto corrigido
                print("aplicação logo após a correção ->", correcao_palavra)
                conta_erro(palavra_certa) #atualiza dicionário

            else: #se está escrita corretamente
                correcao_palavra.append(palavra)  #se estiver correta, manter a palavra original
                print("aplicação fora da correção ->", correcao_palavra)

        linha_corrigida = ' '.join(correcao_palavra) #junta cada palavra corrigida de volta em uma linha
        print("após o join -> ", linha_corrigida)
        texto_corrigido.append(linha_corrigida) #coloca a linha ao final do meu vetor de texto

        
    return texto_corrigido #retorna um vetor com as linhas corretas do arquivo e o dicionario de palavras corrigidas


def conta_erro(palavra_certa):
    cont = 0

    if len(palavras_corrigidas) >= 1: #se o dicionário não estiver vazio
        for chave in palavras_corrigidas.keys(): #para cada palavra no meu vetor de corrigidas, verifica: 
            if palavras_corrigidas[chave] != palavra_certa:
                cont +=1 #conta para cada palavra diferente

            else: #se já foi corrigida antes, atualiza o total de erros naquela palavra
                aux = palavras_corrigidas[palavra_certa]
                palavras_corrigidas[palavra_certa] = aux + 1
                break
            
    if cont == len(palavras_corrigidas) or cont == 0: #se contador == quantidade de palavras corrigidas (palavra não foi corrigida aidna)
                palavras_corrigidas[palavra_certa] = 1 #adiciona minha palavra como key e o nmr atual de erros no dicionário
 


    #print("aqui vai o dicionario:\n")    
    #print(palavras_corrigidas)


def Le_Arquivo(arquivo):
    texto_original = []
    #correcao_palavra = []
    #arquivos_finais = []
    texto = open(arquivo,'r')

    for linha in texto:
        texto_original.append(linha) #texto_original[linha1,linha2,linha3,...]
    texto.close()

    return texto_original
    
def Compara_texto(erros):

    valores_erro = np.asarray(erros) #transforma a lista em um array para operar



    return 



def main():  
    arquivos = ['exemplo.txt']

    #corrige os textos 1 por 1 guardando-os em uma lista de listas realizando as
    #operações necessárias no dicionário
    for n in range(len(arquivos)):
        arquivo_original = Le_Arquivo(arquivos[n]) #processa os arquivos linha por linha
        arquivo_corrigido = corrigir_texto(arquivo_original) #corrige os arquivos linha por linha
        arquivos_corretos.append(arquivo_corrigido) #adiciona os textos corrigidos (em listas)


    #após todos os arquivos serem processados, corrigidos e armazenados
    vetor_num_erro = [] #lista para pegar os valores do dicionario
    vetor_palavra_erro = [] #lista para pegar as keys do dicionario

    #dicionario referente ao texto. precisa refenciar ele dentro da lista de dicionarios
    for chave,valor in palavras_corrigidas.items(): #atribue os valores para a lista
        vetor_num_erro.append(valor)
        vetor_palavra_erro.append(chave)
        print(vetor_num_erro)
        print(vetor_palavra_erro)

    #chama função de comparação de texto
    Compara_texto(vetor_num_erro) 


#preciso mesmo printar k
    for lista in arquivo_corrigido:
        print(lista)
        print("---")


main()
#fofes -> fores

#https://pyspellchecker.readthedocs.io/en/latest/
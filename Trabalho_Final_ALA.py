import multiprocessing
from spellchecker import SpellChecker
import numpy as np

def corrigir_texto(texto):
    # Criar uma instância do corretor ortográfico
    spell = SpellChecker(language='pt')
    # Lista para armazenar as palavras corrigidas
    palavras_corrigidas = {}
    correcao_palavra = []
    texto_corrigido = []



#tenho que ver se a palavra já foi corrigida antes, e contar
#posso ajeitar tudo num dicionario com as keys sendo as palavras e os valores sendo o nmr de rros
#posso passar o número de erros para um array no final e realizar as operações de comparação


    for i in texto:
        palavras = i.split() #separa cada linha por palavra e põe num vetor
        for palavra in palavras: #para cada palavra no meu vetor, faça:

            if not spell.correction(palavra) == palavra: #se não está escrita corretamente:
                palavra_certa = spell.correction(palavra) #corrige a palavra
                correcao_palavra.append(palavra_certa) #adiciona no vetor de texto corrigido

                for chave in palavras_corrigidas.keys(): #para cada palavra no meu vetor de corrigidas, verifica:
                        
                        if palavras_corrigidas.keys(chave) != palavra_certa: #se não foi corrigida antes
                            palavras_corrigidas[palavra_certa] = 1 #adiciona minha palavra como key e o nmr atual de erros no dicionário

                        else: #se já foi corrigida antes, atualiza o total de erros naquela palavra
                            aux = palavras_corrigidas[palavra_certa]
                            palavras_corrigidas[palavra_certa] = aux + 1

            else: #se está escrita corretamente
                correcao_palavra.append(palavra)  #se estiver correta, manter a palavra original

        linha_corrigida = ' '.join(correcao_palavra) #junta cada palavra corrigida de volta em uma linha
        texto_corrigido.append(linha_corrigida) #coloca a linha ao final do meu vetor de texto

        
    return texto_corrigido, palavras_corrigidas #retorna um vetor com as linhas corretas do arquivo e o dicionario de palavras corrigidas





def Le_Arquivo(arquivo):
    texto_original = []
    #correcao_palavra = []
    #arquivos_finais = []

    texto = open(arquivo,'r')
    #texto_original[linha1,linha2,linha3,...]
    for linha in texto:
        texto_original.append(linha.strip()) 
    texto.close()

    return texto_original
    
def Compara_texto(dict_erros):
    vetor_num_erro = [] #cria uma lista para pegar os valores do dicionario

    for valor in dict_erros.values(): #atribue os valores para a lista
        vetor_num_erro.append(valor)

    valores_erro = np.asarray(vetor_num_erro) #transforma a lista em um array para operar





    return 




def main():  
    arquivos = ['exemplo.txt']

    for n in range(len(arquivos)):
        arquivo_original = Le_Arquivo(arquivos[n])
        retorno = corrigir_texto(arquivo_original)
        arquivo_corrigido = retorno[0]
        dict_palavras_corrigidas = retorno[1]
        Compara_texto(dict_palavras_corrigidas)



#parece que estou adicionando uma linhas mais de uma vez!! olhar a lógica do for da função de corrigir

#preciso mesmo printar k
    for lista in arquivo_corrigido:
        print(lista)
        print("---")


main()
#fofes -> fores

#https://pyspellchecker.readthedocs.io/en/latest/
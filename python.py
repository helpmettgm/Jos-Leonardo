from googletrans import Translator
# Tradutor de ingles para o portugues


def traduzir_para_portugues(texto_em_ingles):
    tradutor = Translator()
    traducao = tradutor.translate(texto_em_ingles, src='en', dest='pt')
    return traducao.text


frase = input('Digite uma palavra ou frase em ingles:')
traducao = traduzir_para_portugues(frase)
print(f'Traducao em portugues:{traducao}')
# Tradutor do portugues para o ingles


def traduzir_para_ingles(texto_em_portugues):
    tradutor = Translator()
    traducao = tradutor.translate(texto_em_portugues, src='pt', dest='en')
    return traducao.text


frase = input('Digite uma palavra ou frase em portugues:')
traducao = traduzir_para_ingles(frase)
print(f'Translation in english:{traducao}')

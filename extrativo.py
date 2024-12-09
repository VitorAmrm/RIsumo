# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:17:29 2024

@author: Vitor
"""
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer
from nltk.tokenize import sent_tokenize, word_tokenize

# Baixar o pacote de tokenização do NLTK, caso ainda não tenha feito
import nltk
nltk.download('punkt')

class Tokenizer(object):
    def to_sentences(self, text):
        return sent_tokenize(text)  # Usando o NLTK para tokenizar em sentenças
    
    def to_words(self, text):
        return word_tokenize(text)  # Usando o NLTK para tokenizar em palavras

def gerar_resumo_extrativo(texto):
    # Criar o tokenizador
    tokenizer = Tokenizer()

    # Criar o parser com o tokenizador adequado
    parser = PlaintextParser.from_string(texto, tokenizer)

    # Criar o summarizer (usando LSA como exemplo)
    summarizer = LsaSummarizer()

    # Gerar o resumo (com 3 frases, como exemplo)
    resumo = summarizer(parser.document, 3)

    # Concatenar as frases do resumo em um único texto
    resumo_texto = " ".join(str(frase) for frase in resumo)

    return resumo_texto







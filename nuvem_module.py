# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:12:04 2024

@author: Vitor
"""
import os
import string
import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from wordcloud import WordCloud
import PyPDF2
import pdfplumber

# Função para extrair texto de PDF
def extrair_texto_pdf(pdf_path):
    try:
        with open(pdf_path, "rb") as f:
            pdf_reader = PyPDF2.PdfReader(f)
            texto = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                texto += page.extract_text()  # Extrai texto de cada página
            if texto.strip():
                return texto
            else:
                raise ValueError("O texto extraído usando PyPDF2 está vazio.")
    except Exception as e:
        try:
            with pdfplumber.open(pdf_path) as pdf:
                texto = ""
                for page in pdf.pages:
                    texto += page.extract_text()
                return texto
        except Exception as e:
            raise ValueError(f"Erro ao tentar ler o PDF: {e}")

# Função para gerar nuvem de palavras com suporte a PDF e TXT
def gerar_nuvem_palavras(filepath, output_path='nuvem.png', palavras_extras=None, max_palavras=100):
    # Verificar se o arquivo é PDF ou TXT
    if filepath.lower().endswith(".pdf"):
        # Extrair texto do PDF
        texto = extrair_texto_pdf(filepath)
    elif filepath.lower().endswith(".txt"):
        # Ler o conteúdo do arquivo TXT
        with open(filepath, mode='r', encoding='utf-8') as file:
            texto = file.read()
    else:
        raise ValueError("Formato de arquivo não suportado. Apenas .pdf e .txt são aceitos.")

    # Transformar o texto em minúsculas
    texto = texto.lower()

    # Remover pontuação
    texto_sem_pontuacao = ''.join([p for p in texto if p not in string.punctuation])

    # Baixar recursos necessários
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)

    # Carregar stopwords em português
    stopwords_pt = stopwords.words('portuguese')

    # Adicionar palavras extras às stopwords
    if palavras_extras:
        stopwords_pt.extend(palavras_extras)

    # Tokenização do texto
    tokenizacao = nltk.word_tokenize(texto_sem_pontuacao)

    # Remover stopwords
    tokenizacao_sem_stopwords = [p for p in tokenizacao if p not in stopwords_pt]

    # Frequência das palavras
    freq = FreqDist(tokenizacao_sem_stopwords)

    # Gerar nuvem de palavras
    nuvem_palavras = WordCloud(
        background_color='white',
        stopwords=stopwords_pt,
        height=1080,
        width=1080,
        max_words=max_palavras
    )

    # Usar palavras filtradas para a nuvem
    nuvem_palavras.generate(' '.join(tokenizacao_sem_stopwords))

    # Salvar a nuvem em um arquivo
    nuvem_palavras.to_file(output_path)
    return output_path

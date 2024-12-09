# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:14:45 2024

@author: Vitor
"""
from transformers import pipeline

# Carregar modelo de resumo abstrativo BART
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def gerar_resumo_abstrativo(texto):
    # Truncar o texto para garantir que ele não ultrapasse o limite de tokens do modelo
    max_length = 1024  # Limite de tokens para o modelo BART
    if len(texto.split()) > max_length:  # Verificar se o texto ultrapassa o limite
        texto = ' '.join(texto.split()[:max_length])  # Truncar o texto para max_length palavras
    
    # Gerar o resumo
    summary = summarizer(texto, max_length=300, min_length=30, do_sample=False)
    
    return summary[0]['summary_text']



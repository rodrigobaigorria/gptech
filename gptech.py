#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 15:59:15 2023

@author: hbaigorria
"""

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import sys
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

model_name = 'EleutherAI/gpt-neo-2.7B'
# Obtenemos el texto pasado como parámetro
prompt = sys.argv[1]
model_path = '/gptech_model'
tokenizer_path = '/gptech_tokenizer'
# Descargar el modelo y el tokenizador si aún no están disponibles
if not os.path.exists(model_path):
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.save_pretrained(model_path)
else:
    model = AutoModelForCausalLM.from_pretrained(model_path)

if not os.path.exists(tokenizer_path):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.save_pretrained(tokenizer_path)
else:
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)

# Crear el generador utilizando el modelo y el tokenizador
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

# prompt = "crea un alert en javascript"
res = generator(prompt, max_length=500, do_sample=True, temperature=0.7)

print(res[0]['generated_text'])

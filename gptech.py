#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 06:07:15 2023

@author: hbaigorria
"""

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from curtsies.fmtfuncs import red, bold, green, on_blue, yellow, blue, cyan

from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = 'EleutherAI/gpt-neo-2.7B'

# Descargar el modelo y el tokenizador si aún no están disponibles
if not os.path.exists('gptech_model'):
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.save_pretrained('gptech_model')
else:
    model = AutoModelForCausalLM.from_pretrained('gptech_model')

if not os.path.exists('gptech_tokenizer'):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.save_pretrained('gptech_tokenizer')
else:
    tokenizer = AutoTokenizer.from_pretrained('gptech_tokenizer')

# Cargar el modelo y el tokenizador
model = AutoModelForCausalLM.from_pretrained('gptech_model')
tokenizer = AutoTokenizer.from_pretrained('gptech_tokenizer')

prompt = "crea un componente base en reactJS con un formik para login"

# Tokenizar el prompt
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# Generar texto utilizando el modelo
output = model.generate(input_ids, max_length=500, do_sample=True, temperature=0.7)

# Decodificar el texto generado
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)

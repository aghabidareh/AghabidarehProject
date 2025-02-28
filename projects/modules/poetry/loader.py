import os
from transformers import GPT2LMHeadModel, GPT2Tokenizer

"""
Loading the model and tokenizer to create the poem
using trained model and tokenizer
"""

current_directory = os.path.dirname(os.path.abspath(__file__))
model_name_directory = os.path.join(current_directory, 'gpt2-fa-poetry-finetuned')

model_name = model_name_directory
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

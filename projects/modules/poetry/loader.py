from transformers import GPT2LMHeadModel, GPT2Tokenizer

"""
Loading the model and tokenizer to create the poem
using trained model and tokenizer
"""

model_name = "projects/modules/poetry/gpt2-fa-poetry-finetuned"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "HooshvareLab/gpt2-fa-poetry"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_path = "projects\modules\poetry\gpt2-fa-poetry-finetuned"
model = GPT2LMHeadModel.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
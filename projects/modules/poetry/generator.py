from projects.modules.poetry.loader import *

def generator(input_text):
    model.eval()
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2, top_k=90,
                            top_p=0.95, temperature=0.9)
    generated_poem = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_poem.replace("<sep>" , '\n').replace('<|startoftext|>' , '')
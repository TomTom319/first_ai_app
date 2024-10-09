from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Set the model path to where it was downloaded
model_path = "/home/tom/.llama/checkpoints/Llama3.2-3B-Instruct"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

def generate_microcontent(input_text):
    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt")

    # Generate output (e.g., limit to 50 tokens)
    output = model.generate(**inputs, max_length=50)

    # Decode and return the output
    return tokenizer.decode(output[0], skip_special_tokens=True)


import json 
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from transformers import AutoTokenizer, AutoModelForCausalLM

app = Flask(__name__)
api = Api(app)

device = "cpu"
# load model and tokenizer
model_name_or_path = "ismaelfaro/gpt2-poems.en"

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model = AutoModelForCausalLM.from_pretrained(model_name_or_path)
model.to(device)

def generate_poem(input_text):
    input_text = input_text.replace("_", " ")
    input_ids = tokenizer.encode(input_text, return_tensors="pt").to(device)
    gen_ids = model.generate(
    input_ids, max_length=48, num_beams=100, no_repeat_ngram_size=2
    )
    generated = tokenizer.decode(gen_ids[0, :].tolist(), skip_special_tokens=True)
    return generated.replace("\\n", "<br/>").replace(";", "<br/>").replace(".", "<br/>")
 
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/<query_str>', methods=['GET'])
def update_record( query_str):
    print(query_str)
    return generate_poem(query_str)



if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80, debug=True)

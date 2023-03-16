import flask
import string
import random
import os
from example import load


app = flask.Flask(__name__)

# runs when app starts
gen_global = load(
	ckpt_dir = "../weights/7B",
	tokenizer_path = "../weights/tokenizer.model",
	max_seq_len = 512,
	max_batch_size = 32,
	use_int8 = True
	)


@app.route("/")
def hello():
	print("flask server is running", flush=True)
	return "flask server is running"

@app.route("/flask-inference/", methods = ["POST"])
def flask_inference_no_batching():

	global gen_global

	print("received POST request", flush=True)

	req_data = flask.request.json
	print("request data", req_data, flush=True) # for testing

	apikey, prompt = req_data["apikey"], req_data["prompt"]
	print(req_data["apikey"], req_data["prompt"], flush = True) # for testing

	prompts = [prompt]
	results = gen_global.generate(
		prompts,
		max_gen_len=1024,
        temperature=0.8,
        top_p=0.95,
        repetition_penalty_range=1024,
        repetition_penalty_slope=0,
        repetition_penalty=1.15, 
		)

	result = results[0]

	print("result from model: ", result)

	res_data = {
		"apikey": req_data["apikey"],
		"result": result
	}

	return flask.jsonify(res_data)

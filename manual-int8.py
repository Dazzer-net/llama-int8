from example import load

gen_global = load(
	ckpt_dir = "../weights/7B",
	tokenizer_path = "../weights/tokenizer.model",
	max_seq_len = 512,
	max_batch_size = 32,
	quantize = True
	)



while True:

	prompt = str(input())

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
	print(result)


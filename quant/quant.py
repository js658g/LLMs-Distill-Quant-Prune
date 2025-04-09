from transformers import AutoModelForCausalLM, AutoTokenizer
model_name = "EleutherAI/pythia-410m"
model = AutoModelForCausalLM.from_pretrained(model_name, 
low_cpu_mem_usage=True)
tokenizer = AutoTokenizer.from_pretrained(model_name)
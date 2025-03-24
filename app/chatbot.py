from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM
import torch

MODELS = {
    "dialo": {
        "name": "microsoft/DialoGPT-small",
        "tokenizer": None,
        "model": None
    },
    "flan": {
        "name": "google/flan-t5-base",
        "tokenizer": None,
        "model": None
    }
}

def load_models():
    for key in MODELS:
        print(f"Loading model: {MODELS[key]['name']}")
        MODELS[key]["tokenizer"] = AutoTokenizer.from_pretrained(MODELS[key]["name"])
        if key == "flan":
            MODELS[key]["model"] = AutoModelForSeq2SeqLM.from_pretrained(MODELS[key]["name"])
        else:
            MODELS[key]["model"] = AutoModelForCausalLM.from_pretrained(MODELS[key]["name"])

chat_histories = {
    "dialo": None,
    "flan": None  # 不保存 history
}

def generate_response(model_key, user_input):
    tokenizer = MODELS[model_key]["tokenizer"]
    model = MODELS[model_key]["model"]

    if model_key == "dialo":
        input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
        history = chat_histories["dialo"]
        bot_input_ids = torch.cat([history, input_ids], dim=-1) if history is not None else input_ids
        output_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        chat_histories["dialo"] = output_ids
        response = tokenizer.decode(output_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        return response
    else:  # flan
        inputs = tokenizer(user_input, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=100)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)

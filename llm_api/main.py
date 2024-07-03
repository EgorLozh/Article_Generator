from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


class LLM_Qwen05B:
    def __init__(self):
        self._device = "cuda" if torch.cuda.is_available else "cpu"
        self._model = AutoModelForCausalLM.from_pretrained(
            "Qwen/Qwen2-0.5B-Instruct",
            torch_dtype="auto",
            device_map="auto"
        )
        self._tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2-0.5B-Instruct")

    def get_request(self, prompt, system_contex="You are a helpful assistant."):
        messages = [
            {"role": "system", "content": system_contex},
            {"role": "user", "content": prompt}
        ]
        text = self._tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = self._tokenizer([text], return_tensors="pt").to(self._device)

        generated_ids = self._model.generate(
            model_inputs.input_ids,
            max_new_tokens=1024,

        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = self._tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

        return response


if __name__=="__main__":
    llm = LLM_Qwen05B()
    print(llm.get_request("Hi there, How are you"))

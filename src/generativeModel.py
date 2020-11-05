####################### IMPORT LIBRARIES #######################
from transformers import (
    MODEL_WITH_LM_HEAD_MAPPING,
    WEIGHTS_NAME,
    AdamW,
    AutoConfig,
    AutoModelForCausalLM,
    AutoTokenizer,
    PreTrainedModel,
    PreTrainedTokenizer,
    get_linear_schedule_with_warmup,
)

import torch

class GenerativeModel():
    def __init__(self):
        self.step = 0
        self.tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-medium')
        self.model = AutoModelForCausalLM.from_pretrained('microsoft/DialoGPT-medium')
    
    def add_to_history(self, utterance):
        """Tokenises the utterance and appends it to the chat history"""
        # encode the new user input, add the eos_token and return a tensor in Pytorch
        new_input_ids = self.tokenizer.encode(utterance + self.tokenizer.eos_token, return_tensors='pt')
        self.chat_history = torch.cat([self.chat_history, new_input_ids], dim=-1) if self.step > 0 else new_input_ids
        self.step += 1

    def get_response(self):
        modelResults = self.model.generate(
            self.chat_history, max_length=200,
            pad_token_id=self.tokenizer.eos_token_id,  
            no_repeat_ngram_size=3,       
            do_sample=True, 
            top_k=40, 
            top_p=0.7,
            temperature = 0.8
        )
        # pretty print last ouput tokens from bot
        response = "{}".format(self.tokenizer.decode(modelResults[:, self.chat_history.shape[-1]:][0], skip_special_tokens=True))
        self.chat_history = modelResults
        return response        

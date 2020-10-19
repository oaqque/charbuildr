####################### IMPORT LIBRARIES #######################
from transformers import (
    MODEL_WITH_LM_HEAD_MAPPING,
    WEIGHTS_NAME,
    AdamW,
    AutoConfig,
    AutoModelWithLMHead,
    AutoTokenizer,
    PreTrainedModel,
    PreTrainedTokenizer,
    get_linear_schedule_with_warmup,
)

import torch
from user_relationship import *

####################### Initialisations #######################

tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-small') # Grab pre-trained Tokenizer
model = AutoModelWithLMHead.from_pretrained('microsoft/DialoGPT-small') # Grab pre-trained Model

relationship_variability = 0.5
relationship = RelationshipScore(relationship_variability) # Initialise a user-relationship score 0

####################### Main Chat Loop #######################
for step in range(5):
    message = input("User: ")
    print("Relationship Score: " + str(round(relationship.update(message), 2)))
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizer.encode(message + tokenizer.eos_token, return_tensors='pt')

    
    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids
    # generated a response while limiting the total chat history to 1000 tokens, 
    chat_history_ids = model.generate(
        bot_input_ids, max_length=200,
        pad_token_id=tokenizer.eos_token_id,  
        no_repeat_ngram_size=3,       
        do_sample=True, 
        top_k=40, 
        top_p=0.7,
        temperature = 0.8
    )
    
    # pretty print last ouput tokens from bot
    response = "{}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True))
    print("ConvAI: " + response)
    print("Relationship Score: " + str(round(relationship.update(response), 2)))

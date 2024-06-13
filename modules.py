import streamlit as st
import pandas as pd
import numpy as np
import json
import time
import requests
from datetime import datetime

import random



def query_model_json(input_string, max_new_tokens=1000, temperature=0.7, top_p=0.9, top_k=0, repetition_penalty=1,
                stop=None, num_responses=1, presence_penalty=0, frequency_penalty=0, webhook=None, stream=False):
    input_string
    url = "https://api.deepinfra.com/v1/inference/mistralai/Mixtral-8x7B-Instruct-v0.1"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer M4pvFvYNC4og6aZkRYdvHUJdxuOOBoBL"
    }
    data = {
        "input": input_string,
        "max_new_tokens": max_new_tokens,
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k,
        "repetition_penalty": repetition_penalty,
        "num_responses": num_responses,
        "presence_penalty": presence_penalty,
        "frequency_penalty": frequency_penalty,
        "stream": stream,
        "response_format" : {"type":"json_object"}
    }
    if webhook:
        data["webhook"] = webhook
    if stop:
        data["stop"] = stop

    response = requests.post(url, headers=headers, json=data)
    # print("___________________")
    # print(response.json())
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.text)
        return None
    

def query_model_withoutjson(input_string, max_new_tokens=200, temperature=0.7, top_p=0.9, top_k=0, repetition_penalty=1,
                stop=None, num_responses=1, presence_penalty=0, frequency_penalty=0, webhook=None, stream=False):
    input_string
    url = "https://api.deepinfra.com/v1/inference/mistralai/Mixtral-8x7B-Instruct-v0.1"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer M4pvFvYNC4og6aZkRYdvHUJdxuOOBoBL"
    }
    data = {
        "input": input_string,
        "max_new_tokens": max_new_tokens,
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k,
        "repetition_penalty": repetition_penalty,
        "num_responses": num_responses,
        "presence_penalty": presence_penalty,
        "frequency_penalty": frequency_penalty,
        "stream": stream,
        # "response_format" : {"type":"json_object"}
    }
    if webhook:
        data["webhook"] = webhook
    if stop:
        data["stop"] = stop

    response = requests.post(url, headers=headers, json=data)
    # print("___________________")
    # print(response.json())
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.text)
        return None
    



def summerize(idea_history):

    system_prompt  = 'Act as an AI summarizer and condense all the ideas into a single paragraph under 100 words.'
    user_prompt = f' list of ideas -: {idea_history}'

    input_string = f"[INST] <<SYS>>\n{system_prompt}\n<<SYS>>\n{user_prompt} [/INST]"
    response = query_model_withoutjson(input_string)
    output =response['results'][0]['generated_text']
    token_genrated = response['inference_status']['tokens_generated']
    token_input = response['inference_status']['tokens_input']
    response_time = response['inference_status']['runtime_ms']
    cost = response['inference_status']['cost']
    

    return output,token_genrated,token_input,response_time,cost


# def ideagen(company_profile,summary):

#     system_prompt = "I want you to act as a social media strategist specializing in Social media  engagement and content creation. My first request is to generate ideas for social media that are concise, engaging, and tailored to the target audience and Brand Vision."

#     user_prompt = f"""

#     {company_profile}

#    Strictly follow this output format:
# - "Narrative Idea Title": "Narrative idea description (under 25 words)"

#     ### Sample JSON Output
#     {{
#         "Redefining Beauty: Embracing Your Uniqueness": "Celebrate diverse beauty, emphasizing self-acceptance and sharing tips on embracing personal features and imperfections."
#     }}

#     I need you to write content with a good balance of “perplexity” and “burstiness”.

#     ### Ideas History Summary:
#     {summary}

#     ### Strict Rules

#     1) Generate exactly 5 ideas.
#     2) Ensure the ideas are distinct from those in the history summary.


#     """

   




#     input_string = f"[INST] <<SYS>>\n{system_prompt}\n<<SYS>>\n{user_prompt} [/INST]"
#     response = query_model_json(input_string)
#     output =response['results'][0]['generated_text']
#     token_genrated = response['inference_status']['tokens_generated']
#     token_input = response['inference_status']['tokens_input']
#     response_time = response['inference_status']['runtime_ms']
#     cost = response['inference_status']['cost']
#     json_object = json.loads(output)
    

#     return json_object,token_genrated,token_input,response_time,cost





def ideagen(company_profile,summary):

    system_prompt = "I want you to act as a social media strategist specializing in Social media  engagement and content creation. My first request is to generate ideas for social media that are concise, engaging, and tailored to the target audience and Brand Vision."

    user_prompt = f"""

    {company_profile}

   Strictly follow this output format:
   Output Format:

"Working Title": "A clear, concise, and engaging title that summarizes the main topic or focus of the content."
"Target Audience": "A specific description of the intended audience for the content, including their interests, demographics, and pain points."
"Short Key Message": "A brief statement that encapsulates the main takeaway or purpose of the content."

    ### Sample JSON Output
    {{
            "Content Idea 1": {{
        "Working Title": "Family Fun at the Farm: U-Pick Your Own Adventure",
        "Target Audience": "Families with young children looking for outdoor activities and a chance to connect with nature.",
        "Short Key Message": "Create lasting memories while harvesting your own fresh produce at our family-friendly U-pick farm."
    }}



    }}

    I need you to write content with a good balance of “perplexity” and “burstiness”.

    ### Ideas History Summary:
    {summary}

    ### Strict Rules

    1) Generate exactly 5 ideas.
    2) Ensure the ideas are distinct from those in the history summary.


    """

   




    input_string = f"[INST] <<SYS>>\n{system_prompt}\n<<SYS>>\n{user_prompt} [/INST]"
    response = query_model_json(input_string)
    output =response['results'][0]['generated_text']
    token_genrated = response['inference_status']['tokens_generated']
    token_input = response['inference_status']['tokens_input']
    response_time = response['inference_status']['runtime_ms']
    cost = response['inference_status']['cost']
    json_object = json.loads(output)
    

    return json_object,token_genrated,token_input,response_time,cost




def script(narrative,post_structure,social_channel,goal,post_type,target_Audience,short_key_message,error):

    system_prompt = f"""
           
            Role: Movie Director. Provide strategic advice for creating content on specific social media channels. The guidance should help the user develop their content by focusing on strategic and creative aspects.

            Input Parameters:

            Narrative : The central theme or storyline for the content is : {narrative}. Validates if the narrative is coherent and suitable for social media.
            Social Channel : The intended social media platform {social_channel}. Tailors advice to the platform's specific features and audience demographics.
            Post Type : The content format type is {post_type}. Checks if the post type is appropriate for both the narrative and the platform.
            Goal : The main objective of the post is to {goal}. Ensures the goal is clearly defined and aligns with the narrative and post type.
            Target Audience : A specific description of the intended audience is {target_Audience}. Validates that the target audience is clear and suitable for the content.
            Short Key Message : A concise message that the content aims to communicate is {short_key_message}. Validates that the message is compelling and aligns with the narrative and audience.
        
            
            
            ### Error Handling output Format:
            {error}

            

            ### Output Format 

            
            {post_structure}

            
            

            ### Rules
            1. output should be only json, no extra content .
            2. strictly follow output format.
            3. strictly follow error handling format.
            4. Before proceeding with the guidance, the system validates each parameter. If one or more parameters are found to be illogical, missing, or inappropriate, the system generates a JSON response detailing errors for each problematic parameter

            """


        
    
    input_string = f"[INST] <<SYS>>\n{system_prompt}\n<<SYS>>[/INST]"
    
    print("input______   ", input_string)
    response = query_model_json(input_string)
    
    token_genrated = response['inference_status']['tokens_generated']
    token_input = response['inference_status']['tokens_input']
    response_time = response['inference_status']['runtime_ms']
    cost = response['inference_status']['cost']
    try:
        output = json.loads(response['results'][0]['generated_text'])
    except:
        output  =  {
            "errors": [
                {
                "parameter": "Unclear Narative Idea",
                "message": "give a correct and understandable logical ideas or according to the comunity guidelines"
                }
            ] 
        }
    return output,token_genrated,token_input,response_time,cost




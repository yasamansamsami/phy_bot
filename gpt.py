import openai
import json

openai.api_key = ""


def add_json(data):
    with open("log.json", mode="r") as file:
        messeges = json.load(file)
    messeges.append(data)
    with open("log.json", mode="w") as file:
        json.dump(messeges, file)


def chatgpt_response(prompt):
    add_json({"role": "user", "content": prompt})
    with open("log.json", mode="r") as file:
        json_messeges = json.load(file)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=json_messeges,
        temperature=0.5,
        max_tokens=100
    )
    prompt_response = response['choices'][0]['message']['content']
    add_json(response['choices'][0]['message'])
    return prompt_response

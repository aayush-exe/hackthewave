import os

import openai
openai.api_key = "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"

user_input = input("Talk to the waifu!: ")
completion_input = user_input + " There should be 3 sections: a response,  an 'Ingredients:' section, and a short 'Instuctions:' section." \
                                "Seperate each section with two enter statements. "
chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":
    completion_input}])
content = chat_completion['choices'][0]['message']['content']
sections = content.split("\n\n")
anime_response = sections[0]
ingredients = sections[1]
instructions = sections[2]

anime_text = user_input + " Make it anime style, aesthetic, and with no text."
response = openai.Image.create(prompt=anime_text, n=1, size="1024x1024")
image_url = response['data'][0]['url']


# Print the content
print(anime_response)
print(ingredients)
print(instructions)
print(image_url)



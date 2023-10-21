import openai
#import anvil.server
#anvil.server.connect("server_G2CT33LWBAYSXBZEJY57QWW6-DK36JKLLPLGZLZCW")
openai.api_key = "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"

#completion_input = prompt + " There should be 3 sections: a response,  an 'Ingredients:' section, and a short 'Instuctions:' section." \
                                #"Seperate each section with two enter statements. "
#@anvil.server.callable
def get_text(prommpt):
    completion_input = prommpt + " There should be 3 sections: a response,  an 'Ingredients:' section, and a short 'Instuctions:' section." \
                                "Seperate each section with two enter statements. "
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":
    completion_input}])
    content = chat_completion['choices'][0]['message']['content']
    return content

get_text("Give me a steak recipe")
'''anime_text = user_input + " and make the art style similar to My Hero Academia. Have no text in the photo. Make the photo aesthetically pleasing. Make the colors pastel."
response = openai.Image.create(prompt=anime_text, n=1, size="1024x1024")
image_url = response['data'][0]['url']


# Print the content
print(anime_response)
print(ingredients)
print(instructions)
print(image_url)'''

#anvil.server.wait_forever()



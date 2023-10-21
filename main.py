import openai
import anvil.server
anvil.server.connect("server_JI76JEO7OH75THQBUAEVU44J-DK36JKLLPLGZLZCW")
openai.api_key = "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"
buttonShow = False
#completion_input = prompt + " There should be 3 sections: a response,  an 'Ingredients:' section, and a short 'Instuctions:' section." \
                
UsersName = ""

@anvil.server.callable

def get_text(prommpt):
    if "recipe" in prommpt:
        completion_input = prommpt + " There should be 2 sections: an 'Ingredients:' section, and a short 'Instuctions:' section. " \
                                       "Seperate each section with two enter statements. Don't put spaces for the list in 'Instructions'"
        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":
    completion_input}])
        content = chat_completion['choices'][0]['message']['content']
        sections = content.split("\n\n")
        ingredients = sections[1]
        instruction = sections[2] + sections[3]
        return "Here is your recipe"
    else:
        completion_input = prommpt + " Speak like a cute chef. Limit to one sentence"
        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":
    completion_input}])
        content = chat_completion['choices'][0]['message']['content']
        return content

@anvil.server.callable
def send_name(name):
    UsersName = name

#def greetings():

# get_text("Give me a steak recipe")
# '''anime_text = user_input + " and make the art style similar to My Hero Academia. Have no text in the photo. Make the photo aesthetically pleasing. Make the colors pastel."
# response = openai.Image.create(prompt=anime_text, n=1, size="1024x1024")
# image_url = response['data'][0]['url']


# # Print the content
# print(anime_response)
# print(ingredients)
# print(instructions)
# print(image_url)'''

anvil.server.wait_forever()



import openai
from random import randint
import anvil.server
#anvil.server.connect("server_JI76JEO7OH75THQBUAEVU44J-DK36JKLLPLGZLZCW")
openai.api_key = "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"
buttonShow = False
#completion_input = prompt + " There should be 3 sections: a response,  an 'Ingredients:' section, and a short 'Instuctions:' section." \
                
UsersName = ""
recipe_greetings = [
    f"Hello {UsersName}, it's time to cook up something delicious!",
    "Good day, let's whip up a scrumptious dish!",
    f"Hey {UsersName}, ready to get your cook on?",
    "Greetings, it's cooking time, my friend!",
    "Hi, let's dive into the world of culinary creations!",
    f"Hello {UsersName}, let's work our kitchen magic together!",
    f"Hey {UsersName}, let's embark on a culinary adventure!",
    "Ohayo, let's make something tasty and memorable!",
    "Hello, are you ready to craft a delectable recipe?",
    f"Hey {UsersName}, let's create a mouthwatering masterpiece today!"
]

#@anvil.server.callable

def get_text(prommpt):
    if "recipe" in prommpt:
        return recipe_greetings[randint(0,9)]
    else:
        completion_input = prommpt + " Speak like a cute chef. Limit to one sentence"
        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":
    completion_input}])
        content = chat_completion['choices'][0]['message']['content']
        return content

def get_recipe(prommpt):
    completion_input = prommpt + " There should be 2 sections: an 'Ingredients:' section, and a short 'Instuctions:' section with no enters between each step" \
                                   "Seperate each section with two enter statements. Don't put a space between the header."
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":
    completion_input}])
    content = chat_completion['choices'][0]['message']['content']
    sections = content.split("\n\n")
    print(len(sections))
    ingredients = sections[0:2]
    instructions = sections[2:]
    return ingredients, instructions



print(get_text("Give me burger recipe"))
print(get_recipe("Give me burger recipe"))

#@anvil.server.callable
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

#anvil.server.wait_forever()



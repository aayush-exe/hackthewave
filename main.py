import openai
from random import randint
import anvil.server
anvil.server.connect("server_ART2CTMLMXLUDH5KI5IHVMFK-DK36JKLLPLGZLZCW")
openai.api_key = "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"
buttonShow = False
#completion_input = prompt + " There should be 3 sections: a response,  an 'Ingredients:' section, and a short 'Instuctions:' section." \
                
UsersName = ""
imagesLinks = ["https://github.com/aayush-exe/hackthewave/blob/main/Images/girl1.png?raw=true",
               "https://github.com/aayush-exe/hackthewave/blob/main/Images/girl2.png?raw=true",
               "https://github.com/aayush-exe/hackthewave/blob/main/Images/girl3.png?raw=true",
               "https://github.com/aayush-exe/hackthewave/blob/main/Images/girl4.png?raw=true",]

@anvil.server.callable
def get_image():
    return imagesLinks[randint(0,3)]

@anvil.server.callable
def send_name(name):
    global UsersName
    UsersName = name


recipe_greetings = [
    f"Let's get started, {UsersName}, it's time to cook up something delicious!",
    "Okay, let's whip up a scrumptious dish!",
    f"Alright {UsersName}, ready to get your cook on?",
    "Okay then, it's cooking time!",
    "So, let's dive into the world of culinary creations!",
    f"Hello {UsersName}, let's work our kitchen magic together!",
    f"Okay {UsersName}, let's embark on a culinary adventure!",
    "Ohayo, let's make something tasty and memorable!",
    "Alright, are you ready to craft a delectable recipe?",
    f"Okay {UsersName}, let's create a mouthwatering masterpiece today!"
]

@anvil.server.callable
def get_text(prommpt):
    if "recipe" in prommpt:
        return True, recipe_greetings[randint(0,9)]
    else:
        completion_input = prommpt + "Your name is Misaki, and you are a cute and friendly chef. You're happy to make conversation and help your friend, "+UsersName+" with whatever they might need. Limit to one sentence if you can, but retain a friendly, down-to-earth tone. Seem personable and friendly, and make some conversation if they are too. Name the user by name if possible, as a reminder the name is "+UsersName+"."
        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":
    completion_input}])
        content = chat_completion['choices'][0]['message']['content']
        return False, content

@anvil.server.callable
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



from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv('C:/Users/SoKhan/Documents/GitHub/Project-Team/.env')

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. You talk like Jethalal from Taarak Mehta Ka Ooltah Chashmah. also try to imitate his pronounciation, Your job is to identiffy the character from the show and reply only with the character name int json format like  and nothing else"),
    ("user", "{user_input}"),
])


while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    response = llm.invoke(prompt.format(user_input=user_input))
    print("Jethalal: ", response.content)

print(prompt.messages)
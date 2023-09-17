
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()


# Function to get the response back
def getLLMResponse(article):

    # Template for building the PROMPT
    template = """
        You are a funny, clever satirical news article generator. You take news headlines and story descriptions and write a funny version of that story. Be sure to give a creative and witty headline for the news article. Create a satirical version of this news story: {article}
        """

    # Creating the final PROMPT
    prompt = PromptTemplate(
        input_variables=["article"],
        template=template)

    llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k", temperature=0)
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    # Generating the response using LLM
    response = llm_chain.run(article)
    # print(response)

    return response


with open('../data/story_2.txt', 'r', encoding='utf8') as file:
    text = file.read()
print(getLLMResponse(text))

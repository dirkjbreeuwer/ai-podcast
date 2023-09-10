"""Summarizes and article using GPT4 and returns a summary of the article."""
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains.llm import LLMChain
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate

load_dotenv()

class Summarizer:
    """Summarizes and article using GPT4 and returns a summary of the article."""

    def __init__(self, article):
        """Initialize the Summarizer class."""
        self.article = article
        self.llm = ChatOpenAI(temperature=0, model_name="gpt-4-0613") # checked
        self.prompt_template = """Extract 5 facts from this article: \n "{article}" \n 5 facts:"""
        self.prompt = PromptTemplate.from_template(self.prompt_template)
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def summarize(self):
        """Summarize the article."""
        return self.chain.run(self.article)

if __name__ == "__main__":
    article = """
    The United States is a country in the Western Hemisphere. It consists of 50 states, a federal district, five major self-governing territories, and various possessions. At 3.8 million square miles, it is the world's third- or fourth-largest country by total area. With a population of over 328 million, it is the third most populous country in the world. The national capital is Washington, D.C., and the most populous city is New York City.
    Paleo-Indians migrated from Siberia to the North American mainland at least 12,000 years ago, and European colonization began in the 16th century. The United States emerged from the thirteen British colonies established along the East Coast. Numerous disputes between Great Britain and the colonies led to the American Revolutionary War lasting between 1775 and 1783, leading to independence. The United States embarked on a vigorous expansion across North America throughout the 19th century, acquiring new territories, displacing Native American tribes, and gradually admitting new states until it spanned the continent by 1848.
    Even though the United States is the world's third- or fourth-largest country by total area, it is the world's third-most populous country. The capital is Washington, D.C., and the most populous city is New York City. Forty-eight states and the capital's federal district are contiguous in North America between Canada and Mexico. The State of Alaska is in the northwest corner of North America, bordered by Canada to the east and across the Bering Strait from Russia to the west. The State of Hawaii is an archipelago in the mid-Pacific Ocean. The U.S. territories are scattered about the Pacific Ocean and the Caribbean Sea, stretching across nine official time zones. The extremely diverse geography, climate, and wildlife of the United States make it one of the world's 17 megadiverse countries.
    Finnally the United States is a developed country and has the world's largest economy by nominal and real GDP, benefiting from an abundance of natural resources and high worker productivity. While the U.S. economy is considered post-industrial, it continues to be one of the world's largest manufacturers. Accounting for 39% of global military spending and 25% of world GDP, it is the world's foremost military and economic power, a prominent political and cultural force, and a leader in scientific research and technological innovations.
    """
    summarizer = Summarizer(article)
    print(summarizer.summarize())

import os
import openai
from dotenv import find_dotenv, load_dotenv
import time
import logging
from datetime import datetime

load_dotenv()
#you can also initialize the client like this client = openai.OpenAI() (only if key is named OPENAI_API_KEY)
openai.api_key = os.environ.get("OPENAI_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")
model = "gpt-4"
client = openai.OpenAI()



# ==================================
# =====create the assistant ========
# ==================================

def main():
    

    

    def get_news(topic):
        url = f"https://newsapi.org/v2/everything?q={topic}&from=2024-03-09&sortBy=publishedAt&apiKey={news_api_key}&pageSizes=5"













if __name__ == "__main__":
    main()
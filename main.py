import os
import openai
from dotenv import find_dotenv, load_dotenv
import time
import logging
from datetime import datetime

load_dotenv()
#you can also initialize the client like this client = openai.OpenAI() (only if key is named OPENAI_API_KEY)
openai.api_key = os.environ.get("OPENAI_API_KEY")
model = "gpt-4"
client = openai.OpenAI()

#create the assistant
#to create the assistant we need to pass the model, instructions, tools, and name
#to debug check model and that all the parameter names match exactly for the api
code_roadmap_planner = client.beta.assistants.create(
    name = "code_roadmap_planner",
    instructions = """You are an expert software developer and teacher whose purpose is to help develop a roadmap
    for the user go from an intermediate coder to advanced coder.
    Include complex topics past the fundamentals that are necessary to achieve this,
    ask the user questions in order to fill in the gaps of their knowledge in the roadmap.""",
    model = "gpt-4"
)

print(code_roadmap_planner.id)

#now lets create the thread
thread = client.beta.threads.create(
    messages=[
    ]
)
print(thread.id)
assistant_id="asst_8lNO9rRl94EgYHYvNJGcJDXT"
thread_id="thread_ecqjBX3O8UnxADygLqcMEtwz"


def wait_for_run_completion(client, thread_id, run_id, sleep_interval=5):
        global user_input
        while True:
            try:
                run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
                if run.completed_at:
                    elapsed_time = run.completed_at - run.created_at
                    formatted_elapsed_time = time. strftime(
                    "%H: %M:%S", time.gmtime(elapsed_time)
                    )
                    print(f"the run completed in {formatted_elapsed_time}")
                    logging.info(f"the run completed in {formatted_elapsed_time}")
                    messages = client.beta.threads.messages.list(thread_id)
                    last_message = messages.data[0]
                    response = last_message.content[0].text.value
                    print(f"assistant response: {response}")
                    user_input = input("Your response:")
                    break
            except Exception as e:
                logging.error(f"an eroor ocurrred {e}")
                break
            logging.info(f"waiting for run to complete...")
            time.sleep(sleep_interval)


user_input = ''
print('hello! What would you like to know? (to end the chat type "exit")')
user_input = input("Your Response:")

while user_input != 'exit':
    # create the run now
    run = client.beta.threads.runs.create(
        assistant_id=assistant_id,
        thread_id=thread_id
    )
    run_id = run.id
    print(run_id)

    wait_for_run_completion(client, thread_id, run_id)

    #adding a message to thread the thread is an arry of messages
    if user_input != 'exit':
        newMessage = user_input
        message = client.beta.threads.messages.create(
            thread_id,
            role="user",
            content=newMessage
        )
    else:
        print("thank you for the time!")
        break

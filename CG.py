import openai
import time

# set up the API key
openai.api_key = "<your API key>"

# define the prompt to send to the GPT-3 API
prompt = "Hello, GPT-3!"

# define the parameters for the API request
model_engine = "text-davinci-002"
temperature = 0.5
max_tokens = 50

# send the prompt to the GPT-3 API and get a response
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens
)

# wait for the response to be generated
while response["status"] != "completed":
    response = openai.Completion.fetch(response["id"])
    time.sleep(1)

# get the completed response and print it
output_text = response["choices"][0]["text"]
print(output_text)
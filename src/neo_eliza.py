import openai
import sys

def neo_eliza():   
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit']:
            sys.exit(0)
        
        try:
            response = openai.Completion.create(
                model="gpt-4",
                prompt=user_input,
                max_tokens=32000 
            )
            print(f"Neo-Eliza: {response.choices[0].text.strip()}")
        except openai.error.OpenAIError as e:
            if 'authentication' in str(e).lower():
                print("Error: Invalid API key.")
                get_api_key()
            else:
                print(f"An error occurred: {e}")

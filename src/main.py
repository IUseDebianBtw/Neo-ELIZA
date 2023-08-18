import openai
import sys

print(open('src/ascii_art.txt').read())

def get_api_key():
    while True:  
        openai.api_key = input("Please enter your OpenAI API key (or type 'q'/'quit' to exit): ")

        if openai.api_key.lower() in ['q', 'quit']:
            sys.exit(0)
        
        try:
            response = openai.Completion.create(
                model="gpt-4",
                prompt="test",
                max_tokens=5
            )
            break  
        except openai.error.OpenAIError as e:
            if 'authentication' in str(e).lower():
                print("Error: Invalid API key. Please enter a valid key.")
            else:
                print(f"An error occurred: {e}")


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

if __name__ == "__main__":
    get_api_key()  
    neo_eliza()

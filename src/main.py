import openai
import sys

# Initialize OpenAI API
openai.api_key = 'YOUR_OPENAI_API_KEY'

def neo_eliza():
    print("Neo-Eliza: Hello! I'm Neo-Eliza. Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        
        # Allow the user to exit the chat
        if user_input.lower() in ['exit', 'quit']:
            print("Neo-Eliza: Goodbye!")
            sys.exit(0)
        
        # Fetching the response from ChatGPT
        response = openai.Completion.create(
            model="text-davinci-002",  # Choose the model you prefer
            prompt=user_input,
            max_tokens=150  # You can adjust this value as needed
        )
        
        print(f"Neo-Eliza: {response.choices[0].text.strip()}")

if __name__ == "__main__":
    neo_eliza()

import openai
import sys
from neo_eliza import neo_eliza
from get_api_key import get_api_key

print(open('src/ascii_art.txt').read())

if __name__ == "__main__":
    get_api_key()  
    neo_eliza()

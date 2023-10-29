import pwd
import os
import subprocess
from neo_eliza import neo_eliza
from get_api_key import get_api_key

def main():
    try:
        print(open('ascii_art.txt').read())
        
        get_api_key()
        neo_eliza()

    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting gracefully.")
        exit(0)


if __name__ == "__main__":
    main()

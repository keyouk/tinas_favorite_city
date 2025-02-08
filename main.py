from openai import OpenAI
import argparse
from sessions import create_session


def main():
    parser = argparse.ArgumentParser(description="Process user input.")
    parser.add_argument("-m", "--message", type=str, help="Enter a message")
    args = parser.parse_args()

    message = args.message
    create_session(message)

if __name__ == "__main__":
    main()
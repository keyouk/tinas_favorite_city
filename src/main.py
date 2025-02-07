from openai import OpenAI
import argparse
from sessions import create_session



parser = argparse.ArgumentParser(description="Initalize GPT Assistant")
parser.add_argument("assistant_name", help="The name of the assistant.")
parser.add_argument("-f", "--file", help="File name to use", required=False)
args = parser.parse_args()


assistant_name = args.assistant_name
file_name = args.file


create_session(assistant_name, file_name)



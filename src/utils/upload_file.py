import argparse
from openai import OpenAI


parser = argparse.ArgumentParser(description="Upload File to OpenAI and receive FileID")
parser.add_argument("file_name", help="The name of the file.")
args = parser.parse_args()


client = OpenAI()
file_name = args.file_name



def upload_file_to_openAI(file_name):
    data = client.files.create(
        file=open(file_name, "rb"),
        purpose="assistants"
        )
    print(f"\n{data}")
    print(f"\n\nFileID: {data.id}\n\n")
    return data




if __name__ == '__main__':
	upload_file_to_openAI(file_name)
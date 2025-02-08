from openai import OpenAI
import json



def create_assistant(parameters):
    client = OpenAI()
    assistant = client.beta.assistants.create(
        name = parameters["assistant_name"],
        model = parameters["model"],
        tools = parameters["tools"],
        top_p = parameters["top_p"],
        temperature = parameters["temperature"]
        )
    print(f'created {assistant.id}')
    return assistant



def list_assistants(client):
    assistants = client.beta.assistants.list(
        order="desc",
        limit="20",
    )
    return {assistant.name: assistant for assistant in assistants}



def upload_file(client, file_name):
    data = client.files.create(
        file=open(file_name, "rb"),
        purpose="assistants"
        )
    return (data)


def log_session_parameters(parameters,thread_id,run_id,assistant_id):
    data = {
        "thread_id":thread_id,
        "assistant_id":assistant_id,
        "run_id": run_id,
        "max_prompt_tokens":parameters["max_prompt_tokens"],
        "max_completion_tokens":parameters["max_completion_tokens"],
        "temperature":parameters["temperature"],
        "top_p":parameters["top_p"],
    }
    with open("previous_session.json", "w") as file:
        json.dump(data, file, indent=4)
    return 


def load_json_file(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            if not isinstance(data, dict):
                print(f"Error: {filename} does not contain a valid JSON object.")
                return {}  
            return data
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return {}  
    except json.JSONDecodeError:
        print(f"Error: {filename} contains invalid JSON.")
        return {}  

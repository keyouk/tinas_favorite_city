
from openai import OpenAI
from dataclasses import dataclass, field, asdict
import json



@dataclass
class Config:
    name: str = ""
    model: str = "gpt-4o"
    description: str = ""
    instructions: str = ""
    tools: list = field(default_factory=lambda: [{"type": "code_interpreter"}])
    tool_resources: dict = field(default_factory=lambda: {
        "code_interpreter": {"file_ids": []}
    })
    temperature: float = 0.5
    top_p: float = 1.0
    response_format: str = "auto"



def create_assistant(assistant_name, client):
    assistant_config = Config(name=assistant_name)
    assistant_dict = asdict(assistant_config)
    assistant = client.beta.assistants.create(**assistant_dict)
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


def load_json_file(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            if not isinstance(data, dict):
                print(f"Error: {filename} does not contain a valid JSON object.")
                return {}  # Ensure it returns an empty dictionary, not None
            return data
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return {}  # Ensure it returns an empty dictionary
    except json.JSONDecodeError:
        print(f"Error: {filename} contains invalid JSON.")
        return {}  # Ensure it returns an empty dictionary
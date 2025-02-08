
from openai import OpenAI
from assistant_utils import create_assistant, list_assistants, upload_file, load_json_file, log_session_parameters
from typing_extensions import override
from openai import AssistantEventHandler
import time
import json


client = OpenAI()


def create_session():
	parameters = load_json_file("config/parameters.json")
	print(parameters)

	assistant_name = parameters["assistant_name"]
	my_assistants = list_assistants(client)
	if assistant_name not in my_assistants:
		try:
			print(f"Could not find assistant, creating new assistant")
			assistant = create_assistant(parameters)
			create_session(assistant_name, file_name)
		except Exception as e:
			print(f"An Error Occurred: {e}")
	else:
		assistant = my_assistants[assistant_name]
	
	try:
		thread = client.beta.threads.create(
			)
		message = client.beta.threads.messages.create(
			thread_id=thread.id,
			role="user",
			content="what is Tina Escobar's Favorite City"
			)

		run = client.beta.threads.runs.create_and_poll(
			thread_id=thread.id,
			assistant_id=assistant.id,
			max_completion_tokens=parameters["max_completion_tokens"],
			max_prompt_tokens=parameters["max_prompt_tokens"],
			temperature=parameters["temperature"],
			top_p=parameters["top_p"],
			instructions=parameters["instructions"]
			)
		log_session_parameters(parameters, thread.id, run.id, assistant.id)
		if run.status == 'completed': 
			messages = client.beta.threads.messages.list(
				thread_id=thread.id,
				)
			print(f"\n {run}")

			for message in messages:
				print(f"\n {message.content[0].text.value}")
		else:
			print(run.status)

	except Exception as e:
		print(f"An error has occurred: {e}")



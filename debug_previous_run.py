from openai import OpenAI
import json



filename = "previous_session.json"


try:
    with open(filename, "r") as file:
        previous_session_data = json.load(file)
        print(previous_session_data)
except Exception as e:
	print(f"JSON Error was found {e}")



client = OpenAI()
runs = client.beta.threads.runs.steps.list(
	thread_id=previous_session_data["thread_id"],
	run_id=previous_session_data["run_id"]
	)


completion_tokens=0
run_steps=0
for run in runs:
	run_steps+=1
	completion_tokens+=run.usage.total_tokens
	print(f"\nrunstep: \n{run.step_details}")


print(f"\n\n\n-------------------------------------------")
print(f"-------------------------------------------")
print(f"Amount of Run Steps: {run_steps}")
print(f"Temperature: {previous_session_data['temperature']}")
print(f"Top_p: {previous_session_data['top_p']}")
print(f"Max Prompt Tokens: {previous_session_data['max_prompt_tokens']}")
print(f"Max Completion Tokens: {previous_session_data['max_completion_tokens']}")
print(f"Total Run Completion Tokens {completion_tokens}")
print(f"\n\n\n-------------------------------------------")
print(f"-------------------------------------------")
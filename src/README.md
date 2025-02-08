# Tina's Favorite City Debugger

A debugging tool to analyze and optimize responses from OpenAI's Assistants API, specifically focusing on **truncated responses from Code Interpreter**.

---

## Setup & Installation

### 1. Install Dependencies
Run the following command to install required packages:
```sh
pip3 install -r requirements.txt
```

### 2. Set Your OpenAI API Key
Export your API key as an environment variable:
```sh
export OPENAI_API_KEY={YOUR_API_KEY}
```
### 3. Manually upload FileID prior to first run:

Copy this file_id for next step
```sh
python3 /utils/upload_file.py data/tse_takehome_dataset
```
### 3. Set up Config File in /config/parameters.json
---
```sh
{
	"assistant_name": {assistant_name}, 
	"max_prompt_tokens":10000,
	"max_completion_tokens": 10000,
	"temperature":0.1, # value between .01 - 1
	"top_p":0.1,       # value between .01 - 1
	"instructions":"", 
	"file_id":{file_id}, #string 
	"tools":[{"type": "code_interpreter"}],
	"model":"gpt-4o",
	"reasoning_effort":"medium" # reasoning effort low, medium, high
}
```

## 4. Running the Code
Before you start, you will need to upload the file data manually first and grab the FileID:
```sh
python3 /utils/upload_file.py data/tse_takehome_dataset
```

Afterwards, you can start executing the prompt. 
```sh
python3 main.py {prompt}
```
 **Note:** This will execute a new assistant run and log configurations.

---

## 5. Debugging the Last Execution
The debugger analyzes **the last execution stored in `previous_session.json`**.

To run the debugger:
```sh
python3 debug/debug_previous_run.py
```
🔹 This will load **the most recent assistant run**, extract logs, and display potential reasons for truncation.

---

## 6. Logs & Debugging Output
- **Session Logs:** Stored in `previous_session.json`
- **Run Configurations:** Includes parameters like `max_completion_tokens`, `top_p`, and truncation strategy.
- **Debugger Insights:** Helps identify causes of response truncation.

---

## 7. Troubleshooting
If the assistant's responses seem **truncated**, check:
- `max_completion_tokens` and `max_prompt_tokens` in `previous_session.json`
- The number of **run steps** used
- Whether **instructions** were provided in the assistant or run configuration

---

## 8. Additional Resources
- [OpenAI Assistants API](https://platform.openai.com/docs/assistants)
- [Understanding Token Limits](https://platform.openai.com/docs/concepts#tokens)
- [Debugging Assistants API](https://platform.openai.com/docs/assistants/deep-dive#debugging)

---

### 9. Need Help?
For any issues or improvements, feel free to open an **[issue](https://github.com/keyouk/tinas_favorite_city/issues)** or submit a **pull request**. 🚀





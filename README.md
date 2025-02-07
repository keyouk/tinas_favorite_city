# 🎯 Tina's Favorite City Debugger

A debugging tool to analyze and optimize responses from OpenAI's Assistants API, specifically focusing on **truncated responses from Code Interpreter**.

---

## 🚀 Setup & Installation

### 1️⃣ Install Dependencies
Run the following command to install required packages:
```sh
pip3 install -r requirements.txt
```

### 2️⃣ Set Your OpenAI API Key
Export your API key as an environment variable:
```sh
export OPENAI_API_KEY={YOUR_API_KEY}
```

---

## ▶️ Running the Code
To start a new session with a given assistant name and file input, run:
```sh
python3 main.py {assistant_name} -f tse_takehome_dataset.csv
```
📌 **Note:** This will execute a new assistant run and log configurations.

---

## 🐞 Debugging the Last Execution
The debugger analyzes **the last execution stored in `previous_session.json`**.

To run the debugger:
```sh
python3 debug_previous_run.py
```
🔹 This will load **the most recent assistant run**, extract logs, and display potential reasons for truncation.

---

## 📂 Logs & Debugging Output
- **Session Logs:** Stored in `previous_session.json`
- **Run Configurations:** Includes parameters like `max_completion_tokens`, `top_p`, and truncation strategy.
- **Debugger Insights:** Helps identify causes of response truncation.

---

## 🛠️ Troubleshooting
If the assistant's responses seem **truncated**, check:
- `max_completion_tokens` and `max_prompt_tokens` in `previous_session.json`
- The number of **run steps** used
- Whether **instructions** were provided in the assistant or run configuration

---

## 📖 Additional Resources
- [OpenAI Assistants API](https://platform.openai.com/docs/assistants)
- [Understanding Token Limits](https://platform.openai.com/docs/concepts#tokens)
- [Debugging Assistants API](https://platform.openai.com/docs/assistants/deep-dive#debugging)

---

### 💡 Need Help?
For any issues or improvements, feel free to open an **[issue](https://github.com/keyouk/tinas_favorite_city/issues)** or submit a **pull request**. 🚀





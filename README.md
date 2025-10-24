# 🤖 CodeSmith_AI

> **An autonomous AI developer built with [CrewAI](https://github.com/joaomdmoura/crewAI)** and powered by OpenAI — capable of **writing, executing, and analyzing code inside a Docker sandbox**.

---

## 🧭 Overview

**CodeSmith_AI** is your personal **AI-powered coding assistant** that doesn’t just generate code — it **plans, writes, executes, and evaluates** programs safely in a containerized environment.

It uses **CrewAI’s multi-agent orchestration** to coordinate intelligent agents that understand your coding assignment, generate clean and efficient code, execute it, and return structured, human-readable results.

---

## ⚙️ Key Features

- 🧠 **Autonomous Code Generation** – Converts natural language prompts into executable code.
- 🐳 **Docker-Based Execution** – Runs safely inside a Docker sandbox for secure and isolated code evaluation.
- 🧩 **Structured Outputs** – Returns code, execution results, and metadata in a clean JSON format.
- 🪶 **Dynamic Multi-Language Support** – Currently optimized for Python, with plans to expand further.
- 🎨 **Beautiful Terminal UI** – Uses [Rich](https://github.com/Textualize/rich) for syntax-highlighted, color-coded output.
- 🔁 **Retry and Safety Controls** – Auto-retries failed executions and enforces runtime limits for safety.

---

## 🏗️ Tech Stack

| Layer                            | Technology                                      |
| -------------------------------- | ----------------------------------------------- |
| **Agent Framework**        | [CrewAI](https://github.com/joaomdmoura/crewAI)    |
| **LLM Backend**            | OpenAI GPT Models (`gpt-4o`, `gpt-4o-mini`) |
| **Execution Environment**  | Docker container                                |
| **Output Schema**          | [Pydantic](https://docs.pydantic.dev/latest/)      |
| **Terminal Visualization** | [Rich](https://github.com/Textualize/rich)         |
| **Language**               | Python 3.10+                                    |

---

## 🚀 How It Works

1. **Input your prompt** — e.g.,_"Write a Python program to generate the Fibonacci series up to the 25th term."_
2. The **CrewAI agent**:

   - Plans the steps,
   - Writes the complete code,
   - Executes it inside Docker,
   - Returns structured results.
3. The **output** is beautifully displayed in your terminal and saved in:

```

Output/
├── generated_code_<timestamp>.py
└── output_<timestamp>.txt

```

---

## 🧩 Example Output

```bash
💡 Code Generation Result
──────────────────────────────────────────────

🧾 Assignment
Question: Write a Python program to calculate the factorial of a number.
Language: Python

🧠 Generated Code
──────────────────────────────────────────────
def factorial(n):
 return 1 if n == 0 else n * factorial(n-1)

print(factorial(5))

🧩 Program Output
──────────────────────────────────────────────
120
```

---

## 🧰 Prerequisites

Before you begin, make sure you have the following installed:

| Tool                        | Purpose                           | Installation                                                   |
| --------------------------- | --------------------------------- | -------------------------------------------------------------- |
| **🐍 Python 3.10+**   | Run the project and CrewAI        | [Download Python](https://www.python.org/downloads/)              |
| **🐳 Docker Desktop** | For code execution isolation      | [Install Docker](https://www.docker.com/products/docker-desktop/) |
| **🔑 OpenAI API Key** | Required by CrewAI for LLM access | [Get API Key](https://platform.openai.com/account/api-keys)       |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/siddharth1310/codesmith_ai.git
cd codesmith_ai
```

### 2️⃣ Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 5️⃣ Run Docker (ensure Docker Desktop is running)

Make sure Docker is running before you execute any code — CrewAI will automatically use the containerized environment for code execution.

---

## ▶️ Running the Project

From the project root, run:

```bash
crewai run
```

Then follow the prompts:

```bash
Enter programming language: Python
Enter your coding assignment/question: Write a Python program to find the sum of digits in a number.
```

---

## 📂 Project Structure

```
codesmith_ai/
│
├── knowledge/
│   └── user_preference.txt        # Stores user preferences for code styles
│
├── output/                        # Stores generated code & execution outputs
│
├── src/
│   └── codesmith_ai/
│       ├── crew.py                # CrewAI workflow definition (agents & tasks)
│       ├── main.py                # Entry point to run the CrewAI app
│       ├── schemas.py             # Pydantic schemas for structured outputs
│       │
│       └── config/
│           ├── agents.yaml        # Configuration for CrewAI agents
│           └── tasks.yaml         # Task definitions and prompts
│
├── .env                           # Environment variables (e.g., OpenAI API key)
├── .gitignore                     # Files & folders to ignore in version control
├── requirements.txt               # Python dependencies
├── uv.lock                        # Dependency lock file (for reproducible builds)
└── README.md                      # Project documentation
```

---

## 🧠 Example YAMLs

**agents.yaml**

```yaml
coder:
  role: >
    AI Developer
  goal: >
    Write, execute, and test code to solve this assignment: {question}.
  backstory: >
    You're an experienced AI developer skilled in writing clean, efficient, and well-tested code.
  llm: gpt-4o-mini
```

**tasks.yaml**

```yaml
coding_task:
  description: >
    Write and execute code in {programming_language} for: {question}.
  expected_output: >
    A structured JSON object containing the code, execution result, and metadata.
  agent: coder
  output_file: output/code_and_output.json
```

---

## 🧩 Why CodeSmith_AI?

- **Safer**: Runs code in Docker to prevent local damage.
- **Smarter**: Uses CrewAI orchestration to reason about the problem.
- **Structured**: Produces Pydantic outputs for easy downstream use.
- **Beautiful**: Styled terminal display with syntax highlighting.

---

## 🌟 Future Enhancements

- Add multi-language support (Java, C++, JS)
- Integrate OpenRouter / Anthropic LLMs
- Build a minimal web dashboard for code visualization
- Improve Docker container efficiency and resource monitoring

---

## 💬 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit a pull request.

---

## 🧾 License

MIT License © 2025 Siddharth
Use it freely for research and development.

---

## 🙌 Acknowledgements

- [CrewAI](https://github.com/joaomdmoura/crewAI) — for multi-agent orchestration
- [Rich](https://github.com/Textualize/rich) — for beautiful terminal UI
- [Docker](https://www.docker.com/) — for safe and isolated execution

---

## 👤 Author

Created by **Siddharth Singh**. Find me on [LinkedIn](https://www.linkedin.com/in/siddharth-singh-021b34193/)

# In-built packages (Standard Library modules)
import os
import sys
import json
import time
import warnings
from datetime import datetime

# External packages
from rich.text import Text
from rich.panel import Panel
from rich.syntax import Syntax
from rich.console import Console

# Our Own Imports
from .crew import CodeSmith_AI

# Suppress unwanted syntax warnings from certain third-party modules
warnings.filterwarnings("ignore", category = SyntaxWarning, module = "pysbd")

# Create a local output directory if it doesn't exist (used for CrewAI outputs)
os.makedirs("output", exist_ok = True)

# Initialize Rich console for pretty terminal output
console = Console()

def run():
    """
    Main function to run the CrewAI Coder pipeline.
    1. Takes user input (language + question)
    2. Passes input to CrewAI crew for code generation & execution
    3. Displays the structured result beautifully in the terminal
    4. Saves both the generated code and output to files in the project Output folder
    """
    
    # 🧠 STEP 1: Take user input
    programming_language = input("Enter programming language: ").strip()
    question = input("Enter your coding assignment/question: ").strip()
    
    # Prepare inputs for the CrewAI agent
    inputs = {"programming_language" : programming_language, "question" : question}
    
    try:
        # 🚀 STEP 2: Run the CrewAI workflow
        result = CodeSmith_AI().crew().kickoff(inputs = inputs)
        
        # The result comes as a raw JSON-like string
        json_obj = json.loads(result.raw)
        
        # Extract the main components from structured output
        code_content = json_obj["code"].strip()
        final_result = json_obj["final_result"].strip()
        
        # 💡 STEP 3: Display results beautifully in terminal
        
        # Create a rich visual separator
        console.rule("[bold cyan]💡 Code Generation Result[/bold cyan]")
        
        # 3.1 Show the question and language info
        qna = (
            f"[bold]Question:[/bold] {json_obj['question']}\n"
            f"[bold]Language:[/bold] {json_obj['programming_language'].capitalize()}"
        )
        console.print(Panel.fit(qna, title = "[yellow]🧾 Assignment[/yellow]", border_style = "yellow"))
        
        # 3.2 Syntax-highlighted code block
        syntax = Syntax(json_obj["code"].strip(), lexer = json_obj["programming_language"].lower(), theme = "monokai", line_numbers = True)
        console.print(Panel(syntax, title = "[green]🧠 Generated Code[/green]", border_style = "green"))
        
        # 3.3 Final program output panel
        output_text = Text(json_obj["final_result"].strip(), style = "bold white")
        console.print(Panel(output_text, title = "[blue]🧩 Program Output[/blue]", border_style = "blue"))
        
        # 💾 STEP 4: Save generated code and results to files
        # Dynamically locate project root (this script is inside src/coder/)
        script_dir = os.path.dirname(os.path.abspath(__file__))  # → src/coder/
        project_root = os.path.abspath(os.path.join(script_dir, "../../"))  # → coder/
        
        ## Point to the top-level "Output" folder in the project root
        output_folder = os.path.join(project_root, "output")
        os.makedirs(output_folder, exist_ok = True)
        
        # Use a timestamp to make filenames unique
        timestamp = int(time.time())
        
        # 4.1 Save generated code as a .py file
        code_filename = os.path.join(output_folder, f"generated_code_{timestamp}.py")
        with open(code_filename, "w", encoding = "utf-8") as f:
            f.write(code_content)
        console.print(f"[bold green]✅ Generated code saved to:[/bold green] {code_filename}")
        
        # 4.2 Save execution result (console output) as a .txt file
        result_filename = os.path.join(output_folder, f"output_{timestamp}.txt")
        with open(result_filename, "w", encoding = "utf-8") as f:
            f.write(final_result)
        console.print(f"[bold green]✅ Execution output saved to:[/bold green] {result_filename}")
    # ⚠️ STEP 5: Handle runtime errors gracefully
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        CodeSmith_AI().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CodeSmith_AI().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        CodeSmith_AI().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

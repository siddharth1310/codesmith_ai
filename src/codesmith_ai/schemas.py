# In-built packages (Standard Library modules)

# External packages
from pydantic import BaseModel, Field

# Our Own Imports

class CodeResult(BaseModel):
    """Structured response for generated and executed code"""
    question : str = Field(..., description = "The original question or assignment from the user")
    programming_language : str = Field(..., description = "The programming language chosen for this task")
    code : str = Field(..., description = "The generated source code that solves the question")
    final_result : str = Field(..., description = "The output or result after executing the code")

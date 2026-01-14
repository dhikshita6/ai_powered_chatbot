import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()

def generate_docstring_content(fn: dict) -> dict:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY not set")

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.3,
        api_key=api_key
    )

    arg_names = [a["name"] for a in fn.get("args", [])]

    prompt = f"""
Return ONLY valid JSON:

{{
  "summary": "Imperative one-line description",
  "args": {{ "arg": "description" }},
  "returns": "description",
  "raises": {{}}
}}

Rules:
- Imperative mood
- No markdown
- No triple quotes
- Strict JSON

Function: {fn["name"]}
Arguments: {arg_names}
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        return {
            "summary": f"Describe `{fn['name']}`.",
            "args": {a: "DESCRIPTION" for a in arg_names},
            "returns": "DESCRIPTION",
            "raises": {}
        }

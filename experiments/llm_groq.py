# # from langchain_groq import ChatGroq
# # from langchain_core.messages import HumanMessage

# # llm = ChatGroq(
# #     model="llama-3.1-8b-instant",
# #     temperature=0.3,
# # )

# # response = llm.invoke([
# #     HumanMessage(content="What is data scientist. Explain step by step.")
# # ])

# # print(response.content)


# # from dotenv import load_dotenv
# # import os
# # from langchain_groq import ChatGroq
# # from langchain_core.messages import HumanMessage

# # # Load .env file
# # load_dotenv()

# # # Verify key is loaded
# # api_key = os.getenv("GROQ_API_KEY")

# # llm = ChatGroq(
# #     model="llama-3.1-8b-instant",
# #     temperature=0.3,
# #     api_key=api_key
# # )

# # response = llm.invoke([
# #     HumanMessage(content="What is data scientist. Explain step by step.")
# # ])

# # print(response.content)


# import streamlit as st
# from dotenv import load_dotenv
# import os
# from langchain_groq import ChatGroq
# from langchain_core.messages import HumanMessage

# # Load .env file
# load_dotenv()

# # Get API key
# api_key = os.getenv("GROQ_API_KEY")

# st.title("Groq LLM Test (LangChain + Streamlit)")

# if not api_key:
#     st.error("GROQ_API_KEY not found. Please set it in your .env file.")
# else:
#     llm = ChatGroq(
#         model="openai/gpt-oss-120b", #llama-3.1-8b-instant
#         temperature=0.3,
#         api_key=api_key
#     )

#     # ✅ Single-line input box
#     user_input = st.text_area(
#         "Enter your prompt:",
#         value="What is a data scientist? Explain step by step."
#     )

#     if st.button("Run LLM"):
#         if not user_input.strip():
#             st.warning("Please enter a prompt.")
#         else:
#             with st.spinner("Thinking..."):
#                 response = llm.invoke([
#                     HumanMessage(content=user_input)
#                 ])

#             st.subheader("Response:")
#             st.write(response.content)

# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain_core.messages import HumanMessage

# class GroqDocstringGenerator:
#     def __init__(self):
#         load_dotenv()
#         api_key = os.getenv("GROQ_API_KEY")

#         if not api_key:
#             raise ValueError("GROQ_API_KEY not found in .env file")

#         self.llm = ChatGroq(
#             model="llama-3.1-8b-instant",
#             temperature=0.3,
#             api_key=api_key
#         )

#     def generate(self, function_name, params, source_code=""):
#         prompt =f"""
# You are an automated docstring generator.

# TASK:
# Generate ONLY a Python docstring for the given function.

# STRICT RULES (MANDATORY):
# - Output ONLY the docstring
# - Use triple double quotes 
# - DO NOT include code
# - DO NOT include markdown
# - DO NOT include explanations
# - DO NOT include examples
# - DO NOT include backticks
# - DO NOT repeat the function definition
# - DO NOT add any text outside the docstring

# Function name:
# {function_name}

# Function source code:
# {source_code}
# """

#         response = self.llm.invoke([
#             HumanMessage(content=prompt)
#         ])

#         return f'"""\n{response.content.strip()}\n"""'
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()


class GroqDocstringGenerator:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")

        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.3,
            api_key=api_key
        )

    def generate(self, function_name, params, source_code):
        """
        Generate a clean Python docstring using Groq LLM.
        """

        param_list = ", ".join(params) if params else "None"

        prompt = f"""
Generate ONLY a Python docstring.

STRICT RULES:
- Output ONLY the docstring
- Start and end with triple double quotes
- NO markdown
- NO explanations
- NO code blocks
- NO imports
- NO function definition

Function name: {function_name}
Parameters: {param_list}

Function source code:
{source_code}

Follow PEP-257 style.
"""

        response = self.llm.invoke([
            HumanMessage(content=prompt)
        ])

        return response.content.strip()

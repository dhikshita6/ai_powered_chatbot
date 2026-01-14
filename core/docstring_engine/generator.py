# # def generate_docstring(name, style="google"):
# #     if style == "google":
# #         return f'''"""{name}.

# # Args:
# #     param: description

# # Returns:
# #     result
# # """'''
# #     if style == "numpy":
# #         return f'''"""{name}

# # Parameters
# # ----------
# # param : type
# #     description

# # Returns
# # -------
# # type
# # """'''
# #     if style == "rest":
# #         return f'''"""{name}

# # :param param: description
# # :return: result
# # """'''


# class DocstringGenerator:
#     """
#     Generates preview docstrings in different styles.
#     """

#     def generate(self, func_name, params, style="rest"):
#         if style == "rest":
#             lines = [
#                 f"{func_name} function.",
#                 ""
#             ]
#             for p in params:
#                 lines.append(f":param {p}: DESCRIPTION")
#                 lines.append(f":type {p}: TYPE")
#             return '"""\n' + "\n".join(lines) + '\n"""'

#         # default fallback
#         return f'"""{func_name} function."""'
from core.docstring_engine.llm_integration import generate_docstring_content

def generate_docstring(fn, style="google"):
    llm = generate_docstring_content(fn)

    summary = llm["summary"]
    args = llm["args"]
    returns = llm["returns"]

    if style == "google":
        lines = [summary, "", "Args:"]
        for k, v in args.items():
            lines.append(f"    {k}: {v}")
        lines.append("")
        lines.append(f"Returns:")
        lines.append(f"    {returns}")
    
    elif style == "numpy":
        lines = [
            summary,
            "",
            "Parameters",
            "----------"
        ]
        for k, v in args.items():
            lines.append(f"{k}")
            lines.append(f"    {v}")
        lines.extend(["", "Returns", "-------", returns])
    
    else:  # reST
        lines = [summary, ""]
        for k, v in args.items():
            lines.append(f":param {k}: {v}")
        lines.append(f":return: {returns}")

    return '"""\n' + "\n".join(lines) + '\n"""'

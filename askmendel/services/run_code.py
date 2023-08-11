# import re
# import io
# from contextlib import redirect_stdout
# from askmendel.prompts.correct_error_prompt import CorrectErrorPrompt


# def execute_code(code_to_run, data, original_instructions, _max_retries=5):
#     START_CODE_TAG = "<startCode>"
#     END_CODE_TAG = "<endCode>"
#     separator: str = "```"
#     match = re.search(
#         rf"{START_CODE_TAG}(.*)({END_CODE_TAG}"
#         rf"|{END_CODE_TAG.replace('<', '</')}"
#         rf"|{START_CODE_TAG.replace('<', '</')})",
#         code_to_run,
#         re.DOTALL,
#     )
#     if match:
#         code_to_run = match.group(1).strip()
#     if len(code_to_run.split(separator)) > 1:
#         code_to_run = code_to_run.split(separator)[1]

#     if re.match(r"^(python|py)", code_to_run):
#         code_to_run = re.sub(r"^(python|py)", "", code_to_run)
#     if re.match(r"^`.*`$", code_to_run):
#         code_to_run = re.sub(r"^`(.*)`$", r"\1", code_to_run)
#     code_to_run = code_to_run.strip()

#     # Redirect standard output to a StringIO buffer
#         with redirect_stdout(io.StringIO()) as output:
#             count = 0
#             while count < _max_retries:
#                 try:
#                     # Execute the code
#                     locals_dict = {"adata": data}
#                     exec(code_to_run, globals(), locals_dict)
#                     adata = locals_dict["adata"]
                    
#                 except Exception as e:
#                     count += 1
#                     print(f"Ran into error. Trying again {count} time")
#                     code_to_run = self._retry_run_code(code, e, adata)

#     return code_to_run, adata
            
#     def _retry_run_code(self, code: str, e: Exception, original_instructions: dict, adata):
#         correct_error_default_values = {
#             "code": code,
#             "error_returned": e,
#             "question": original_instructions["question"],
#             "adata_metadata": original_instructions["adata_metadata"],
#             "num_rows": original_instructions["num_rows"],
#             "num_columns": original_instructions["num_columns"],
#         }
#         instruction = CorrectErrorPrompt(**correct_error_default_values)

#         code = self._llm.generate_code(instruction, "")

#         return code, adata


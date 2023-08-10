import re
import io
from contextlib import redirect_stdout


def execute_code(code_to_run, data):
    START_CODE_TAG = "<startCode>"
    END_CODE_TAG = "<endCode>"
    separator: str = "```"
    match = re.search(
        rf"{START_CODE_TAG}(.*)({END_CODE_TAG}"
        rf"|{END_CODE_TAG.replace('<', '</')}"
        rf"|{START_CODE_TAG.replace('<', '</')})",
        code_to_run,
        re.DOTALL,
    )
    if match:
        code_to_run = match.group(1).strip()
    if len(code_to_run.split(separator)) > 1:
        code_to_run = code_to_run.split(separator)[1]

    if re.match(r"^(python|py)", code_to_run):
        code_to_run = re.sub(r"^(python|py)", "", code_to_run)
    if re.match(r"^`.*`$", code_to_run):
        code_to_run = re.sub(r"^`(.*)`$", r"\1", code_to_run)
    code_to_run = code_to_run.strip()

    # Redirect standard output to a StringIO buffer
    with redirect_stdout(io.StringIO()) as output:
        count = 0
        try:
            # Execute the code
            locals_dict = {"adata": data}
            exec(code_to_run, globals(), locals_dict)
            adata = locals_dict["adata"]
            return code_to_run, adata
        except Exception as e:
            print(e)

    # captured_output = output.getvalue().strip()
    # print()
    # print("================")
    # print("captured_output")
    # print(captured_output)
    # print("================")
    # print(adata.shape)
    # return captured_output

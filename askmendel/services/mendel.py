import re
import io
from contextlib import redirect_stdout
from askmendel.llm.openai import LLM
from askmendel.prompts.default_plan import DefaultPlan
from askmendel.prompts.default_prompt import DefaultPrompt
from askmendel.prompts.correct_error_prompt import CorrectErrorPrompt


class AskMendel:
    def __init__(self):
        self.llm = LLM()  # This can be langchain LLM
        self._start_time = None
        self._n_rows_to_display = 5
        self.original_instructions = None
        self._max_retries = 5
        self.count = 0
        self.last_result = None
        self.last_prompt = None

    def ask(self, data, prompt, plan):
        generate_code_default_values = {
            "adata_metadata": data.to_df().head(),
            "n_rows": data.shape[0],
            "n_columns": data.shape[1],
            "plan": plan,
        }

        instruction = DefaultPrompt(**generate_code_default_values)
        
        result = self.llm.call(
            instruction=str(instruction), prompt=str(prompt), suffix="\n\nCode:\n"
        )
        if self.original_instructions is None:
            self.original_instructions = generate_code_default_values
            self.original_instructions["question"] = str(prompt)
        
        self.last_result = result
        self.last_prompt = str(prompt)

        return result

    def generate_plan(self, data, prompt):
        generate_code_default_values = {
            "adata_metadata": data.to_df().head(),
            "n_rows": data.shape[0],
            "n_columns": data.shape[1],
        }
        instruction = DefaultPlan(**generate_code_default_values)
    
        plan = self.llm.call(instruction=str(instruction), prompt=str(prompt))
        self.original_instructions = {"plan": str(plan)}

        return plan


    def _clean_code(self, code_to_run):
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

        return code_to_run

    def _run_code(self, code_to_run, adata):
        # Redirect standard output to a StringIO buffer
        with redirect_stdout(io.StringIO()) as output:
            self.count = 0
            while self.count < self._max_retries:
                print(f"Trying to run {self.count} time")
                try:
                    # Execute the code
                    locals_dict = {"adata": adata}
                    exec(code_to_run, globals(), locals_dict)
                    adata = locals_dict["adata"]
                    break
                except Exception as e:
                    self.count += 1
                    print(e)
                    # code_to_run = self._retry_run_code(code_to_run, e, adata)

        captured_output = output.getvalue().strip()
        if code_to_run.count("print(") > 1:
            return captured_output

        lines = code_to_run.strip().split("\n")
        last_line = lines[-1].strip()

        match = re.match(r"^print\((.*)\)$", last_line)
        if match:
            last_line = match.group(1)

        try:
            result = eval(last_line, environment)

            # In some cases, the result is a tuple of values. For example, when
            # the last line is `print("Hello", "World")`, the result is a tuple
            # of two strings. In this case, we want to return a string
            if isinstance(result, tuple):
                result = " ".join([str(element) for element in result])

            return result
        except Exception:
            return captured_output

    def _retry_run_code(self, code_to_run: str, e: Exception, adata):
        print("Going to correct the error")
        correct_error_default_values = {
            "code": str(code_to_run),
            "error_returned": str(e),
            "plan": self.original_instructions['plan'],
            "question": self.original_instructions["question"],
            "adata_metadata": self.original_instructions["adata_metadata"],
            "n_rows": self.original_instructions["n_rows"],
            "n_columns": self.original_instructions["n_columns"]
        }
        print(correct_error_default_values)
        print()
        
        instruction = CorrectErrorPrompt(**correct_error_default_values)

        code = self.llm.call(instruction=str(instruction), prompt="")

        return code


def ask_mendel_for_result(adata, prompt, plan):
    mendel = AskMendel()
    response = mendel.ask(adata, prompt, plan)
    code = mendel._clean_code(response)
    return mendel._run_code(code, adata)


def ask_mendel_for_plan(adata, prompt):
    mendel = AskMendel()
    return mendel.generate_plan(adata, prompt)
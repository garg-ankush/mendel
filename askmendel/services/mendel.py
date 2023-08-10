from askmendel.llm.openai import LLM
from .format_code import execute_code
from askmendel.prompts.default_plan import DefaultPlan
from askmendel.prompts.default_prompt import DefaultPrompt


class AskMendel:
    def __init__(self):
        self.llm = LLM()  # This can be langchain LLM
        self._start_time = None
        self._n_rows_to_display = 5

    def ask(self, data, prompt, plan):
        generate_code_default_values = {
            "adata_metadata": data.to_df().head(),
            "n_rows": data.shape[0],
            "n_columns": data.shape[1],
            "plan": plan,
        }

        instruction = DefaultPrompt(**generate_code_default_values)
        return self.llm.call(
            instruction=str(instruction), prompt=str(prompt), suffix="\n\nCode:\n"
        )

    def generate_plan(self, data, prompt):
        generate_code_default_values = {
            "adata_metadata": data.to_df().head(),
            "n_rows": data.shape[0],
            "n_columns": data.shape[1],
        }
        instruction = DefaultPlan(**generate_code_default_values)
        return self.llm.call(instruction=str(instruction), prompt=str(prompt))


def ask_mendel_for_result(adata, prompt, plan):
    mendel = AskMendel()
    response = mendel.ask(adata, prompt, plan)
    result = execute_code(response, adata)
    return result


def ask_mendel_for_plan(adata, prompt):
    mendel = AskMendel()
    return mendel.generate_plan(adata, prompt)

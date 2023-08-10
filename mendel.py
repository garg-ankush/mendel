import time
import openai
import os
from dotenv import load_dotenv

load_dotenv()


class LLM:
    def __init__(self):
        self.model_name: str = "gpt-3.5-turbo"
        self.openai = openai
        self.openai.api_key = os.getenv("OPENAI_API_KEY")

    def call(self, instruction: str, prompt: str, suffix=""):
        return self.completion(str(instruction) + str(prompt) + suffix)

    def completion(self, instructions):
        params = {
            "messages": [
                {
                    "role": "system",
                    "content": instructions,
                }
            ],
            "temperature": 0,
            "max_tokens": 512,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0.6,
        }

        response = self.openai.ChatCompletion.create(
            model=self.model_name,
            **params
        )
        return response["choices"][0]["message"]["content"]


class DefaultPrompt:
    text: str = """
    You are provided with anndata data (adata) with {n_rows} genes and {n_columns} cells.
    
    You are also provided with a general plan on how to execute the steps: {plan}
    
    Based on the given plan write python code, use scanpy library to generate the code. 

    """

    #   This is the metadata of the dataset: {adata_metadata}
    #   No need to load the dataset, you will be provided the adata.

    # When asked about the data, you should respond with a plan in a bullet list.

    # When asked about the data, your response should include a python code that describes the ann dataframe
    # `dataset`. This code is preferably using the scanpy library. Using the provided data, dataset, return the
    # python code and make sure to prefix the requested python code with {START_CODE_TAG} exactly and suffix the code
    # with {END_CODE_TAG} exactly to get the answer to the following question:

    def __init__(self, **kwargs):
        self._args = kwargs
        self._args["START_CODE_TAG"] = "<startCode>"
        self._args["END_CODE_TAG"] = "<endCode>"

    def __str__(self):
        return self.text.format(**self._args)


class DefaultPlan:
    text: str = """
    You are provided with anndata data (adata) with {n_rows} genes and {n_columns} cells. 
    
    This is the metadata of the dataset: {adata_metadata}
    
    No need to load the dataset, you will be provided the adata.
    
    When asked about the data, you should respond with a plan in a bullet list based on the following question: 
    
    """

    def __init__(self, **kwargs):
        self._args = kwargs

    def __str__(self):
        return self.text.format(**self._args)


class AskMendel:
    def __init__(self, llm=None):
        # if llm is None:
        #     raise Exception("An LLM should be provided to instantiate a Mendel Instance.")
        self.llm = LLM()  # This can be langchain LLM
        self._start_time = None
        self._n_rows_to_display = 5

    def ask(self, data, prompt, plan):
        generate_code_default_values = {
            "adata_metadata": data.to_df().head(),
            "n_rows": data.shape[0],
            "n_columns": data.shape[1],
            "plan": plan
            }

        instruction = DefaultPrompt(**generate_code_default_values)
        return self.llm.call(instruction=str(instruction), prompt=str(prompt), suffix="\n\nCode:\n")

    def generate_plan(self, data, prompt):
        generate_code_default_values = {
            "adata_metadata": data.to_df().head(),
            "n_rows": data.shape[0],
            "n_columns": data.shape[1]
        }
        instruction = DefaultPlan(**generate_code_default_values)
        return self.llm.call(instruction=str(instruction), prompt=str(prompt))







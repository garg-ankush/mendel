
class CorrectErrorPrompt:
    text: str = """
    You are provided with anndata data (adata) with {n_rows} genes and {n_columns} cells.
    This is the metadata of the adata: {adata_metadata}
    
    You are also provided with a general plan on how to execute the steps: {plan}

    The user asked this question: {question}

    The code you generated was this: {code}

    It fails with the following error: {error_returned}

    Correct the pytnon code and return a new python code that fixes the above
    mentioned error. Do not generate the same code again.

    """
    def __init__(self, **kwargs):
        self._args = kwargs
        self._args["START_CODE_TAG"] = "<startCode>"
        self._args["END_CODE_TAG"] = "<endCode>"
    
    def __str__(self):
        return self.text.format(**self._args)

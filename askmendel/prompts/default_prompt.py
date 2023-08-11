
class DefaultPrompt:
    text: str = """
    You are provided with anndata data (adata) with {n_rows} genes and {n_columns} cells.
    
    This is the metadata of the dataset: {adata_metadata}.

    You are also provided with a general plan on how to execute the steps: {plan}
    
    Based on the given plan write python code, use scanpy library to generate the code. 

    """

    # No need to load the dataset, you will be provided the adata.

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

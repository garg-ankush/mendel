
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

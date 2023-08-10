import os
import scanpy as sc
from pathlib import Path
import matplotlib.pyplot as plt


def read_data(file_path: str, file_type: str):
    if file_type == "mtx":
        adata = sc.read_10x_mtx(file_path, var_names="gene_symbols", cache=True)
        return adata

    adata = sc.read_10x_h5(file_path)
    return adata


def save_figure(figure, filename: str):
    # Derive root path
    parent_path = Path(__file__).resolve().parent
    root_path = Path(parent_path).parents[1]  # "path/to
    # Derive directory path for figures
    directory_path = "/".join([str(root_path), "output", "figures"])
    # Create directory if it doesn't exist already
    os.makedirs(directory_path, exist_ok=True)
    # Save the current figure to a variable
    figure.savefig(f"{directory_path}/{filename}")
    plt.close(figure)

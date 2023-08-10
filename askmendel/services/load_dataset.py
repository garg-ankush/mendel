from .utilities import read_data
import os
import scanpy as sc


def load_dataset(path_to_dataset):
    # Check contents of the dataset path

    file_type = None
    file_path = None

    # Traverse through all the files in the path to dataset
    for root, dirs, files in os.walk(path_to_dataset):
        for file in files:
            if file.endswith("h5"):
                file_type = "h5"
                file_path = os.path.join(root, file)
                continue

            if file.endswith("mtx"):
                file_type = "mtx"
                file_path = root
                continue

    # @ TODO Raise exception when either file_path or file_type is None
    return read_data(file_path=file_path, file_type=file_type)


def download_dataset():
    os.makedirs("dataset", exist_ok=True)
    sc.datasets.pbmc3k()

    return sc.read_h5ad("data/pbmc3k_raw.h5ad")

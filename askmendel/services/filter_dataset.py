import scanpy as sc


def filter_cells(dataset, minimum_genes: int):
    print("Filtering cells...")
    return sc.pp.filter_cells(dataset, min_genes=minimum_genes)


def filter_genes(dataset, minimum_cells: int = None):
    print("Filtering genes...")
    return sc.pp.filter_genes(dataset, min_cells=minimum_cells)


def filter_outliers(dataset, column_name, threshold):
    print("Filtering outliers...")
    return dataset[dataset.obs[column_name] < threshold, :]

import scanpy as sc


def calculate_qc_metrics(dataset, mitochondrial_genes_only=True):
    print("Calculating QC metrics...")
    if mitochondrial_genes_only:
        dataset.var['mt'] = dataset.var_names.str.startswith('MT-')  # annotate the group of mitochondrial genes as 'mt'
        sc.pp.calculate_qc_metrics(dataset, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)
        return dataset
    else:
        sc.pp.calculate_qc_metrics(dataset, percent_top=None, log1p=False, inplace=True)
        return dataset


def pca(dataset):
    print("Performing PCA.")
    return sc.tl.pca(dataset, svd_solver='arpack')

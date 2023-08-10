import argparse
import matplotlib.pyplot as plt
import scanpy as sc

from load_dataset import load_dataset
from filter_dataset import filter_genes, filter_cells, filter_outliers

from data.services.read_configs import read_configs

from format_code import execute_code
from mendel import AskMendel

parser = argparse.ArgumentParser(description='Load dataset')
parser.add_argument('path_to_dataset', help='Provide a path to dataset')


if __name__ == "__main__":
    args = parser.parse_args()
    configs = read_configs()

    print(configs)

    # # RUN OUTLIER DETECTION ALGORITHMS HERE
    # # Keep values less than n_genes
    # filter_outliers(dataset=adata, column_name="n_genes_by_counts", threshold=2500)
    # # Keep values less than pct_counts
    # filter_outliers(dataset=adata, column_name="pct_counts_mt", threshold=5)
    #
    # # Normalize dataset
    # sc.pp.normalize_total(adata, target_sum=1e4)
    #
    # # Log dataset
    # sc.pp.log1p(adata)
    #
    # # Calculate highly variable genes
    # sc.pp.highly_variable_genes(
    #     adata,
    #     min_mean=configs["highly_variable_genes_min_mean"],
    #     max_mean=configs["highly_variable_genes_max_mean"],
    #     min_disp=configs["highly_variable_genes_min_disp"]
    # )
    # #
    # # generate_highly_variable_genes_plot(dataset, plot_name="highly_variable_genes.png")
    # #
    # # Save raw data
    # adata.raw = adata
    #
    # # PCA
    # pca(adata)
    # generate_pca_plot(adata, plot_name="pca.png")
    #
    # # Neighborhood graph
    # sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)

    # mendel_client = AskMendel()
    # # code = mendel_client.run( adata, "Can you draw a scatter plot with total_counts and pct_counts_mt? Do not
    # # calculate these metrics - they're already provided in the dataset and the metadata" )
    #
    # # code = mendel_client.run(
    # #     adata,
    # #     "Remove the records in adata that have total_counts greater than 6000."
    # # )
    #
    # # code = mendel_client.run(
    # #     adata,
    # #     "Remove the records in adata that have total_counts greater than 6000."
    # # )
    #
    # # code = mendel_client.run(
    # #     adata,
    # #     "Can you plot the embedded graph using UMAP? Use these colors - 'CST3', 'NKG7', 'PPBP'"
    # # )
    #
    # # code = mendel_client.run(
    # #     adata,
    # #     "Can you plot the embedded graph using UMAP? Use these colors - 'CST3', 'NKG7', 'PPBP'."
    # # )
    #
    # code = mendel_client.run(
    #     adata,
    #     "Save the latest adata object to disk?"
    # )
    #
    # code, result = execute_code(code, adata)
    # print(result)
    # print(code)

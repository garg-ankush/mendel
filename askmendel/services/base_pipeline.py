import scanpy as sc
from .filter_dataset import filter_genes, filter_cells
from .generate_plots import (
    generate_scatter_plot,
    generate_violin_plot
)
from .preprocessing import calculate_qc_metrics


def run_pipeline(adata, configs, show_plots=False):
    # Filter dataset
    filter_cells(adata, minimum_genes=configs.get("minimum_genes"))
    filter_genes(adata, minimum_cells=configs.get("minimum_cells"))

    calculate_qc_metrics(
        dataset=adata, mitochondrial_genes_only=configs["mitochondrial_genes_only"]
    )

    # Generate plots
    generate_violin_plot(
        dataset=adata,
        variables=["n_genes_by_counts", "total_counts", "pct_counts_mt"],
        plot_name="violin-plots.png",
        show_plots=show_plots,
    )
    generate_scatter_plot(
        dataset=adata,
        variables=["total_counts", "pct_counts_mt"],
        plot_name="total_counts-vs-pct-counts-mt.png",
    )
    generate_scatter_plot(
        dataset=adata,
        variables=["total_counts", "n_genes_by_counts"],
        plot_name="total_counts-vs-n_genes_by_counts.png",
    )

    print("Normalizing data...")
    sc.pp.normalize_total(adata, target_sum=1e4)

    print("Logarithmize data...")
    sc.pp.log1p(adata)

    
import scanpy as sc
import matplotlib.pyplot as plt
from utilities import save_figure


def generate_violin_plot(dataset, variables, plot_name, show_plots):
    sc.pl.violin(
        dataset,
        variables,
        jitter=0.4,
        multi_panel=True,
        show=show_plots
    )
    figure = plt.gcf()
    if not show_plots:
        save_figure(figure=figure, filename=plot_name)


def generate_scatter_plot(dataset, variables, plot_name):
    sc.pl.scatter(
        dataset,
        x=variables[0],
        y=variables[1],
        show=False
    )

    figure = plt.gcf()
    save_figure(figure=figure, filename=plot_name)


def generate_highly_variable_genes_plot(dataset, plot_name):
    sc.pl.highly_variable_genes(dataset, show=False)

    figure = plt.gcf()
    save_figure(figure=figure, filename=plot_name)


def generate_pca_plot(dataset, plot_name):
    sc.pl.pca(dataset, color='CST3', show=False)

    figure = plt.gcf()
    save_figure(figure=figure, filename=plot_name)
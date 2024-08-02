import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_objective_function(file_template, start, n_clusters, nbuildings):
    """
    Plots the objective function values from a series of pickle files which differs in terms of the number of clusters.

    Parameters:
    - file_template: a string template for the file paths with a placeholder for the cluster number (e.g., 'path/to/3a_TD{}.pickle')
    - start: the starting number of clusters
    - n_clusters: the ending number of clusters
    - nbuildings : numbers of buildings
    """

    clusters = []
    objectives = []
    capex = []
    opex = []

    for n in range(start, n_clusters + 1):
        file_path = file_template.format(n)
        results = pd.read_pickle(file_path)
        sc = list(results.keys())[0]
        id = list(results[sc].keys())[0]
        era = results[sc][id]['df_Buildings'].ERA.sum()
        objective_value = results['totex'][0]['df_Performance']['Objective'][nbuildings]/era
        opex_value = results['totex'][0]['df_Performance']['Costs_op'][nbuildings]/era
        capex_value = results['totex'][0]['df_Performance']['Costs_inv'][nbuildings]/era

        clusters.append(n)
        objectives.append(objective_value)
        opex.append(opex_value)
        capex.append(capex_value)

    plt.rcParams['axes.spines.left'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.bottom'] = False

    plt.plot(clusters,objectives, label='TOTEX',color='gray', linestyle='dashed', marker='|',
     markerfacecolor='gray', markersize=10,linewidth=0.5)
    plt.plot(clusters,opex, label='OPEX',color='blue', linestyle='dashed', marker='|',
     markerfacecolor='blue', markersize=10,linewidth=0.5)
    plt.plot(clusters,capex, label='CAPEX',color='green', linestyle='dashed', marker='|',
     markerfacecolor='green', markersize=10,linewidth=0.5)
    plt.hlines(y=0,xmin=1,xmax=n_clusters,colors='black',linestyles='dashed',linewidth=0.5)
    plt.xticks(np.arange(start, n_clusters+1, step=1))
    plt.yticks([min(objectives),0, max(objectives)])
    plt.xlabel('Amount of clusters [-]')
    plt.ylabel('Costs [CHF/m$^2$ yr]', rotation=0,labelpad=-110, loc='top')
    plt.legend()
    plt.show()

if __name__ == '__main__':

    file_template = 'C:/Users/lefebvreart/PycharmProjects/REHO_2024_07_31/scripts/examples/results/3a_TD{}.pickle'
    plot_objective_function(file_template, 2, 16, 10)
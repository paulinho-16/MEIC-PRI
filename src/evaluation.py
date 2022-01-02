import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import numpy as np
import requests
import pandas as pd
from pathlib import Path

evaluation_folder = Path("./evaluation")

N = 40
precision = None
recall = None

# METRICS TABLE
# Define custom decorator to automatically calculate metric based on key
metrics = {}
metric = lambda f: metrics.setdefault(f.__name__, f)

@metric
def ap(results, relevant):
    """Average Precision"""
    precision_values = [
        len([
            doc 
            for doc in results[:idx]
            if doc['imdbID'] in relevant
        ]) / idx 
        for idx in range(1, len(results) + 1)
    ]
    print(precision_values)
    return sum(precision_values)/len(precision_values)

@metric
def precisionAtN(results, relevant, n=N):
    """Precision at N"""
    print("--------------------------------------")
    print(len(results))
    print("--------------------------------------")
    print(relevant)

    global precision
    precision = len([doc for doc in results[:n] if doc['imdbID'] in relevant])/n
    return precision

@metric
def recallAtN(results, relevant, n=N):
    """Recall at N"""
    global recall
    recall = len([doc for doc in results[:n] if doc['imdbID'] in relevant])/float(len(relevant))
    return recall

@metric
def f1AtN(_, __, n=N):
    """F1 at N"""
    f1 = 2 * (precision * recall)/(precision + recall)
    return f1

def calculate_metric(key, results, relevant):
    return metrics[key](results, relevant)

# Define metrics to be calculated
evaluation_metrics = {
    'ap': 'Average Precision',
    'precisionAtN': f'Precision at {N} (P@{N})',
    'recallAtN': f'Recall at {N} (R@{N})',
    'f1AtN': f'F1 at {N} (R@{N})'
}

def evaluate_query(query_number, query_url):
    qrels_file = evaluation_folder/f'qrels_{query_number}.txt'

    # Read qrels to extract relevant documents
    relevant = list(map(lambda el: el.strip(), open(qrels_file).readlines()))

    # Get query results from Solr instance
    results = requests.get(query_url).json()['response']['docs']

    # Calculate all metrics and export results as LaTeX table
    df = pd.DataFrame([['Metric','Value']] +
        [
            [evaluation_metrics[m], calculate_metric(m, results, relevant)]
            for m in evaluation_metrics
        ]
    )

    with open(f'{evaluation_folder}/results_query{query_number}.tex','w') as tf:
        tf.write(df.to_latex())
    
    # PRECISION-RECALL CURVE
    # Calculate precision and recall values as we move down the ranked list
    precision_values = [
        len([
            doc 
            for doc in results[:idx]
            if doc['imdbID'] in relevant
        ]) / idx 
        for idx, _ in enumerate(results, start=1)
    ]

    recall_values = [
        len([
            doc for doc in results[:idx]
            if doc['imdbID'] in relevant
        ]) / len(relevant)
        for idx, _ in enumerate(results, start=1)
    ]

    precision_recall_match = {k: v for k,v in zip(recall_values, precision_values)}

    # Extend recall_values to include traditional steps for a better curve (0.1, 0.2 ...)
    recall_values.extend([step for step in np.arange(0.1, 1.1, 0.1) if step not in recall_values])
    recall_values = sorted(set(recall_values))

    # Extend matching dict to include these new intermediate steps
    for idx, step in enumerate(recall_values):
        if step not in precision_recall_match:
            if recall_values[idx-1] in precision_recall_match:
                precision_recall_match[step] = precision_recall_match[recall_values[idx-1]]
            else:
                precision_recall_match[step] = precision_recall_match[recall_values[idx+1]]

    disp = PrecisionRecallDisplay([precision_recall_match.get(r) for r in recall_values], recall_values)
    disp.plot()
    plt.savefig(f'{evaluation_folder}/precision_recall_query{query_number}.pdf')

if __name__ == '__main__':
    # evaluate_query(1, 'http://localhost:8983/solr/shows/query?q=english&q.op=AND&defType=edismax&indent=true&debugQuery=false&qf=language%5E2%20summary&rows=20&tie=1')
    # evaluate_query(2, 'http://localhost:8983/solr/shows/select?defType=edismax&indent=true&q.op=AND&q=title%3ADoing%20originCountry%3A%22United%20States%22%20startYear%3A%5B2017%20TO%202021%5D&tie=1')
    # evaluate_query(3, 'http://localhost:8983/solr/shows/select?defType=edismax&indent=true&q.op=AND&q=rating%3A%5B7%20TO%20*%5D%20startYear%3A%5B2010%20TO%20*%5D%20endYear%3A%5B*%20TO%202020%5D%20(certificate%3AR%C3%BAssia%20OR%20certificate%3APortugal)&rows=40&sort=numVotes%20DESC&tie=1')
    evaluate_query(4, 'http://localhost:8983/solr/shows/select?indent=true&q.op=OR&q=(cast%3A%22DB%22%20cast%3A%22Lesley%20Ann%22%20cast%3A%22jk%22%20cast%3AMatt)%20AND%20genres%3A%22Action%22&rows=30&sort=episodes%20ASC')
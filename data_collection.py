import time

import requests

base_url = 'https://media.githubusercontent.com/media/microsoft/SQL-Server-R-Services-Samples/master/PredictiveMaintenanceModelingGuide/Data'
datasets = ['machines', 'errors', 'maint', 'telemetry', 'failures']

for dataset in datasets:
    print('Fetching `{dataset}`...')
    start = time.time()
    r = requests.get(f'{base_url}/{dataset}.csv')
    assert r.status_code == 200
    with open(f'{dataset}.csv', 'w') as fp:
        fp.write(r.text)
    elapsed = time.time() - start
    print(f'`{dataset}` saved in {elapsed:.2f} seconds.\n')

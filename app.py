from google.cloud import bigquery

client = bigquery.Client()
bucket_name = 'bq_esun_output'
project = 'neat-motif-123006'
dataset_id = 'data_export'
table_id = 'dailykyc'
filename = 'dailykyc.csv'

destination_uri = 'gs://{}/{}'.format(bucket_name, filename)
dataset_ref = client.dataset(dataset_id, project=project)
table_ref = dataset_ref.table(table_id)

extract_job = client.extract_table(
    table_ref,
    destination_uri,
    location='US',
    )
extract_job.result()

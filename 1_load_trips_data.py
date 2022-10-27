from google.cloud import bigquery


# TODO : Change to your name
DATASET_NAME_PREFIX = '2022_temp_lippe'

PROJECT_ID = "jlr-dl-cat-training"
BUCKET_NAME = "2022-jlr-temp-lippe"
# GCS_URI = f"gs://{BUCKET_NAME}/dataset/trips/20180101/*.json"
# This uri for load data from 2018-01-02
GCS_URI = f"gs://{BUCKET_NAME}/dataset/trips/20180102/*.json"
TABLE_ID = f"{PROJECT_ID}.{DATASET_NAME_PREFIX}_raw_bikesharing.trips"

client = bigquery.Client()

def load_gcs_to_bigquery_event_data(GCS_URI, TABLE_ID, table_schema):
    job_config = bigquery.LoadJobConfig(
        schema=table_schema,
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        write_disposition = 'WRITE_APPEND'
        )

    load_job = client.load_table_from_uri(
        GCS_URI, TABLE_ID, job_config=job_config
    )

    load_job.result()
    table = client.get_table(TABLE_ID)

    print(f"Loaded {table.num_rows} rows to table {TABLE_ID}")

bigquery_table_schema = [
    bigquery.SchemaField("trip_id", "STRING"),
    bigquery.SchemaField("duration_sec", "INTEGER"),
    bigquery.SchemaField("start_date", "TIMESTAMP"),
    bigquery.SchemaField("start_station_name", "STRING"),
    bigquery.SchemaField("start_station_id", "STRING"),
    bigquery.SchemaField("end_date", "TIMESTAMP"),
    bigquery.SchemaField("end_station_name", "STRING"),
    bigquery.SchemaField("end_station_id", "STRING"),
    bigquery.SchemaField("member_gender", "STRING")
]
if __name__ == '__main__':
    load_gcs_to_bigquery_event_data(GCS_URI, TABLE_ID, bigquery_table_schema)

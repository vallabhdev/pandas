import io
import pandas as pd
from google.cloud import storage



gcp_key = 'gcp_key.json'
bucket_name = 'preserve_endangered_species_01'
file_name = 'Endangered_Species.csv'
upload_file_name = "testfile.txt"
# create storage client
client = storage.Client.from_service_account_json(gcp_key)

def read_data(client,bucket_name,file_name):
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    string_data = blob.download_as_string()
    csv_data = pd.read_csv(io.BytesIO(string_data))
    print(csv_data)

    print(
        "File {} read successfully  from Bucket  {}.".format(
            file_name, bucket_name
        )
    )
def upload_file(client,bucket_name,file_name):
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file_name)

read_data(client,bucket_name,file_name)
upload_file(client,bucket_name,upload_file_name)

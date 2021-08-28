from web3.beacon import Beacon
from minio import Minio
import json
import io
import api.access as ac

#ToDo: Add Production and Development Mode -> secure=False
#ToDo: Add Test functionalities
#ToDo: Add Try and Catch Functionalities
#ToDo: Add Logs

def extract_blocks(first_block_number: int, last_block_number: int,
                    bucket_name: str, object_name: str, object_folder: str) -> None:
    
    connectors = ac.Connectors()
    eth2_client = connectors.open_ethereum2()
    minio_client = connectors.open_minio()

    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)
    else:
        print(f"Bucket {bucket_name} already exists")


    def __upload_data(minio_client: Minio, bucket_name: str, object_name: str, data: json) -> None:
        minio_client.put_object(bucket_name = bucket_name,
                                object_name = object_name,
                                data = io.BytesIO(data),
                                length=len(data),
                                content_type = 'application/json')

    def __download_block_data(eth2_client: Beacon, block_number: int) -> bytes:

        return json.dumps(eth2_client.get_block(block_number), indent=2).encode('utf-8')


    for i in range(first_block_number, last_block_number+1):
        data = __download_block_data(eth2_client = eth2_client, block_number = i)
        __upload_data(minio_client = minio_client,
                    bucket_name = bucket_name,
                    object_name = f'{object_folder}/{object_name}_{i}.json',
                    data = data)

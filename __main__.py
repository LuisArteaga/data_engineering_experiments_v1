import sys
import extraction.ethereum as eth2


# todo: Creating API Service
# todo: Creating Batch Processing Service for API
# todo: Creating Streaming Processing Service for API
# todo: Creating Webscraping Service

if __name__ == "__main__":
    sys.path.append('/home/larte/projects/data_engineering_experiments_v1')
    
    BUCKET_NAME = "eth2"
    OBJECT_FOLDER = 'raw'
    OBJECT_NAME_BASE = 'eth2_block'

    eth2.extract_blocks(
                        first_block_number=0,
                        last_block_number=4,
                        bucket_name=BUCKET_NAME,
                        object_folder=OBJECT_FOLDER,
                        object_name=OBJECT_NAME_BASE
                        )

import sys
import extraction.ethereum as eth2
import time
import argparse

def main():
    sys.path.append('/home/larte/projects/data_engineering_experiments_v1')
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--bucket_name", help="define bucket name", type=str)
    parser.add_argument("--object_folder", help="define object folder", type=str)
    parser.add_argument("--object_name_base", help="define object name", type=str)
    parser.add_argument("--first_block_number", help="define start block number", type=int)
    parser.add_argument("--last_block_number", help="define end block number", type=int)
    args=parser.parse_args()

    BUCKET_NAME = args.bucket_name
    OBJECT_FOLDER = args.object_folder
    OBJECT_NAME_BASE = args.object_name_base
    FIRST_BLOCK_NUMBER = args.first_block_number
    LAST_BLOCK_NUMBER = args.last_block_number

    print(f"Start: block number {FIRST_BLOCK_NUMBER}")
    start = time.time()
    eth2.extract_blocks(
                        first_block_number=FIRST_BLOCK_NUMBER,
                        last_block_number=LAST_BLOCK_NUMBER,
                        bucket_name=BUCKET_NAME,
                        object_folder=OBJECT_FOLDER,
                        object_name=OBJECT_NAME_BASE
                        )
    
    end = time.time()
    
    print(f"End: block number {LAST_BLOCK_NUMBER}")
    print(f"Total time in seconds: {end - start}")
    print(f"Total blocks: {LAST_BLOCK_NUMBER - FIRST_BLOCK_NUMBER}")
    print(f"Seconds per block: {(end - start)/(LAST_BLOCK_NUMBER - FIRST_BLOCK_NUMBER)}")


if __name__ == "__main__":
    main()


#!/usr/bin/env python3
import os
from web3.beacon import Beacon
from minio import Minio

AUTH_DIRECTORY = '/home/larte/projects/data_engineering_experiments_v1/api/.auth/'


class Connectors:
    class VaultKeeper:
        def __init__(self):
            # Replace it later with JSON
            self.vaults = {'openweathermap.org': 'openweathermap.txt',
                            'infura.io': 'infura_endpoint.txt',
                            'min.io': 'minio_credentials.txt'}
        def get_secret(self, source):
            with open(os.path.join(AUTH_DIRECTORY, self.vaults[source])) as f:
                return f.read()

    def __init__(self):
        self.vault_keeper = self.VaultKeeper()

    def open_ethereum2(self):
        eht2_client = Beacon(base_url=self.vault_keeper.get_secret('infura.io'))
        
        return eht2_client
            
    def open_minio(self):
        MINIO_CREDENTIALS =  self.vault_keeper.get_secret('min.io').split() 

        minio_client = minio_client = Minio(
                                            "0.0.0.0:9000",
                                            access_key = MINIO_CREDENTIALS[0],
                                            secret_key = MINIO_CREDENTIALS[1],
                                            secure=False
                                            )
        return minio_client



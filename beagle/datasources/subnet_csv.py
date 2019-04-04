import os
from typing import Generator

import pandas as pd

from beagle.common.logging import logger
from beagle.datasources.base_datasource import DataSource
from beagle.transformers.subnet_transformer import SubnetTransformer


class SubnetCSV(DataSource):
    """Reads events in one by one from a Subnet CSV, and parses them into the GenericTransformer"""

    name = "Subnet CSV" # The name as it'll appear in the web GUI
    category = "Subnet" # The category this will output to.
    transformers = [SubnetTransformer] # The transformer this will send events to

    def __init__(self, subnet_csv: str) -> None:

        self._df = pd.read_csv(subnet_csv,sep=";")

        logger.info("Set up SubnetCSVs")


    def metadata(self) -> dict:
        return {}


    def events(self) -> Generator[dict, None, None]:
            for _, row in self._df.iterrows():

                yield {
                    "subnet_name": row['subnet_name'],
                    "address_range": row['address_range'],
                    "environment": row['environment'],
                    "cloud": row['cloud'],
                    "nsg_rules": row['nsg_rules']
                }

import ast
import re
from typing import Optional, Tuple

from beagle.common import split_path, logger
from beagle.nodes import Subnet
from beagle.transformers.base_transformer import Transformer


class SubnetTransformer(Transformer):
    name = "Subnet"

    def transform(self, event: dict) -> Optional[Tuple]:

        subn = Subnet(
            subnet_name = event['subnet_name'],
            address_range = event['address_range'],
            environment = event['environment'],
            cloud = event['cloud']
        )

        for elem in ast.literal_eval(event['nsg_rules']):
            target_sub = Subnet(subnet_name = elem[0], cloud = elem[1])
            raw_dic = elem[2]
            subn.can_connect_to[target_sub].append(priority=raw_dic['priority'],
                source_addr=raw_dic['source_addr'], source_port=raw_dic['source_port'],
                target_addr=raw_dic['target_addr'], target_port=raw_dic['target_port'],
                protocol=raw_dic['protocol'], nsg_name=raw_dic['nsg_name']
            )

        return (subn,)

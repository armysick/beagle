from collections import defaultdict
from typing import DefaultDict, List, Optional

from beagle.nodes import Edge, Node

class Nsg_Rules(Edge):
    __name__ = "Can Connect To"

    nsg_name: Optional[str]
    priority: Optional[str]
    source_addr: Optional[str]
    source_port: Optional[str]
    target_addr: Optional[str]
    target_port: Optional[str]
    protocol: Optional[str]

    def __init__(self) -> None:
        super().__init__()


class Subnet(Node):
    __name__ = "Subnet"
    __color__ = "#ADD8E6"  # blue

    subnet_name: Optional[str]
    address_range: Optional[str]
    environment: Optional[str]
    cloud: Optional[str]

    can_connect_to: DefaultDict["Subnet", Nsg_Rules]
    key_fields: List[str] = ["subnet_name", "cloud"]

    def __init__(
        self,
        subnet_name: str = None,
        address_range: str = None,
        environment: str = None,
        cloud: str = None
    ) -> None:
        self.subnet_name = subnet_name
        self.address_range = address_range
        self.environment = environment
        self.cloud = cloud

        self.can_connect_to = defaultdict(Nsg_Rules)

    @property
    def edges(self) -> List[DefaultDict]:
        return [self.can_connect_to]

    @property
    def _display(self) -> str:
        return self.subnet_name or super()._display

from collections.abc import Callable


import abc


from watch import WatchMe
from watch.core import AttributeControllerMeta
from watch.builtins import InstanceOf, SubclassOf, Container


class WatchABCMetaType(abc.ABCMeta, AttributeControllerMeta):
    pass


class WatchABCType(abc.ABC, WatchMe, metaclass=WatchABCMetaType):
    pass


NodeId = bytes
NodePayload = bytes


class UnidentifiedDAGNode(WatchABCType):

    data = InstanceOf(NodePayload)
    links = Container(InstanceOf(NodeId), container=list)

    def __init__(self, data, links):
        self.data = data
        self.links = links


class IdentifiedDAGNode(UnidentifiedDAGNode):

    id = InstanceOf(NodeId)

    def __init__(self, id_maker, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id_maker(self)


class AbstractDriver(WatchABCType):

    return_type = SubclassOf(IdentifiedDAGNode)
    node_identifier = InstanceOf(Callable)

    @abc.abstractmethod
    def store(self, data: NodePayload) -> NodeId:
        pass

    @abc.abstractmethod
    def lookup(self, node_id: NodeId) -> IdentifiedDAGNode:
        pass


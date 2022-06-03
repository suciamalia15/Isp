from interface.penolakan_operation import PenolakanOperation
from abc import ABC, abstractmethod

class DriverOperation(PenolakanOperation, ABC):
    
    @abstractmethod
    def menolak_pesanan(self) -> None:
        super().menolak_pesanan()
        pass
    
    @abstractmethod
    def mengantarkan_pesanan(self) -> None:
        pass 
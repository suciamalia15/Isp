from interface.penjual_operation import penjual_operation

class penjualController(PenjualOperation):

    def menolak_pesanan(self) -> None:
        print("penjual menolak pesanan karena stok habis")

    def menyiapkan_pesanan(self) -> None:
        print("penjual menyiapkan pesanan sesuai pilihan pembeli")
        
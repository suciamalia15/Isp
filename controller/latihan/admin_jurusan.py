from interface.tugas_admin_jurusan import TugasAdminJurusan

class AdminJurusan (TugasAdminJurusan) :

    def mencatat_kehadiran (self) -> None :
        print ("Rekab per semester dari semua dosen")

    def publikasi_jadwal(self) -> None :
        print ("Admin jurusan mempublikasi jadwal ujian")
        
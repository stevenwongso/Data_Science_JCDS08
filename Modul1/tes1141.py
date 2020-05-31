import datetime

hariDict ={
    'Monday' : 'Senin',
    'Tuesday' : 'Selasa',
    'Wednesday' : 'Rabu',
    'Thursday' : 'Kamis',
    'Friday' : 'Jumat',
    'Saturday' : 'Sabtu',
    'Sunday' : 'Minggu'
}

bulanDict ={
    'January' : 'Januari',
    'February' : 'Februari',
    'March' : 'Maret',
    'April' : 'April',
    'May' : 'Mei',
    'June' : 'Juni',
    'July' : 'Juli',
    'August' : 'Agustus',
    'September' : 'September',
    'October' : 'Oktober',
    'November' : 'November',
    'December' : 'Desember'
}
class idwaktu:
    def __init__(self) :
        self.x = datetime.datetime.now()
    def hari(self):
        y = self.x.strftime('%A')
        return hariDict[y]
    def bulan(self):
        y = self.x.strftime('%B')
        return bulanDict[y]

waktu = idwaktu()
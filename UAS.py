"""
Created on Wed Jul  7 21:36:45 2021
@author: ZAHRAH AMBAR SARI-20083000124 
"""

ulang = 'y'
while ulang == 'y':
    #Format Rp.
    def rp(uang):
            x = str(uang)
            if len(x) <= 3:
                return 'Rp. ' + x
            else:
                a = x[:-3]
                b = x[-3:]
                return rp(a) + '.' + b
    
    #Siapkan variabel
    tipe = ['1','2','3']
    uang = [2500000, 4500000, 6500000]
    bonus_is = [1/100, 3/100, 5/100]
    bonus_an = 2/100
    b_jbtn = 0.5
    b_pens = 15500
    b_org  = 3500
    
    print('***************************************************')
    print('-SLIP GAJI KARYAWAN CV.LOGOS-'.center(50))
    
    #Input tanggal
    from datetime import date
    x = date.today()
    print('              Tanggal :', x.strftime('%d %B %Y'))
    
    #Tampilkan inputan
    nama = input('Nama                  :')
    gol = input('Golongan              :')
    gen = input('Jenis Kelamin(L/P)    :')
    sts = input('Status Kawin(S/B)     :')
    print()
    
    #Hitung gaji
    i = 0
    while i<len(uang):
        if tipe[i] == gol:
            gaji = uang[i]
            tunj = bonus_is[i] 
        i+=1
        
    #Tunjangan istri    
    if gen == 'l' and sts =='s':
        tun_is = tunj * gaji
    else:
        tun_is = 0
        
    #Tunjangan anak
    if sts == 's':
        tun_an = bonus_an * gaji
    else:
        tun_an = 0
    
    #Gaji bruto
    bruto = gaji + tun_is + tun_an
    
    #Biaya jabatan
    jbtn = b_jbtn * bruto
    
    #Gaji netto
    netto = bruto - jbtn - b_pens - b_org
    
    #Tampilkan Hasil
    print('=============================================')
    print('Gaji Pokok            :', rp (int(gaji)))
    print('Tunjangan Istri       :', rp (int(tun_is)))
    print('Tunjangan Anak        :', rp (int(tun_an)))
    print('--> Gaji Bruto        :', rp (int(bruto)))
    print('=============================================')
    print('Biaya Jabatan         :', rp (int(jbtn)))
    print('Iuran Pensiun         :', rp (int(b_pens)))
    print('Iuran Organisasi      :', rp (int(b_pens)))
    print('--> Gaji Netto        :', rp (int(netto)))
    
    ulang = input('Ulangi Program? Y/T:')
    print()
    if ulang == 't':
        break


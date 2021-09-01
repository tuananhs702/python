import numpy as ny
so_lan_tung=10000
tung_dong_xu = ny.random.randint(2, size=so_lan_tung)
so_lan_0 = (tung_dong_xu == 0).sum()
so_lan_1 = (tung_dong_xu == 1).sum()
P_0=so_lan_0/so_lan_tung
P_1=so_lan_1/so_lan_tung
print(P_0)
print(P_1)

print('----')

def tung_xu():
    if ny.random.random()<0.6:
        return 0
    else:
        return 1
ket_qua=ny.zeros(so_lan_tung)
for i in range(so_lan_tung):
    ket_qua[i]=(tung_xu())

P_3=(ket_qua ==0).sum()/so_lan_tung
P_4=(ket_qua ==1).sum()/so_lan_tung
print(P_3)
print(P_4)

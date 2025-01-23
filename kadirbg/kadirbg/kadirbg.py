def faktoriyel(sayi):
    if sayi <= 1:
        return 1
    sonuc = 1
    for i in range(2, sayi + 1):
        sonuc *= i
    return sonuc

def kombinasyon(n, k):
    return faktoriyel(n) // (faktoriyel(k) * faktoriyel(n - k))

def bernstein_polinomu(i, n, t):
    return kombinasyon(n, i) * (t ** i) * ((1 - t) ** (n - i))

def bezier_nokta_hesapla(kontrol_noktalari, u, w):
    
    satir_sayisi = len(kontrol_noktalari)
    sutun_sayisi = len(kontrol_noktalari[0])

    nokta = [0.0, 0.0, 0.0]
    for i in range(satir_sayisi):
        for j in range(sutun_sayisi):
            b_u = bernstein_polinomu(i, satir_sayisi - 1, u)
            b_w = bernstein_polinomu(j, sutun_sayisi - 1, w)
            katsayi = b_u * b_w

            nokta[0] += katsayi * kontrol_noktalari[i][j][0]
            nokta[1] += katsayi * kontrol_noktalari[i][j][1]
            nokta[2] += katsayi * kontrol_noktalari[i][j][2]

    return nokta

kontrol_noktalari = [
    [[0.2, 0.6, 0.8], [0.2, 1.5, 0.4], [0.2, 1.0, 0.3]],
    [[0.5, 0.6, 0.8], [0.5, 1.5, 0.4], [0.5, 1.0, 0.3]],
    [[0.8, 0.6, 0.8], [0.8, 1.5, 0.4], [0.8, 1.0, 0.3]],
    [[1.4, 0.6, 0.8], [1.4, 1.5, 0.4], [1.4, 1.0, 0.3]],
    [[1.7, 0.6, 0.8], [1.7, 1.5, 0.4], [1.7, 1.0, 0.3]]
]
u1=0.25 
w1 =0.65
u2=1
w2 =0

P1 = bezier_nokta_hesapla(kontrol_noktalari, u1, w1)
P2 = bezier_nokta_hesapla(kontrol_noktalari, u2, w2)

delta = [P2[i] - P1[i] for i in range(3)]

print("Bezier Yüzeyi Üzerinde Nokta ve Delta Hesaplamaları\n")
print(f"P1: x={P1[0]:.2f}, y={P1[1]:.2f}, z={P1[2]:.2f}")
print(f"P2: x={P2[0]:.2f}, y={P2[1]:.2f}, z={P2[2]:.2f}")
print(f"Δx={delta[0]:.2f}, Δy={delta[1]:.2f}, Δz={delta[2]:.2f}")

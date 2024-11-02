from golpes import *
from revisao import *
from armas import *

if __name__ == "__main__":
    J1 = Jogador()
    J2 = Jogador()

    # s1 = Soco()
    # s1.golpear(J1)
    # print(J1)
    # c1 = Chute()
    # c1.golpear(J2)
    # print(J2)

    f1 = Faca()
    # for x in range(1,13):
    #     print(x)
    #     f1.agredir(J2)
    #     print(f1.lamina)
    #     print(J2)

    r1 = Revolver()
    # for y in range(1,8):
    #     print(y)
    #     r1.disparar(J1)
    #     print(r1.cartuchos)
    #     print(J1)

    # si = Soco_Ingles()
    # for z in range(1,13):
    #     print(z)
    #     si.agredir(J3)
    #     print(si.lamina)
    #     print(J3)

    # lc = Lanca_Chamas()
    # for y in range(1,21):
    #      print(y)
    #      lc.disparar(J4)
    #      print(lc.gas)
    #      print(J4)

    J1.armas.append(r1)
    J2.armas.append(r1)

    J1.armas[0].disparar(J2)
    J2.armas[0].disparar(J1)

    J1.bater(J2, Soco())
    J2.bater(J1, a=J2.armas[0])

    print(J1)
    print(J2)
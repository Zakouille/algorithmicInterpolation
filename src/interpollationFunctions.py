import sympy.polys.polyfuncs
import sympy


def Lagrange (Lx, Ly):
    X=sympy.symbols('X')
    if  len(Lx)!= len(Ly):
        print("ERROR")
        return 1
    y=0
    for k in range ( len(Lx) ):
        t=1
        for j in range ( len(Lx) ):
            if j != k:
                t=t* ( (X-Lx[j]) /(Lx[k]-Lx[j]) )
        y+= t*Ly[k]
    return y


if __name__ == "__main__":
    Lx = [-4, -2, 0, 1, 3]
    Ly = [16, 4, 0, 1, 9.]
    print (Lagrange(Lx, Ly))
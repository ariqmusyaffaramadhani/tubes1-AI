import random
import numpy as np

def chrom():
    X = []
    for i in range(8):
        X.append(random.randint(0,7))
    return X


def split_chrom(a_list):  #nilai X1 dan X2
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


def encode_func(x, mx, mn):
    up = 0
    dn = 0
    for i in range(len(x)):
        up = (x[i]*10**-i) + up
        dn = (9*10**-i) + dn
    return mn + (((mx-mn)*up)/dn)


def encodechrom(x): #x = get chromosom
    g1,g2 = split_chrom(x)
    x1 = encode_func(g1, 3, -3)
    x2 = encode_func(g2, 2, -2)
    return x1,x2

def calc_func(x1,x2):
    return (4-2*(x1**2)+ (x1**4)/3) * (x1**2+x1*x2+(-4 + 4*(x2**2))*x2**2)



def fitness(chrm): #inputan berupa individu
    x1,x2 = encodechrom(chrm)
    f = calc_func(x1,x2)
    return 1/(f + 1)


def populesyen():
    pop = []
    for i in range(10): #banyak populasi = 10
        pop.append(chrom())
    return pop

def populesyen_fitness(pop): #inputan berupa populasi
    fit = []
    for i in range(len(pop)): 
        fit.append(fitness(pop[i]))

    print('       kromosom           |       fitness')
    print('--------------------------|------------------------')
    for j in range(len(pop)):
        print(pop[j],' | ', fit[j]) 
        
    return fit


def paret_sel(pop):  #tournament_selection, menghasilkan 1 indv sebagai parent
    best = []
    for i in range 10
        krom = pop[random.randint(0,9)]  #generate individu random dari 0-9 (karena ada 10 populasi)
        if len(best)==0 or fitness(krom) > fitness(best)

#-------------------------------------------------MAIN_PROG--------------------------------------------------------

populesyen_fitness(populesyen())
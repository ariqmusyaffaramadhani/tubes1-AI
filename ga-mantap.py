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



def fitness(chrm): #inputan individu
    x1,x2 = encodechrom(chrm)
    f = calc_func(x1,x2)
    return 1/(f + 0.001)


def populesyen():
    pop = []
    for i in range(10): #banyak populasi = 10
        pop.append(chrom())
    return pop

# def populesyen_fitness(pop): #inputan berupa populasi
#     fit = []
#     for i in range(len(pop)): 
#         fit.append(fitness(pop[i]))
#     return fit


def parent_sel(pop):  #tournament_selection, menghasilkan 2 indv sebagai parent
    best1 = []
    best2 = []
    for i in range(10):
        krom = pop[random.randint(0,9)]  #generate individu random dari 0-9 (karena ada 10 populasi)
        if len(best1)==0 or fitness(krom) > fitness(best1):
            best1 = krom
    for i in range(10):
        krom = pop[random.randint(0,9)]  #generate individu random dari 0-9 (karena ada 10 populasi)
        if len(best2)==0 or fitness(krom) > fitness(best2) and krom != best1: #cari best2 tapi != best1
            best2 = krom
    return best1,best2


def crossover(p1,p2):
    tipot = random.randint(0,7)
    prob = 0.02 #probabilitas crossover
    x = random.random()
    if x >= prob:
        for i in range(tipot, 8):
            temp = p1[i]
            p1[i] = p2[i]
            p2[i] = temp
    return p1,p2 #child baru

def mutation(c1,c2):
    prob = 0.02 #probabilitas mutasi
    x = random.random()
    t1 = random.randint(0,7) #titik mutasi
    t2 = random.randint(0,7)
    if x >= prob:
        c1[t1] = random.randint(0,7)
        c2[t2] = random.randint(0,7)
    return c1,c2    


def newpop_generator(pop): #indikator generasi
    
    newpopulesyen = []
    for i in range(5): #mendapatkan mutasi sebanyak populasi(10)
        best1,best2 = parent_sel(pop)
        c1,c2 = crossover(best1,best2)
        m1,m2 = mutation(c1,c2)
        newpopulesyen.append(m1)
        newpopulesyen.append(m2)
    return newpopulesyen


def show_pop(pop):
    fit = []
    for i in range(len(pop)): 
        fit.append(fitness(pop[i]))
    print('       kromosom           |       fitness')
    print('--------------------------|------------------------')
    for j in range(len(pop)):
        print(pop[j],' | ', fit[j]) 
        

def show_krom(x):
    print('       kromosom           |       fitness')
    print('--------------------------|------------------------')
    print(x,' | ',fitness(x))



def catch_local_best(pop):
    best_fit = -9999
    
    for i in range(len(pop)):
        if fitness(pop[i]) > best_fit:
            best_fit = fitness(pop[i])
            best_local = pop[i]
    return best_local

# def find_best_global(arr_best_local):
#     best_fit = -9999
#     best = []
#     for i in range(len(arr_best_local)):
#         f = fitness(arr_best_local[i])
#         if f > best_fit:
#             best_fit = f
#             best = arr_best_local[i]
#     return best

def throw_indx(arr):
    x = -99999
    idx = 0
    for i in range(len(arr)):
        if arr[i] > x:
            x = arr[i]
            idx = i
    return idx

#-------------------------------------------------MAIN_PROG-------------------------------------------------#

best_chrm = []
best_fit  = []

pop = populesyen()
b = catch_local_best(pop)
best_chrm.append(b)
best_fit.append(fitness(b))
print("best local    : ",b)
print("fitness : ",fitness(b))
print()

new = newpop_generator(pop)
x = catch_local_best(new)
best_chrm.append(x)
best_fit.append(fitness(x))
print("best local    : ",x)
print("fitness : ",fitness(x))
print()

itr = 0
while itr!=5:
    new = newpop_generator(new)
    x = catch_local_best(new)
    best_chrm.append(x)
    best_fit.append(fitness(x))
    print("best local    : ",x)
    print("fitness : ",fitness(x))
    print()
    itr+=1


# print("----------isi best-------------")
# for i in range(len(best_chrm)):
#     print(best_chrm[i]," | ",best_fit[i])

idx = throw_indx(best_fit)
print("best    : ",best_chrm[idx])
print("fitness : ",best_fit[idx])
x1,x2 = encodechrom(best_chrm[idx])
print("x1,x2   : ",x1,x2)

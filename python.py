import matplotlib.pyplot as plt
import matplotlib as mpl

numlist = [int()]

def Syracuse(num = int()):
    x = []
    y = []
    flight_time = 0
    while num != 1:
        
        #verifie si la valeur tester cycle (4,2,1)
        if num in numlist or num % num == 1 and num % 2 == 0:
            print("La valeur cycle déjà")
            return
        else:
            #ajoute la suite de nombres à la liste
            numlist.append(num)
            
            #Conjoncture 3x + 1
            if num % 2 == 0:
                num = num/2
                flight_time += 1
                y.append(num)
            else:
                num = 3 * num + 1
                flight_time += 1
                y.append(num)
            #fin conjoncture
                
            x.append(flight_time)
        
        plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['r'])
        plt.plot(x, y, '-',)
        plt.xlabel('Temp de vol')
        plt.ylabel('Valeur testé')
        plt.pause(1e-5)

def main():
    incr = 0
    n = 1
    while True:
        incr += 1
        n += incr
        print(str(n))
        Syracuse(n)
        
        plt.gca().clear()
    
main()
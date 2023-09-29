import matplotlib.pyplot as plt
import matplotlib as mpl

def Syracuse(num = int()):
    numlist = []
    x = []
    y = []
    flight_time = 0
    
    while num != 1:
        #verifie si la valeur tester cycle (4,2,1)
        if num == 2:
            numlist.append(num)
            
        
        if num in numlist:
            #print("La valeur cycle déjà")
            break
            
        else:
            #ajoute la suite de nombres à la liste
            x.append(flight_time)
            flight_time += 1
            #Conjoncture 3x + 1
            if num % 2 == 0:
                num = num/2
            else:
                num = 3 * num + 1
        y.append(num)
        #fin conjoncture

#     plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['r'])
#     plt.yscale("log")
#     plt.plot(x, y, '-')
#     plt.xlabel('Temp de vol')
#     plt.ylabel('Valeur testé')
#     plt.pause(1e-5)     
#     print("flight time = ", flight_time)
    return flight_time

def main():
    
    best_flight_time = int()
    incr = 1
    n = 1
    longest_value = []
    while True:
        n += incr
        #print("Nombre qui va être testé:", n)
        flight_time = Syracuse(n)
        # ... #si flight_time est meilleur que le meilleur jusqu'ici, il devient le nouveau meilleur jusqu'ici
        if flight_time > best_flight_time:
            
            best_flight_time = flight_time
            longest_value.append(n)
            print("Meilleurs temp de vol est le nombre : " + str(n) + " Temps de vol : ",best_flight_time)

          #plt.gca().clear()
        if n > 1e10:
            
            print("La valeur " + str(longest_value[-1])+ " plus long temps de vol : ", best_flight_time)
            
            break

main()
#Syracuse(258)
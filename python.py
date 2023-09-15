import matplotlib.pyplot as plt

numlist = [int()]

def Syracuse(num = int()):
    x = []
    y = []
    flight_time = 0
    while num != 1:
    
        #verifie si la valeur tester cycle (4,2,1)
        if num in numlist:
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
        
        plt.plot(x, y, '-.')

    
def main():
    
    while True:
        n = int(input("Entré une valeur entière"))
        Syracuse(n)
        plt.show()
        plt.close()
    
main()

def main():

    sum = 0
    with open("day1-test.txt") as file:
        list1 = []
        list2 = []
        for line in file:
            parts = line.split()
            if len(parts) >= 2:  
                list1.append(int(parts[0])) 
                list2.append(int(parts[1]))  

        list1.sort()
        list2.sort()

        for i in range(len(list1)):
            temp = abs((int(list2[i])) - (int(list1[i])))
            sum += temp
            
        print(sum)

        
    
if __name__ == "__main__":
    main()
from collections import Counter

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

        counts = Counter(list2)

        for num in list1:
            sum += num * counts.get(num, 0)
            
        print(counts)
        
        
    
if __name__ == "__main__":
    main()

dictionary={}  # dicitonary={"name": count}  name ist key and count ist value

with open("C:/Users/Administrator/Desktop/Python kurs/Kursmaterialien/data/names.csv","r") as file:
    for line in file:
        
        liste= line.strip().split(",") # strip() = clean the ends // split() = cut into pieces and makea list out of every line
        
        #this if anweisung makes sure that th first line with id name count doent get in the dicitonary
        if liste[0] == "Id":
            continue
        
        
        #those are the two variables that will help filling the dicionary. name is the jkey in the dictionary and count would be the value
        name= liste[1]
        count=int(liste[5])
        
        
        # this if anweisung fills the dicionary up with new names. and if the same name exists already. it just add up the count of that name
        if name in dictionary:
            dictionary[name]= dictionary[name] + count  
        else:
            dictionary[name]= count
    
    highest_count=0
    name_with_highest_count=""
    
    # this is the outputshcleife gives a dictionary with names and the sum of all counts
    for key,value in dictionary.items():
        if highest_count< value:
            highest_count=value
            name_with_highest_count= key
       
    print(name_with_highest_count)
            
            
        
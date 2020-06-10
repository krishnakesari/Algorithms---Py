
# Each word is used as a key and number of occurrences as it's value

def wordcount(fname): 
    try: 
        fhand=open(fname) 
    except: 
        print('File cannot be opened') 
        exit() 

    count= dict() 
    for line in fhand: 
        words = line.split() 
        for word in words: 
            if word not in count: 
                count[word] = 1 
            else: 
                count[word] += 1 
    return(count) 

count=wordcount('alice.txt') 
filtered = { key:value for key, value in count.items() if value  < 13 and value > 3 } 

print(filtered)

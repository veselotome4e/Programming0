def hash_them(keys, values):

    dictionary = {}
  
    for i in range(len(keys)):
        if i > len(values)-1:
            dictionary[keys[i]] = None
        else:
            dictionary[keys[i]] = values[i]

    return dictionary
         
print(hash_them(["Ivan", "Maria"], [1, 2]))
print(hash_them(["Ivan", "Maria"], [1]))
        
    

        
        
    
    

def validate_password(password):
    spaces =[' '] 
    val = True
      
    if len(password) < 8: 
        val = False
        return val
          
    elif not any(char.isdigit() for char in password): 
        val = False
        return val
          
    elif not any(char.isupper() for char in password): 
        val = False
        return val
    
    elif not any(char.islower() for char in password): 
        val = False
        return val
    
    elif  any(char in spaces for char in password): 
        val = False
        return val
        
    else: 
        return val 

def reverse_string(s):
    
    if len(s) <= 1:
        return s
    else:
        
        first_char = s[0]
        remaining_chars = s[1:]
        
        reversed_remaining = reverse_string(remaining_chars)
        
        reversed_string = reversed_remaining + first_char
        return reversed_string


print(reverse_string("hello"))  
      

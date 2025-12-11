def format_base(n, base):
    """Format number according to base"""
    if base == '2':
        return bin(n)[2:] + ' b'
    elif base == '8':
        return oct(n)[2:] + ' o'
    elif base == '10':
        return str(n) + ' d'
    elif base == '16':
        return hex(n)[2:].upper() + ' hx'
    
def Base(usr_input:str):
    num , base = usr_input.split(' ')
    num = num.strip()
    base = base.strip()
    
    if base == 'b':
        decimal_num = int(num, 2)
    elif base == 'o':
        decimal_num = int(num, 8)
    elif base == 'd':
        decimal_num = int(num, 10)
    elif base == 'hx':
        decimal_num = int(num, 16)
    else:
        return ("Invalid number or base!")


# Build conversion dictionary
    output = {
        'Binary': format_base(decimal_num, '2'),
        'Octal': format_base(decimal_num, '8'),
        'Decimal': format_base(decimal_num, '10'),
        'Hexadecimal': format_base(decimal_num, '16')
    }   
    final = []
    for k, v in output.items():
        final.append(f"🔢 {k}: {v}")
    return final
    



def get_string(list:list):
    result = ''
    for i in list:
        result=result+i+'\n'
    return result
    
def define_calculate_base(string:str):
    num , base = string.split(' ')
    unit = base.strip().lower()
    
    if unit in ['b', 'o', 'd','hx']:
        
        return get_string(Base(string))

   
   

    else:
        return "Unknown unit! Check your input or use help_base"
    

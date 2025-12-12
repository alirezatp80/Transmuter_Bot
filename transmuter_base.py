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
    
def validation_input(string:str):
   while True:
        try:
            num , unit = string.split(' ')
            num = num.strip()
            unit = unit.strip()
            return num , unit
            
        except:
            return 'The input you entered is not valid','not valid'

def valid_base(num, base):
    if base == 'b':
        for i in num:
            if int(i)>1:
                
                raise Exception('base not correct!!!')
    elif base == 'o':
        for i in num:
            if int(i)>7:
                raise Exception('base not correct!!!')
    elif base == 'd':
        for i in num:
            int(i)
            
    elif base == 'hx':
       
        for i in num :
            if i not in  ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F']:
                raise Exception('base not correct!!!')
            
def check_base(num , base) : 
    try :
        valid_base(num , base)
        return num , base
    except:
        return 'the base is not correct!!' , "not valid"
    
    
def Base(usr_input:str):
    num , base =validation_input(usr_input)
    num , base = check_base(num , base)
    
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
    num , base =validation_input(string)
    num , base = check_base(num , base)
    base = base.lower()
    
    if base in ['b', 'o', 'd','hx']:
        
        return get_string(Base(string))

   
   

    else:
        return "Unknown base! Check your input or use help_base"
    

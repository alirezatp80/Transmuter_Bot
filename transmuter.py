def format_num(n):
    return f"{n:,.10f}".rstrip("0").rstrip(".")


#temperture
def Temperature(usr_input:str):
    num , unit = usr_input.split(' ')
    num = float(num)
    unit = unit.strip()
    if unit =='C':
        output = {
            'C' : num,
            'F' : (num*9.5) +32,
            'K' : num + 273.15
        }
        
    elif unit == 'F':
        output = {
            'C' : (num-32) /5.9,
            'F' : num ,
            'K' : ((num-32) /5.9) + 273.15
        }
        
    elif unit == 'K':
        output = {
            'C' : num - 273.15,
            'F' : ((num - 273.15)*9.5) +32,
            'K' : num   
        }
        
    else:
        return ("Invalid unit! Only  < C, F, K > are allowed.")
    
    final = []
    for u, val in output.items():
        final.append(f"🌡️ {format_num(num)} {unit} = {format_num(val)} {u}")
    return final
    
    
#Length
def Length(usr_input:str):
    num , unit = usr_input.split(' ')
    num = float(num)
    unit = unit.strip().lower()
    if unit == 'm':
        output = {
            'm': num,
            'km': num / 1000,
            'cm': num * 100,
            'mm': num * 1000,
            'mi': num / 1609.344,
            'yd': num * 1.0936133,
            'ft': num * 3.28084,
            'in': num * 39.3701
        }
    elif unit == 'km':
        output = {
            'm': num * 1000,
            'km': num,
            'cm': num * 100_000,
            'mm': num * 1_000_000,
            'mi': num / 1.609344,
            'yd': num * 1093.6133,
            'ft': num * 3280.84,
            'in': num * 39370.1
        }
    elif unit == 'cm':
        output = {
            'm': num / 100,
            'km': num / 100_000,
            'cm': num,
            'mm': num * 10,
            'mi': num / 160_934.4,
            'yd': num / 91.44,
            'ft': num / 30.48,
            'in': num / 2.54
        }
    elif unit == 'mm':
        output = {
            'm': num / 1000,
            'km': num / 1_000_000,
            'cm': num / 10,
            'mm': num,
            'mi': num / 1_609_344,
            'yd': num / 914.4,
            'ft': num / 304.8,
            'in': num / 25.4
        }
    elif unit == 'mi':
        output = {
            'm': num * 1609.344,
            'km': num * 1.609344,
            'cm': num * 160_934.4,
            'mm': num * 1_609_344,
            'mi': num,
            'yd': num * 1760,
            'ft': num * 5280,
            'in': num * 63_360
        }
    elif unit == 'yd':
        output = {
            'm': num / 1.0936133,
            'km': num / 1093.6133,
            'cm': num * 91.44,
            'mm': num * 914.4,
            'mi': num / 1760,
            'yd': num,
            'ft': num * 3,
            'in': num * 36
        }
    elif unit == 'ft':
        output = {
            'm': num / 3.28084,
            'km': num / 3280.84,
            'cm': num * 30.48,
            'mm': num * 304.8,
            'mi': num / 5280,
            'yd': num / 3,
            'ft': num,
            'in': num * 12
        }
    elif unit == 'in':
        output = {
            'm': num / 39.3701,
            'km': num / 39_370.1,
            'cm': num * 2.54,
            'mm': num * 25.4,
            'mi': num / 63_360,
            'yd': num / 36,
            'ft': num / 12,
            'in': num
        }
    else:
        return("Invalid unit! Only m, km, cm, mm, mi, yd, ft, in are allowed.")
    
    final = []
    for u, val in output.items():
        final.append(f"📏 {format_num(num)} {unit} = {format_num(val)} {u}")
    return final


def Weight(usr_input:str):
    num , unit = usr_input.split(' ')
    num = float(num)
    unit = unit.strip().lower()
    if unit == 'g':
        output = {
            'g': num,
            'kg': num / 1000,
            'mg': num * 1000,
            'lb': num / 453.59237,
            'oz': num / 28.3495231
        }
    elif unit == 'kg':
        output = {
            'g': num * 1000,
            'kg': num,
            'mg': num * 1_000_000,
            'lb': num * 2.20462,
            'oz': num * 35.274
        }
    elif unit == 'mg':
        output = {
            'g': num / 1000,
            'kg': num / 1_000_000,
            'mg': num,
            'lb': num / 453_592.37,
            'oz': num / 28_349.5231
        }
    elif unit == 'lb':
        output = {
            'g': num * 453.59237,
            'kg': num / 2.20462,
            'mg': num * 453_592.37,
            'lb': num,
            'oz': num * 16
        }
    elif unit == 'oz':
        output = {
            'g': num * 28.3495231,
            'kg': num / 35.274,
            'mg': num * 28_349.5231,
            'lb': num / 16,
            'oz': num
        }
    else:
        return("Invalid unit! Only g, kg, mg, lb, oz are allowed.")
    
    final = []
    for u, val in output.items():
        final.append(f"⚖️  {format_num(num)} {unit} = {format_num(val)} {u}")
    return final
    
    
def Volume(usr_input:str):
    num , unit = usr_input.split(' ')
    num = float(num)
    unit = unit.strip().lower()
    if unit == 'l' or unit == "L":
        output = {
            'L': num,
            'mL': num * 1000,
            'm3': num / 1000,
            'cm3': num * 1000,  # 1 L = 1000 cm³
            'gal': num / 3.78541,
            'fl_oz': num * 33.814
        }
    elif unit == 'ml'or unit == "mL":
        output = {
            'L': num / 1000,
            'mL': num,
            'm3': num / 1_000_000,
            'cm3': num,  # 1 mL = 1 cm³
            'gal': num / 3_785.41,
            'fl_oz': num / 29.5735
        }
    elif unit == 'm3':
        output = {
            'L': num * 1000,
            'mL': num * 1_000_000,
            'm3': num,
            'cm3': num * 1_000_000,
            'gal': num * 264.172,
            'fl_oz': num * 33_814
        }
    elif unit == 'cm3':
        output = {
            'L': num / 1000,
            'mL': num,
            'm3': num / 1_000_000,
            'cm3': num,
            'gal': num / 3785.41,
            'fl_oz': num / 29.5735
        }
    elif unit == 'gal':
        output = {
            'L': num * 3.78541,
            'mL': num * 3785.41,
            'm3': num / 264.172,
            'cm3': num * 3785.41,
            'gal': num,
            'fl_oz': num * 128
        }
    elif unit == 'fl_oz':
        output = {
            'L': num / 33.814,
            'mL': num * 29.5735,
            'm3': num / 33_814,
            'cm3': num * 29.5735,
            'gal': num / 128,
            'fl_oz': num
        }
    else:
        return("Invalid unit! Only L, mL, m3, cm3, gal, fl_oz are allowed.")
    
    final = []
    for u, val in output.items():
        final.append(f"🧪 {format_num(num)} {unit} = {format_num(val)} {u}")
    return final

def Speed(usr_input:str):
    num , unit = usr_input.split(' ')
    num = float(num)
    unit = unit.strip().lower()
    if unit == 'm/s':
        output = {
            'm/s': num,
            'km/h': num * 3.6,
            'mph': num * 2.23694
        }
    elif unit == 'km/h':
        output = {
            'm/s': num / 3.6,
            'km/h': num,
            'mph': num / 1.60934
        }
    elif unit == 'mph':
        output = {
            'm/s': num / 2.23694,
            'km/h': num * 1.60934,
            'mph': num
        }
    else:
        return("Invalid unit! Only m/s, km/h, mph are allowed.")
    
    final = []
    for u, val in output.items():
        final.append(f"💨 {format_num(num)} {unit} = {format_num(val)} {u}")
    return final

def Time(usr_input:str):
    num , unit = usr_input.split(' ')
    num = float(num)
    unit = unit.strip().lower()
    if unit == 's':
        output = {
            's': num,
            'min': num / 60,
            'h': num / 3600,
            'd': num / 86400
        }
    elif unit == 'min':
        output = {
            's': num * 60,
            'min': num,
            'h': num / 60,
            'd': num / 1440
        }
    elif unit == 'h':
        output = {
            's': num * 3600,
            'min': num * 60,
            'h': num,
            'd': num / 24
        }
    elif unit == 'd':
        output = {
            's': num * 86400,
            'min': num * 1440,
            'h': num * 24,
            'd': num
        }
    else:
        return("Invalid unit! Only s, min, h, d are allowed.")
    
    final = []
    for u, val in output.items():
        final.append(f"⏱️ {format_num(num)} {unit} = {format_num(val)} {u}")
    return final

def Data(usr_input:str):
    num , unit = usr_input.split(' ')
    num = float(num)
    unit = unit.strip()
    if unit == 'b':  
        output = {
            'b': num,              
            'B': num / 8,          
            'KB': num / (8*1024),
            'MB': num / (8*1024**2),
            'GB': num / (8*1024**3),
            'TB': num / (8*1024**4)
        }
    
    elif unit.lower() == 'kb':
        output = {
            'b': num * 1024 * 8,
            'B': num * 1024,
            'KB': num,
            'MB': num / 1024,
            'GB': num / (1024**2),
            'TB': num / (1024**3)
        }
    elif unit.lower() == 'mb':
        output = {
            'b': num * 1024**2 * 8,
            'B': num * 1024**2,
            'KB': num * 1024,
            'MB': num,
            'GB': num / 1024,
            'TB': num / (1024**2)
        }
    elif unit.lower() == 'gb':
        output = {
            'b': num * 1024**3 * 8,
            'B': num * 1024**3,
            'KB': num * 1024**2,
            'MB': num * 1024,
            'GB': num,
            'TB': num / 1024
        }
    elif unit.lower() == 'tb':
        output = {
            'b': num * 1024**4 * 8,
            'B': num * 1024**4,
            'KB': num * 1024**3,
            'MB': num * 1024**2,
            'GB': num * 1024,
            'TB': num
        }
    elif unit == 'B':
        output = {
            'b': num * 8,
            'B': num,
            'KB': num / 1024,
            'MB': num / (1024**2),
            'GB': num / (1024**3),
            'TB': num / (1024**4)
        }
    else:
        return("Invalid unit! Only b, B, KB, MB, GB, TB are allowed.")
    
    final = []
    for u, val in output.items():
        final.append(f"🧠 {format_num(num)} {unit} = {format_num(val)} {u}")
    return final

def get_string(list:list):
    result = ''
    for i in list:
        result=result+i+'\n'
    return result
    
def define_calculate(string:str):
    num , unit = string.split(' ')
    unit = unit.strip()
    
    if unit in ['C', 'F', 'K']:
        
        return get_string(Temperature(string))

    # Length
    elif unit.lower() in ['m','km','cm','mm','mi','yd','ft','in']:
        
        return get_string(Length(string))

    # Weight / Mass
    elif unit.lower() in ['g','kg','mg','lb','oz']:
       
         return get_string(Weight(string))

    # Volume
    elif unit.lower() in ['l','ml','m3','cm3','gal']:
        
         return get_string(Volume(string))

    # Speed
    elif unit.lower() in ['m/s','km/h','mph']:
        
         return get_string(Speed(string))

    # Time
    elif unit.lower() in ['s','min','h','d']:
        
         return get_string(Time(string))

    # Data
    elif unit in ['b','B','KB','MB','GB','TB']:
        
         return get_string(Data(string))

   

    else:
        return "Unknown unit! Check your input or use help_unit"
    

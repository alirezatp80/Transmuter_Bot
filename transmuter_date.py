import jdatetime 
from  hijridate import Gregorian , Hijri

def valid_input(string:str):
    try:
        year , month , day = map(int,string.split('-'))
        if month>12 or month <1:
            return False , 'month'
        if day<1 or day > 31 :
            return False , 'day'
        return True, (year,month,day)
        
    except:
        return False , 'format'


def Gregorian_date(string:str):
   is_valid , date = valid_input(string)
   if not is_valid:
       return f'❌ Invalid input: {date}'
   year , month , day = date
   try : 
       gregorian_date = Gregorian(year,month,day)
       
       persian_date = jdatetime.date.fromgregorian(date=gregorian_date)
       
       islamic_date = gregorian_date.to_hijri()
       
       return (
            f"📆 Gregorian: {gregorian_date.strftime('%Y-%m-%d')}\n"
            f"🌞 Persian (Jalali): {persian_date.strftime('%Y-%m-%d')}\n"
            f"🌙 Islamic (Hijri): {islamic_date.isoformat()}"
        )
   except Exception as e:
        return f"❌ Error: {str(e)}"
       
def Persian(string:str):
    is_valid , date = valid_input(string)
    if not is_valid:
       return f'❌ Invalid input: {date}'
    year , month , day = date
    
    try : 
        persian_date = jdatetime.date(year,month,day)
        
        gregorian_date =persian_date.togregorian()
        
        gregorian_simple = Gregorian(gregorian_date.year , gregorian_date.month , gregorian_date.day)
        islamic_date = gregorian_simple.to_hijri()
        
        return (
            f"📆 Gregorian: {gregorian_date.strftime('%Y-%m-%d')}\n"
            f"🌞 Persian (Jalali): {persian_date.strftime('%Y-%m-%d')}\n"
            f"🌙 Islamic (Hijri): {islamic_date.isoformat()}"
        )
    except Exception as e: 
         return f"❌ Error: {str(e)}"

def Islamic(string:str):
    isvalid , date = valid_input(string)
    if not isvalid:
        return f'❌ Invalid input: {date}'
    year , month , day = date 
    try:
        islamic_date = Hijri(year , month , day)
        
        gregorian_date = islamic_date.to_gregorian()
        
        jalali = jdatetime.GregorianToJalali(gregorian_date.year , gregorian_date.month,gregorian_date.day).getJalaliList()
        jyear , jmonth , jday = jalali
        persian_date = jdatetime.date(jyear,jmonth,jday)
        
        return (
            f"📆 Gregorian: {gregorian_date.strftime('%Y-%m-%d')}\n"
            f"🌞 Persian (Jalali): {persian_date.strftime('%Y-%m-%d')}\n"
            f"🌙 Islamic (Hijri): {islamic_date.isoformat()}"
        )
    except Exception as e:
        return f"❌ Error: {str(e)}"
        
        
        


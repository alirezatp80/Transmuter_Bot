help_unit = """
🌡️ Temperature Units:
  • Celsius (C)
  • Fahrenheit (F)
  • Kelvin (K)

📏 Length Units:
  • Meter (m)
  • Kilometer (km)
  • Centimeter (cm)
  • Millimeter (mm)
  • Mile (mi)
  • Yard (yd)
  • Foot (ft)
  • Inch (in)

⚖️ Weight / Mass Units:
  • Gram (g)
  • Kilogram (kg)
  • Milligram (mg)
  • Pound (lb)
  • Ounce (oz)


🧪 Volume Units:
  • Liter (L)
  • Milliliter (mL)
  • Cubic Meter (m3)
  • Cubic Centimeter(cm3)
  • Gallon (gal)

💨 Speed Units:
  • Meter per Second (m/s)
  • Kilometer per Hour (km/h)
  • Mile per Hour (mph)

⏱️ Time Units:
  • Second (s)
  • Minute (min)
  • Hour (h)
  • Day (d)

🧠 Data Units:
  • Bit (b)
  • Byte (B)
  • Kilobyte (KB)
  • Megabyte (MB)
  • Gigabyte (GB)
  • Terabyte (TB)

"""

help_base = """
🔢 Base Number Systems:
  • Binary (base 2) — 0b -> 1011 b
  • Octal (base 8) — 0o -> 14 o
  • Decimal (base 10) — 0d -> 12 d
  • Hexadecimal (base 16) — 0x -> 2F hx
"""

unit_page = """
📏 Please enter the value together with its unit.

🔹 ✅ Correct examples:
• 20 km
• 150 m
• 3.5 kg
• 12 cm
• 0.75 L

🔸 ❌ Incorrect examples:
• 20km        (missing space)
• km 20       (order is wrong)
• just 20     (unit missing)
• only "km"   (value missing)

📝 Format rule:
<number> <unit>

I'm ready! ✨

"""


base_page = """
🔢 Please enter the number together with its base.

🔹 ✅ Correct examples:
• 1010 b
• 247 d
• 1F hx
• 777 o
• FF hx

🔸 ❌ Incorrect examples:
• 1010b        (missing space)
• b 1010       (order is wrong)
• 1G hx         (invalid digit for hex)
• only 1010    (base missing)
• only "b"     (number missing)

📝 Format rule:
<number> <base>

🧠 Valid bases:
• b → Binary (base 2)
• d → Decimal (base 10)
• hx → Hexadecimal (base 16)
• o → Octal (base 8)

I'm ready! ✨
"""
date_page = """
📅 Please enter the date in the selected calendar.

🔹 Supported calendars:
• Gregorian  → میلادی
• Persian    → شمسی
• Islamic    → هجری قمری

🔹 ✅ Correct examples:
For Gregorian:
• 2024-12-01
• 1998-07-15

For Persian:
• 1402-05-20
• 1399-01-01

For Islamic:
• 1445-09-10
• 1430-01-01

🔸 ❌ Incorrect examples:
• 2024/12/01     (slashes not allowed)
• 1402-13-40     (invalid month/day)
• 15-07-2020     (wrong order)
• just “2024”    (incomplete)

📝 Format rule:
YYYY-MM-DD  
(Year – Month – Day)

⏳ After entering the date, I will convert it to all other calendars automatically.

I'm ready! ✨
"""

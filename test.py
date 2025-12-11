from transmuter import define_calculate
def test_define_calculate_full():
    test_cases = [
        # Temperature
        "0 C", "100 F", "273.15 K",
        
        # Length
        "1 m", "5 km", "12 cm", "100 mm", "2 mi", "3 yd", "10 ft", "24 in",
        
        # Weight / Mass
        "100 g", "2 kg", "500 mg", "1 lb", "8 oz",
        
        # Volume
        "1 L", "500 mL", "2 m3", "100 cm3", "3 gal",
        
        # Speed
        "10 m/s", "60 km/h", "30 mph",
        
        # Time
        "60 s", "15 min", "2 h", "1 d",
        
        # Data
        "8 b", "1 B", "2 KB", "5 MB", "1 GB", "0.5 TB",
        
       
    ]
    
    for case in test_cases:
        print(f"Input: {case}")
        try:
            result = define_calculate(case)
            print(f"Output:\n{result}\n{'-'*40}")
        except Exception as e:
            print(f"Error processing '{case}': {e}\n{'-'*40}")

# Run the full test
test_define_calculate_full()

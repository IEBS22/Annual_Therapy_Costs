def analyze_query(user_input):
    try:
        year, drug_name = user_input.split(',')
        year = int(year.strip())
        drug_name = drug_name.strip()
        
        if 1900 <= year <= 2100:  # Adjust range as needed
            return {"year": year, "drug_name": drug_name, "is_valid": True}
        else:
            return {"is_valid": False, "error": "Year out of valid range"}
    except ValueError:
        return {"is_valid": False, "error": "Invalid input. Please enter a valid year and drug name, separated by a comma."}

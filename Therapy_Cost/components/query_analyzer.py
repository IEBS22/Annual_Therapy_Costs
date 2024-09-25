def analyze_query(user_input):
    try:
        year = int(user_input)
        if 1900 <= year <= 2100:  # year rangle(flag check man kiya dal diya)
            return {"year": year, "is_valid": True}
        else:
            return {"is_valid": False, "error": "Year out of valid range"}
    except ValueError:
        return {"is_valid": False, "error": "Invalid input. Please enter a valid year."}
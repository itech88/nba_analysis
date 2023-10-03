def height_to_inches(height_str):
    feet, inches = map(int, height_str.split('-'))
    return feet * 12 + inches
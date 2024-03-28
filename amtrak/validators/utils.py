def count_character_types(code: str):
    """
    Counts the number of different types of characters in a string.
    
    Args:
        code (str): The string to count character types in.
    
    Returns:
        Tuple[int, int, int]: A tuple containing the counts of digits, letters,
                              and other characters in the string.
    """
    digit_count = 0
    alpha_count = 0
    other_count = 0
    
    for letter in code:
        if letter.isdigit():
            digit_count += 1
        elif letter.isalpha():
            alpha_count += 1
        else:
            other_count += 1
    
    return digit_count, alpha_count, other_count

def validate_passenger_counts(
    adults: int, seniors: int, youth: int, children: int, infants: int
):
    """
    Validates the counts of different passenger types for a booking.
    
    Args:
        adults (int): The number of adult passengers.
        seniors (int): The number of senior passengers.
        youth (int): The number of youth passengers.
        children (int): The number of child passengers.
        infants (int): The number of infant passengers.
    
    Raises:
        ValueError: If the total number of non-infant passengers exceeds 8 or if
                    the total number of passengers (including infants) exceeds 14.
    """
    non_infant_passengers = adults + seniors + youth + children
    
    if non_infant_passengers > 8:
        raise ValueError("Cannot book for more than 8 non-infant passengers")
    
    total_passengers = non_infant_passengers + infants
    
    if total_passengers > 14:
        raise ValueError("Cannot book for more than 14 passengers")
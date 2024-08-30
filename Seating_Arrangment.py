def is_safe(seating, person, seat, constraints):
    """
    Check if it is safe to assign the person to the given seat.
    
    seating: List of current seating arrangements.
    person: The person to be seated.
    seat: The current seat being considered.
    constraints: A dictionary of constraints, e.g., {(0, 1): False} means person 0 cannot sit next to person 1.
    
    Returns True if the seating is valid, False otherwise.
    """
    for i in range(seat):
        if (seating[i], person) in constraints and not constraints[(seating[i], person)]:
            return False
        if (person, seating[i]) in constraints and not constraints[(person, seating[i])]:
            return False
    return True

def backtrack_seating(seating, used, seat, n, constraints):
    """
    Use backtracking to find a valid seating arrangement.
    
    seating: List to store the current seating arrangement.
    used: List to track which people have already been seated.
    seat: The current seat being filled.
    n: Total number of people.
    constraints: Constraints for seating arrangements.
    
    Returns True if a valid seating arrangement is found, False otherwise.
    """
    if seat == n:
        return True
    
    for person in range(n):
        if not used[person] and is_safe(seating, person, seat, constraints):
            seating[seat] = person
            used[person] = True
            if backtrack_seating(seating, used, seat + 1, n, constraints):
                return True
            seating[seat] = -1
            used[person] = False
    
    return False

def seating_arrangement(n, constraints):
    """
    Find a valid seating arrangement using backtracking.
    
    n: Total number of people.
    constraints: Constraints for seating arrangements.
    
    Returns a list representing the seating arrangement if found, otherwise returns None.
    """
    seating = [-1] * n
    used = [False] * n
    if backtrack_seating(seating, used, 0, n, constraints):
        return seating
    else:
        return None

# Example usage
n = 4  # Number of people
constraints = {
    (0, 1): False,  # Person 0 cannot sit next to Person 1
    (1, 2): True,   # Person 1 must sit next to Person 2
}

arrangement = seating_arrangement(n, constraints)
if arrangement:
    print("Valid seating arrangement found:", arrangement)
else:
    print("No valid seating arrangement found.")

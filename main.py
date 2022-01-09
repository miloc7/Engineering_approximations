def sqrt_approximator(sqrt_formula, num, guess, precision, root_value):
    for iteration in range(precision):
        num = sqrt_formula(root_value, num, guess)
    return num

def sqrt_formula(root_value, num, guess):
    new_approximation = (1/root_value)((root_value(guess) + (num)/(guess^root_value)))
    return new_approximation

def smart_guesser(root_value, num):
    close_guess = 0
    close_guess_reached = False
    if close_guess_reached == False:
        for closest_guess in range(100):
            if closest_guess ^ root_value >= num:
                close_guess = closest_guess
                close_guess_reached = True
    return close_guess
def sqrt_approximator(num, guess, precision, root_value):
    for iteration in range(precision):
        guess = sqrt_formula(root_value, num, guess)
    return guess

def sqrt_formula(root_value, num, guess):
    new_approximation = float((1/root_value)*((root_value-1)*guess + num/guess**(root_value-1)))
    return new_approximation

def smart_guesser(root_value, num):
    close_guess = 0
    close_guess_reached = False
    if close_guess_reached == False:
        for closest_guess in range(100):
            if closest_guess ** root_value >= num:
                close_guess = closest_guess
                close_guess_reached = True
    return close_guess

print(sqrt_approximator(10, 3.5, 1000, 2))
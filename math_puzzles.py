from random import randint

MATH_SIGNS = ["+", "-", "*", "/"]


def generate_new_math_puzzle(exercise=1, difficulty="easy"):
    match exercise:
        case 1:
            return generate_new_level_one_math_puzzle(difficulty)
        case 2:
            return generate_new_level_two_math_puzzle(difficulty)
        case 3:
            return generate_new_level_three_math_puzzle(difficulty)
        case 4:
            return generate_new_level_four_math_puzzle(difficulty)



def generate_new_level_one_math_puzzle(difficulty):
    match difficulty:
        case "easy":
            maximum_number = 20
        case _:
            maximum_number = 20

    first_number = randint(1, maximum_number)
    second_number = randint(1, maximum_number)
    result_number = 0

    math_sign = MATH_SIGNS[randint(0, 3)]
    equality_sign = "="

    match math_sign:
        case "+":
            result_number = first_number + second_number
        case "-":
            result_number = first_number - second_number
        case "*":
            result_number = first_number * second_number
        case "/":
            while first_number % second_number != 0:
                second_number = randint(1, 20)

            result_number = first_number // second_number

    return {"firstNumber": first_number, "signSymbol": math_sign, "secondNumber": second_number,
            "equalitySymbol": equality_sign, "resultNumber": result_number}

def generate_new_level_two_math_puzzle(difficulty):
    match difficulty:
        case "easy":
            maximum_number = 20
        case _: # Ko _: nozīmē?
            maximum_number = 20

    first_number = randint(1, maximum_number)
    second_number = randint(1, maximum_number)
    result_number = 0

    math_sign = MATH_SIGNS[randint(0, 3)]
    equality_sign = "="

    match math_sign:
        case "+":
            result_number = first_number + second_number
        case "-":
            result_number = first_number - second_number
        case "*":
            result_number = first_number * second_number
        case "/":
            while first_number % second_number != 0:
                second_number = randint(1, 20)

            result_number = first_number // second_number

    return {"firstNumber": first_number, "signSymbol": math_sign, "secondNumber": second_number,
            "equalitySymbol": equality_sign, "resultNumber": result_number}

def generate_new_level_three_math_puzzle(difficulty):
    match difficulty:
        case "easy":
            maximum_number = 20
        case _: # Ko _: nozīmē?
            maximum_number = 20

    first_number = randint(1, maximum_number)
    second_number = randint(1, maximum_number)
    result_number = 0

    math_sign = MATH_SIGNS[randint(0, 3)]
    equality_sign = "="

    match math_sign:
        case "+":
            result_number = first_number + second_number
        case "-":
            result_number = first_number - second_number
        case "*":
            result_number = first_number * second_number
        case "/":
            while first_number % second_number != 0:
                second_number = randint(1, 20)

            result_number = first_number // second_number

    return {"firstNumber": first_number, "signSymbol": math_sign, "secondNumber": second_number,
            "equalitySymbol": equality_sign, "resultNumber": result_number}

def generate_new_level_four_math_puzzle(difficulty):
    match difficulty:
        case "easy":
            maximum_number = 20
        case _:
            maximum_number = 20

    first_number = randint(1, maximum_number)
    second_number = randint(1, maximum_number)
    result_number = 0

    math_sign = MATH_SIGNS[randint(0, 3)]
    equality_sign = "="

    match math_sign:
        case "+":
            result_number = first_number + second_number
        case "-":
            result_number = first_number - second_number
        case "*":
            result_number = first_number * second_number
        case "/":
            while first_number % second_number != 0:
                second_number = randint(1, 20)

            result_number = first_number // second_number

    return {"firstNumber": first_number, "signSymbol": math_sign, "secondNumber": second_number,
            "equalitySymbol": equality_sign, "resultNumber": result_number}


    
    #todo implementation

"""
exercise
1 - 1 + 1 = ? [result number]
2 - 1 + ? = 2 [second number]
3 - 1 ? 1 = 2 [sign]
4 - 1 + 1 ? 3 [equality sign]

difficulty 
easy   - 1  ->  20
medium - 10 ->  ??
hard   - 30 ->  ??
"""
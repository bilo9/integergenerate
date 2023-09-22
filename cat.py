
import itertools

def generate_combinations(number):
    
    digits = list(str(number))
    
    permutations = list(itertools.permutations(digits))
    
    combinations = [int(''.join(permutation)) for permutation in permutations]
    
    return combinations

number = input("hello eneter a 4 digit number: ")

combinations = generate_combinations(number)
print(combinations)

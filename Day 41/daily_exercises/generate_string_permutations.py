def generate_permutations(string):
    permutations = []
    if len(string) <= 1:
        return [string]

    # change the 'first' element and run the remaining string in the function
    for i in range(len(string)):

        current = string[i]
        remaining = string[:i] + string[i+1:]
        #create the list of permutations to generate through
        for p in generate_permutations(remaining):
            # append permutations
            permutations.append(current +p)
    return permutations



print(generate_permutations("abcde"))




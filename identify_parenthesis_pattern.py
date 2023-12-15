def check_pattern(input_pattern):
    # Early exit if odd number of braces.
    if len(input_pattern) % 2 != 0:
        print("unequal number of open and closing braces in the pattern detected")
        return False
    
    # define a list to store opening braces '('
    open_braces = []
        
    # Iterate through the string of braces and append open brace to the list.
    # Whenever we encounter a closing brace and the list is non-empty,
    # remove an open brace from the end of the list. Idea is that after the 
    # iteration is over, since we have equal number of open and closing braces,
    # if the pattern is proper the list will be empty.
    # eg: valid case:
    #           pattern = (()) . logic: two append and two pop from list.
    #     invalid case:
    #           pattern = ))((() logic: three append one pop. non zero size for list.
    for element in input_pattern:
        if element == '(':
           open_braces.append(element)

        # even if count is same, pattern can be wrong . eg: ())(
        # This means list shouldn't be empty while encountering a closing brace.    
        elif element == ')' and open_braces:
            open_braces.pop()
        elif element == ')' and not open_braces:
            print("Pattern is invalid")
            return False
    if not open_braces:
        print("Pattern is valid")
        return True
    else:
        return False

if __name__ == '__main__':
    try:
  
        # Inorder for the Github action to succed, Hardcoding the input with an example value.
        # Code verified with user prompted input already.
        #input_pattern = input("Enter the string pattern: ").strip()
        input_pattern = "(())()()"
        if input_pattern:
            if not all(char in ('(', ')') for char in input_pattern):
                raise ValueError("Only '(' and ')' allowed in the input pattern")
            checked_result = check_pattern(input_pattern)
            print(checked_result)
        else:
            raise ValueError("Input pattern is empty. \
                             Only '(' and ')' allowed in the input pattern")
    except ValueError as e:
        print(f"{e.args[0]}")

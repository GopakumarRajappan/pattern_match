def check_pattern(input_pattern):
    ## First check if the count of '(' and ')' are same. If not, no return False. 
    count_opening_braces = 0
    count_closing_braces = 0
    for char in input_pattern:
        if char == '(':
            count_opening_braces += 1
        if char == ')':
            count_closing_braces += 1
    
    if count_opening_braces != count_closing_braces:
        print("unequal number of open and closing braces in the pattern detected")
        return False
    else:
        # logic for validation has to go here

        # define a list to store opening braces '('
        list_of_open_braces = []
        
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
                list_of_open_braces.append(element)

            # even if count is same, pattern can be wrong . eg: ())(
            # This means list shouldn't be empty while encountering a closing brace.    
            elif element == ')' and len(list_of_open_braces) != 0:
                list_of_open_braces.pop()
            elif element == ')' and len(list_of_open_braces) == 0:
                print("Pattern is invalid")
                return False
        if len(list_of_open_braces) == 0:
            print("Pattern is valid")
            return True
        else:
            return False

if __name__ == '__main__':
    input_pattern = input("Enter the string pattern: ").strip()
    checked_result = check_pattern(input_pattern)
    print(checked_result)
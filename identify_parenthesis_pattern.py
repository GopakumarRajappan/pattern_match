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
        return False
    else:
        # logic for validation has to go here
        return True

if __name__ == '__main__':
    input_pattern = input("Enter the string pattern: ").strip()
    checked_result = check_pattern(input_pattern)
    if not checked_result:
        print("improper pattern proper")
    else:
        print("Proper pattern")
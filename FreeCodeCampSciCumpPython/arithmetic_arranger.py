def arithmetic_arranger(problems, show_answers=False):
    try:
        if len(problems) > 5:
            raise ValueError('Error: Too many problems.')
        
        # Declare variables
        top = ''
        bottom = ''
        equals = ''
        answers = ''
        spacer = '    '

        for problem in problems:
            elements = problem.split()
        
            # Limit operators to '+' and '-'
            if elements[1] not in ['+', '-']:
                raise ValueError('Error: Operator must be \'+\' or \'-\'.')

            # Each number must be a digit
            if not elements[0].isdigit() or not elements[2].isdigit():
                raise ValueError('Error: Numbers must only contain digits.')
        
            # Numbers must only be four digits
            if len(elements[0]) > 4 or len(elements[2]) > 4:
                raise ValueError('Error: Numbers cannot be more than four digits.')

            maxLen = max((len(val) for val in elements)) + 2
            print('maxLen', maxLen)

            top += elements[0].rjust(maxLen) + spacer
            bottom += elements[1] + elements[2].rjust(maxLen - 1) + spacer
            equals += '-' * maxLen + spacer

            if show_answers:
                if elements[1] == '+':
                    answer = int(elements[0]) + int(elements[2])
                else:
                    answer = int(elements[0]) - int(elements[2])
                answers += str(answer).rjust(maxLen) + spacer

        results = top.rstrip() + '\n' + bottom.rstrip() + '\n' + equals.rstrip()
        if show_answers:
            results += '\n' + answers.rstrip()

        return results
    except ValueError as e:
        return str(e)
    
problem = ["11 + 4", "3801 - 2999", "1 + 2"]

print(f'\n{arithmetic_arranger(problem, True)}\n')
   

#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
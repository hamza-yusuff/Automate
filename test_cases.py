import random

def generate_test():
    while True:
        function = input("Enter function name : ")
        while function=='':
            function = input("Enter a valid name : ")
        cases = int(input("Enter number of test cases : "))
        while cases==0:
            cases = int(input("Number of cases has to be > 0 : "))
        args = int(input("Enter number of args for the function : "))

        test_cases = []
        expected = []
        for i in range(cases):
            arguments = []
            for j in range(args):
                arguments.append(input("Enter the argument for {}th test ".format(i+1)))
            expected.append(input("Enter the expected result "))
            test_cases.append(arguments)

        for k in range(cases):
            argument_string = " ".join(test_cases[k])
            result = "(check-expect ({} {}) {})".format(function,argument_string,expected[k])
            print(result)
        
            
def generate_random(expect):
    while True:
        function = input("Enter function name : ")
        while function=='':
            function = input("Enter a valid name : ")
        cases = int(input("Enter number of test cases : "))
        while cases==0:
            cases = int(input("Number of cases has to be > 0 : "))
        args = int(input("Enter number of args for the function : "))

        limits = []
        for i in range(args):
            upper_lower = []
            upper_lower.append(input("Enter the lower limit for the argument number {} : ".format(i+1)))
            upper_lower.append(input("Enter the upper limit for the argument number {} : ".format(i+1)))
            limits.append(upper_lower)


        
        for k in range(cases):
            arguments = []
            
            for j in range(args):
                arguments.append(str(random.randint(int(limits[j][0]), int(limits[j][1]))))
                
            argument_string = " ".join(arguments)
            if expect == 1:
                expected = input("For the arguments {}, input the expected value : ".format(argument_string))
            else:
                expected = " "
            result = "(check-expect ({} {}) {})".format(function,argument_string,expected)
            print(result)


while True: 
    test_type = int(input("Enter the type of test you would like to perform "))

    if test_type ==1:
        expected_or_not = input("Would you like to put expected values ")
        exit_val = 0
        while True:
            generate_test()
            exit_val = input("Type 123 to exit the type of test otherwise press anything to continue")
    elif test_type == 2:
        expected_or_not = input("Would you like to put expected values ")
        exit_val = 0
        while exit_val != '123':
            generate_random(expected_or_not)
            exit_val = input("Type 123 to exit the type of test otherwise press anything to continue")
    else:
        print("Not a valid test type")

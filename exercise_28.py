def type_check(correct_type):
    def func(old):
        def new_fun(arg):
            if (isinstance(arg, correct_type)):
                return old(arg)
            else:
                print("Bad Type")
        return new_fun
    return func

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])
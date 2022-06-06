import functions as funcs

with open("function_list.txt") as f:
    function_name = f.read().split("\n")
    for name in function_name:
        try:
            eval("funcs." + name)()
        except SyntaxError:
            print("\"{}\" is not a function".format(name))

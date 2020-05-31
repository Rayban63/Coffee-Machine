first_num = float(input())
second_num = float(input())
operation = input()
no = ["mod", "div", "/"]
if second_num == (0.0 or 0) and operation in no:
    print("Division by 0!")
elif operation == "mod":
    print(first_num % second_num)
elif operation == "pow":
    print(first_num ** second_num)
elif operation == "*":
    print(first_num * second_num)
elif operation == "div":
    print(first_num // second_num)
elif operation == "/":
    print(first_num / second_num)
elif operation == "+":
    print(first_num + second_num)
elif operation == "-":
    print(first_num - second_num)
def main():
   print ("Welcome to PyCalculator  ^⁠_⁠^")
   print("\n")
   while True:
        user_input = input("ENTER: ")
        x = user_input.replace("x", "*").replace("÷", "/")
        result = eval(x)
        print(f"RESULT: {result}")


main()

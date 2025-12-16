try:
    # 1️⃣ ValueError – invalid number input
    num = int(input("Enter an integer: "))

    # 2️⃣ ZeroDivisionError – dividing by zero
    den = int(input("Enter a denominator: "))
    division_result = num / den
    print("Division:", division_result)

    # 3️⃣ TypeError – invalid type operation
    user_choice = input("Enter 'text' to trigger TypeError: ")
    if user_choice == "text":
        print(num + "abc")   # TypeError

    # 4️⃣ IndexError – accessing invalid list index
    lst = [10, 20, 30]
    idx = int(input("Enter list index (0-2): "))
    print("List value:", lst[idx])

    # 5️⃣ KeyError – missing dictionary key
    d = {"name": "Kiran", "role": "Developer"}
    key = input("Enter a dictionary key (name/role/other): ")
    print("Value:", d[key])

    # 6️⃣ FileNotFoundError
    fname = input("Enter a file name (wrong name to trigger error): ")
    f = open(fname, "r")
    print(f.read())
    f.close()

    # 7️⃣ AttributeError
    x = 10
    choice2 = input("Type 'attr' to trigger AttributeError: ")
    if choice2 == "attr":
        x.append(5)

    # 8️⃣ ModuleNotFoundError
    mod = input("Enter module name (wrong name to trigger error): ")
    exec(f"import {mod}")

    # 9️⃣ SyntaxError – using eval with wrong syntax
    code = input("Enter Python expression (wrong syntax to trigger error): ")
    print(eval(code))

    # 🔟 NameError – undefined variable
    choice3 = input("Type 'name' to trigger NameError: ")
    if choice3 == "name":
        print(undefined_variable)

# 🎯 10 Exception Handlers
except ValueError:
    print("❌ ValueError: Please enter a valid integer.")

except ZeroDivisionError:
    print("❌ ZeroDivisionError: Cannot divide by zero.")

except TypeError:
    print("❌ TypeError: Incompatible data types used.")

except IndexError:
    print("❌ IndexError: List index out of range.")

except KeyError:
    print("❌ KeyError: Key not found in dictionary.")

except FileNotFoundError:
    print("❌ FileNotFoundError: File does not exist.")

except AttributeError:
    print("❌ AttributeError: Invalid attribute or method.")

except ModuleNotFoundError:
    print("❌ ModuleNotFoundError: Module does not exist.")

except SyntaxError:
    print("❌ SyntaxError: Invalid Python syntax.")

except NameError:
    print("❌ NameError: Variable not defined.")

# ⭐ ELSE block (runs only when NO exception occurs)
else:
    print("✅ No errors detected! All operations successful.")

# ⭐ FINALLY block (runs always)
finally:
    print("✔ Program execution completed.")
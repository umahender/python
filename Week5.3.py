#3. Use the structure of exception handling all general purpose exceptions.
try:
    even_numbers = [2,4,6,8]
    print(even_numbers[5])
except ZeroDivisionError:
    print("Denominator cannot be 0.")
except IndexError:
    print("Index Out of Bound.")
finally:
    print("This is finally block.")



'''Output:Index Out of Bound
 This is finally block.'''
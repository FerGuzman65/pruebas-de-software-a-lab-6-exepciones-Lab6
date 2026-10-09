class MyException(Exception):
    pass

class ExceptionsDemo:
    
    def divide(self, a, b):
        try:
            result = a / b
            print("Division result:", result)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except TypeError:
            print("Error: Invalid type for division. Please provide numbers.")
            


    def access_list(self, lst, index):
        try:
            print("Element:", lst[index])
        except IndexError:
            print("Error: Index is out of bounds.")


    def access_dict(self, dic, key):
        try:
            print("Value:", dic[key])
        except KeyError:
            print("Error: Key does not exist in the dictionary.")

    def read_file(self, filename):
        try:
            with open(filename, "r") as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print("Error: File not found.")
        except IOError:
            print("Error: Could not read the file.")

    def access_attribute(self, obj):
        try:
            print(obj.tnonexistent_attribue)
        except AttributeError:
            print("Error: The object does not have that attribute.")

    def check_positive(self, number):
        try:
            if number < 0:
                raise MyException("The number must be positive.")
            else:
                print("Valid number:", number)
        except MyException as e:
            print(f"Error: {e}")

# Python - Everything is Object

This project is part of the Holberton School curriculum. It focuses on understanding the concept that in Python, everything is an object. This includes:

- Variables
- Data types (integers, strings, lists, etc.)
- Functions
- Classes

The goal is to gain a deeper understanding of how Python handles objects, memory management, and the underlying mechanisms that make Python a powerful and flexible programming language.
## Examples

### Variables as Objects
```python
a = 10
b = a
print(id(a))  # Output: Memory address of a
print(id(b))  # Output: Same memory address as a
```

### Data Types as Objects
```python
my_list = [1, 2, 3]
print(type(my_list))  # Output: <class 'list'>
```

### Functions as Objects
```python
def my_function():
    return "Hello, World!"

print(type(my_function))  # Output: <class 'function'>
```

### Classes as Objects
```python
class MyClass:
    pass

print(type(MyClass))  # Output: <class 'type'>
```
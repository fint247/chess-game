
class Bang():
    pass

B = Bang()
print(isinstance(B, Bang))





# #I never learned how to use kivy but i do know tkinter


# from tkinter import *
# import tkinter as tk

# r = tk.Tk() 
# r.title('Chess') 
# r.geometry('800x600-0+0')
# r.config(bg = 'white')
# counter = 0
# for x in range(3):
#     for y in range(3):
#       counter += 1
#       button1 = Button(r, text=f'{counter}', bg = 'white', fg = 'black') 
#       button1.grid(row = x+1, column = y+1) 



# r.mainloop() 

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# import functools


# def fibonacci(n):
#     if n < 2:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# def is_even(x):
#     return x % 2 == 0

# def print_string(x,y):
#    string_num = ''
#    string_num += (str(x)+'\n')
#    string_num += (str(y))
#    return string_num

# numbers = [x+1 for x in range(20)]

# fibonacci_seq = list(map(fibonacci, numbers))
# print(fibonacci_seq)

# fibonacci_seq = list(filter(is_even, fibonacci_seq))
# print(fibonacci_seq)

# fibonacci_seq = functools.reduce(print_string, fibonacci_seq)
# print(fibonacci_seq)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # d is a Directory object
# class D():
#    def __init__(self, first_names, last_names):
#       self.first_names = first_names
#       self.last_names = last_names
#       self.index = 0

#    def __iter__(self):
#       return self
   
#    def __next__(self):
#       if self.index < len(self.first_names):
#          result = f"{self.last_names[self.index]}, {self.first_names[self.index]}"
#          self.index += 1
#          return result
#       else:
#          raise StopIteration


# d = D(['caden','ben','jackson'],['Brooks','Parker', 'Meril'])

# for val in d:
#     print(val)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def is_prime(num: int):
   
#    for n in range(num):
#       prime_num = True
#       for x in range(n):
#          for y in range(n):
#             if x*y == n:
#                prime_num = False
#       if prime_num == True:
#          yield n


# prime_gen = is_prime(50)
# for num in prime_gen:
#     print(num)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# def my_decorator(f):
#    def wrapper_function(*args):
#       result = f(*args)
#       print('All done!')
#       print('One more time!')
#       result = f(*args)
#       print('All done!')
#       return result
#    return wrapper_function
   

# @my_decorator
# def say_hello():
#     print("Hello!")



# say_hello()


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# from typing import Protocol

# class Drivable(Protocol):
#   mileage: int
#   def drive(self, distance: int) -> None:
#     ...




# class Car():
#   def drive(self, distance: int) -> None: 
#       print(f"you drove {distance} meters")

# class Golfer():
#   def drive(self, distance: int) -> None:
#     print(f"you drove {distance} meters")


# bus_driver = Car()
# golfer = Golfer()

# bus_driver.drive(100_000)
# golfer.drive(123)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# from typing import List, Tuple

# def create_adjacency_list(edges: List[Tuple[int, int]]) -> List[set]:
#    nodes = set()
#    for edge in edges:
#       nodes.add(edge[0])
#       nodes.add(edge[1])
#    adj_list = [set() for i in range(len(nodes))]
#    for edge in edges:
#       u = edge[0]
#       v = edge[1]
#       adj_list[u].add(v)
#       adj_list[v].add(u)
#    return adj_list

# edges = [(0, 1), (0, 2), (1, 2)]
# g = create_adjacency_list(edges)I
# print(g)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# class Car:
#   def __init__(self, make, model, year):
#     self.make = make
#     self.model = model
#     self.year = year 

    
# car1 = Car('toyota', 'avalon', 1995)
# car2 = Car('tesla','cyber_truck', 2023)
# car3 = Car('BMW','328I', 2011)

# cars = [car1, car2, car3]

# def sort_year_L_to_H(cars):
#    sorted_cars = []
#    for x in cars:
#       sorted_cars.append(x.year)
#    sorted_cars.sort()
#    return sorted_cars

# def sort_make_L_to_H(cars):
#    sorted_cars = []
#    for x in cars:
#       sorted_cars.append(x.make)
#    sorted_cars.sort()
#    return sorted_cars

# def sort_model_H_to_L(cars):
#    sorted_cars = []
#    for x in cars:
#       sorted_cars.append(x.model)
#    sorted_cars.sort()
#    sorted_cars2 = []
#    for x in range(len(sorted_cars)):
#       sorted_cars2.append(sorted_cars[-1*(x+1)])

#    return sorted_cars2

# sorted_year = sort_year_L_to_H(cars)
# sorted_make = sort_make_L_to_H(cars)
# sorted_model = sort_model_H_to_L(cars)

# print(sorted_year)
# print(sorted_make)
# print(sorted_model)

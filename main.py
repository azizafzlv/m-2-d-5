"""
Постройка треугольника, нужно чтобы все условия для его
построения были учтены.
"""

# class TrianglrChecker:

#     def __init__(self, a, b, c) -> None:
#         self.__a = a
#         self.__b = b
#         self.__c = c

#     def is_triangle(self):
#         if isinstance(self.__a, str) or \
#             isinstance(self.__b, str) or \
#              isinstance(self.__c, str):
#              print('Нужно вводить только числа')
#         elif self.__a < 0 or self.__b < 0 or self.__c < 0:
#             print('С отрицательными числами ничего не выйдет')
#         elif (self.__a + self.__b) > self.__c and \
#               (self.__a + self.__c) > self.__b and \
#                 (self.__b + self.__c) > self.__a:
#             print('Треугольник можно построить')
#         else:
#              print('Жаль но из этого треугольника не сделать')


#     def set_a(self, value):
#         if not isinstance(value, str):
#             print('Метод принимает только числовые значения')
#         else:
#             self.__a = value

#     def get_a(self):
#         return self.__a
    

#     def set_b(self, value):
#             if not isinstance(value, str):
#                 print('Метод принимает только числовые значения')
#             else:
#                 self.__b = value

#     def get_b(self):
#         return self.__b
    

#     def set_c(self, value):
#             if not isinstance(value, str):
#                 print('Метод принимает только числовые значения')
#             else:
#                 self.__c = value

#     def get_c(self):
#         return self.__c
    

# triangle = TrianglrChecker(4, 6, 8)

# triangle.is_triangle()

"""
Площадь треугольника и круга
"""

# from math import pi

# class Shape:

#     def __init__(self, name) -> None:
#         self.name = name

#     def get_area(self):
#         pass



# class Triangle(Shape):

#     def __init__(self, name, height, a, b, c) -> None:
#         super().__init__(name)
#         self.__a = a
#         self.__b = b
#         self.__c = c
#         self.__height = height

#     def get_area(self):
#         return (1/2) * self.__a * self.__height


# class Circle(Shape):
#     def __init__(self, name, radius) -> None:
#         super().__init__(name)
#         self.__radius = radius

#     def get_area(self):
#         return pi * (pow(self.__radius, 2))


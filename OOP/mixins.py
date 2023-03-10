'Mixins'
# Миксины - это классы, которые будут использоваться для наследования, но от этих миксинов не создают объекты
# Для чего:
# 1. Вы хотите предоставить множество доп методов для класса
# 2. Вы хотите использовать одну корректную функцию во множестве разных классов

# class Machines:
#     def start_engine(self):
#         print('started engine!')

# class RadioMixin:
#     def play_radio(self):
#         print('music is playing')

# class Auto(RadioMixin, Machines):
#     pass

# class Plane(Machines):
#     pass

# class Train(RadioMixin, Machines):
#     pass

# obj = Auto()
# obj2 = Plane()
# obj3 = Train()

# obj.start_engine()
# obj2.start_engine()
# obj3.start_engine()

# obj.play_radio()
# obj3.play_radio()


# class FlyMixin:
#     def fly(self):
#         print('я могу летать')

# class WalkMixin:
#     def walk(self):
#         print('я могу плыть')

# class SwimMixin:
#     def swim(self):
#         print('я могу плыть')

# class Human(WalkMixin, SwimMixin):
#     name = 'человек'

#     def talk(self):
#         print('я могу говорить')

# class Fish(SwimMixin):
#     name = 'рыба'

# class Exocoetidae(SwimMixin, FlyMixin):
#     name = 'летучая рыба'
class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__memory * self.__cpu

    def __str__(self):
        return f'Оперативная память: {self.memory}, Тактовая частота: {self.cpu}'

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(f'“Идет звонок на номер {call_to_number}” с сим-карты-{sim_card_number} - '
              f'{self.__sim_cards_list[sim_card_number-1]}')

    def __str__(self):
        return f'Список сим-кард: {self.sim_cards_list}'

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    @staticmethod
    def use_gps(location):
        print(f'Маршрут до {location} построен!')

    def __str__(self):
        return f'Список сим-кард: {self.sim_cards_list}, ' \
               f'Оперативная память: {self.memory}, Тактовая частота: {self.cpu}'

nokia_phone = Phone(['O!', 'Beeline'])
simple_computer = Computer('5.1 GHz', 32)
simple2_computer = Computer('5 GHz', 64)
redmi_smartphone = SmartPhone('4.4 GHz', 32, ['Megafon', 'MTS'])
samsung_smartphone = SmartPhone('4.5 GHz', 68, ['MTS', 'TeLe2'])
redmi_smartphone.call(1, '+7 (742) 254-94-11')
nokia_phone.call(2, '+996 550 520 666')
redmi_smartphone.use_gps('Ош базар')

print(simple2_computer > samsung_smartphone)
print(simple2_computer == simple_computer)
print(redmi_smartphone != samsung_smartphone)
print(redmi_smartphone <= samsung_smartphone)


items_list = [simple_computer, nokia_phone, redmi_smartphone, samsung_smartphone]
for items in items_list:
    print(items)
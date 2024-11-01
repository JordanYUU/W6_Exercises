# class Restaurant:
#     '''A magical place for kids and grown-ups alike'''

#     def __init__(self, name, opened, type, service):
#         self.name = name
#         self.opened = opened
#         self.type = type
#         self.service = service

#     def 

class Restaurant:
    '''Restaurant referral starter kit'''

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def rest_desc(self):
        print(f'{self.name} serves {self.type}')

    def rest_open(self):
        print(f'{self.name} is open')

fb_rst = Restaurant('Freadbear\'s Family Diner', 'Pizza')
bb_rst = Restaurant('Bob\'s Burgers', 'Burgers')
cp_rst = Restaurant('Central Perk', 'Coffee')

# print(f'''
# {fb_rst.rest_desc}
# {fb_rst.rest_open}
# {bb_rst.rest_desc}
# {bb_rst.rest_open}
# {cp_rst.rest_desc}
# {cp_rst.rest_open}
# ''')

fb_rst.rest_desc()
fb_rst.rest_open()

bb_rst.rest_desc()
bb_rst.rest_open()

cp_rst.rest_desc()
cp_rst.rest_open()
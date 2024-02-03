class Setting():
    def __init__(self):
        self.auto_queen = True


setting = Setting()

font = 'bold' if setting.auto_queen == True else 'normal'
print(font)










# def new_color(setting, attribute,color):
#     setattr(setting, attribute, color)

# class Setting():
#     def __init__(self):
#         self.color = (255,255,255)
#         self.color2 = (100,100,100)
    
#     def change_color(self, attribute, color):
#         new_color(self, attribute, color)
#         # new_color(self.color2, color)

# set = Setting()
# print(set.color)

# set.change_color('color',(0,0,5))
# print(set.color)

# # # Python code for accessing attributes of class  
# # class emp:  
# #     name='Harsh'
# #     salary='25000'
# #     def show(self):  
# #         print (self.name)  
# #         print (self.salary)  
# # e1 = emp()  
# # # Use getattr instead of e1.name  
# # print (getattr(e1,'salary'))  
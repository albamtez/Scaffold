# def add(x,y):
#   return x+y

# x=1
# y=2
# result = add(x,y)

# print(f"this is the sum:{x},{y},{result}")
# dejandolo asi da error en lint porque estamos definiendo x e y que no se deberia hacer porque es como trampear las variables


# forma buena
def add1(x, y):
    return x + y


result = add1(1, 2)
print(f"esta es la buena en lint:1,2,{result}")

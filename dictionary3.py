car ={"brand":"ford","model":"mustang","year":1964,
"color": ["red","white","green"]}
x=car["color"]
print(x)
print(type(x))
###################################################
y=car.get("brand")
print(y)
print(type(y))
###################################################
a=car.keys()
print(a)
#################################################
b=car.values()
print(b)
################################################
c=car.items()
print(c)
##################################################
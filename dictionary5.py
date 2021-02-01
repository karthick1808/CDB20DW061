car={"brand":"ford","model":"mustang","year":"1964"}
print(car)
print(type(car))
car["color"] = "red"
print(car)
###################################################
car.update({"body type":"hard"})
print(car)
###################pop############################
car.pop("body type")
print(car)
##################################################
car.popitem()
print(car)
#####################################################
#car.clear()
#print(car)
#####################################################
#del car
#print(car)
###################COPY###############################
karthick=car.copy()
print(karthick)
###################COPY###############################
selvam=dict(car)
print(selvam)
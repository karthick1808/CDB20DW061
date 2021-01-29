fruits=("apple","cherry","strawberry","banana")
a=fruits[0]
b=fruits[1]
print(a)
print(b)
###################
#unpacking -> alternative method that will driectly assign the multiple list
#values to variable by its own method
(green,yellow,red,orange)=fruits
print(green)
print(orange)
print(yellow)
print(red)
##################
(g,y,*r)=fruits
print(g)
print(y)
print(r)
#################
(ge,*ye,re)=fruits
print(ge)
print(ye)
print(re)
################
(*gre,yel,red)=fruits
print(gre)
print(yel)
print(red)
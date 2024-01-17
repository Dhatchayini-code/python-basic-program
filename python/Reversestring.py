string="This is a programming world"
b=string.split()
print(b) //['this','is','a','programming','world']
a=a[-1: :-1] //[: :-1]--start,stop,step
print(a)  //['world','programming','a','is','this']
final=" ".join(a)
print(final) // world programming a is this (string wise)

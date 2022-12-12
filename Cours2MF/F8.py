# #name = "jean baptiste jean "
# def pseudo_name(name):
#    # separation_name=name.split()
#     separation_name_without_hyphen=""
#     initial_name=""
#     for i in name.split(" "):
        
#         separation_name_without_hyphen += name.split("-")
#     for i in  separation_name_without_hyphen:
#         initial_name+=i[0]

#     print(initial_name)
    
# pseudo_name("jean batis")
#Kreye yon fonksyon ki ap pran yon non an paramèt, epi ki retounen inisyal yo. Atansyon ak non konpoze ak tirè yo.



calling=[]
initial=""
name=input("your name::")
for i in name:
    name=name.replace(" ","-")
for i in name.split("-"):
    calling.append(i)
for i in calling:
    initial+=i[0]
print(initial)           

    

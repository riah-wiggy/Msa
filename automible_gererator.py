import automobile

#create an automiblie
auto1 = automobile.Autommbile("Mercury","Sable","1234",3.0,"Bob")
auto2 = automobile.Autommbile("Honda","Ford","23456",2.2, "Alice")

auto_list = []
auto_list.append(auto1)
auto_list.append(auto2)
#print each automobuile info
for auto in auto_list:
    print(auto.make)
    print(auto.model)
    print()
#print(auto1.make)
    #print(auto1.model)
   # print("\n")
   # print(auto2.make)
  #  print(auto2.model)
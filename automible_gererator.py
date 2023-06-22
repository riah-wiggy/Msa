import automobile

#create an automiblie
auto1 = automobile.Automobile("Mercury","Sable","1234",3.0,"Bob", 2000)
auto2 = automobile.Automobile("Honda","Accord","23456",2.2, "Alice", 2003)
#change auto2 year
#auto2.year = 2020-but we want to prevent this from happening by making our atributes derictly accesible we create methods to allow acces to those variables

#change auto1 owner
auto1.set_owner("Aryan")

auto_list = []
auto_list.append(auto1)
auto_list.append(auto2)
#print each automobuile info
for auto in auto_list:
    auto.print_data()

print(f"Auto1 is {auto1.get_age()} years old")
#print(auto1.make)
    #print(auto1.model)
   # print("\n")
   # print(auto2.make)
  #  print(auto2.model)
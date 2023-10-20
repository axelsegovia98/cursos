val lista1=List("juan", "miau")
val lista1=List[String]("juan", "miau")

val lista2=List("juan", 10)
val lista2=List[Any]("juan", 10)



lista1.last
lista1.head
lista1.length

lista1.isEmpty

val lista3 = List.fill(5)("alberto")

lista1.reverse

for (m <- lista1){println(m)}




val lista4 = List(1,5,8,6,3)

lista4 = lista4:+45
lista4 = 2+:lista4



val lista5 = List(5,43,3)

//Lista anidada
var lista6 = lista4::lista5

//Union de listas
var lista7 = lista4:::lista5
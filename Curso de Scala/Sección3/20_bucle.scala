// BUCLE


var x = 0

while (x < 10)
{
    println(x)
    x += 1
}

do 
{
    println(x)
    x += 1
} while (x < 10)


for (z <- 1 to 10)
{
    println(z)
    println(x)
}


for (z <- 1 until 10)
{
    println(z)
    println(x)
}

for (z <- 1 until 10 if z%2 == 0)
{
    println(z)
}

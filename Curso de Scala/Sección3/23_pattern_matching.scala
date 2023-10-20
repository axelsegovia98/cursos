//CASE

var color = "red"

color match {
    case "red" => println("Rojo")
    case "blue" => println("Azul")
    case "yellow" | "green" => println("Amarillo o Verde")
    case if(color == "black" || color == "white") => println("Amarillo o Verde")
    case _ => println("Otro color")
}


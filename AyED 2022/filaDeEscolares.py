Datos ->
            str -> nombre
            int -> altura
            int(1-5) -> grado
            char -> curso (A,B,C)

Proceso
Mostrar nombre de alumno y su posición en la fila

Al finalizar
Cantidad de alumnos en la fila separado por curso
El alumno más alto y el más bajo (solo de 5to año).
    Indicando posición en la fila
Promedio de altura

Otras Variables:
            Contador de alumnos
                c_tot
            Contador por curso
                c_ca: Curso A
                c_cb: Curso B
                c_cc: Curso C
            Flag:
                max_a: Max altura
                max_f: Max fila
                min_a: Min altura
                min_f Min fila
            Acumulador:
                alt_tot: Altura


Inicio
c_ca, c_cb, c_cc, max_a, max_f, min_a, min_f, alt_tot <- 0

esq 'Ingrese grado'
leer grado

Mientras (grado != 0)

    esq 'Ingrese Curso'
    leer curso

    esq 'Ingrese Nombre'
    leer nombre

    esq 'Ingrese Altura'
    leer altura

    c_tot += 1
    alt_tot += altura

    esq 'El alumno ', nombre, 'esta en la posición ', c_tot

    Segun (curso)
        Caso 'A':
            c_ca += 1
        Caso 'B':
            c_cb += 1
        Caso 'C':
            c_cc += 1
    FinSegun

    Si (grado == 5):

        Si (altura > max_a O max_a == 0)
            max_a <- altura
            max_f <- c_tot
        FinSi

        Si (altura < min_a O min_a == 0)
            min_a <- altura
            min_f <- c_tot
        FinSi
    FinSi

    esq 'Ingrese grado, 0 para terminar'
    leer grado

FinMientras


esq 'El total de alumnos en el curso A es ', c_ca
esq 'El total de alumnos en el curso B es ', c_cb
esq 'El total de alumnos en el curso C es ', c_cc


esq 'El alumno más alto de 5to grado mide ', min_a
    ' y está en la posición ', min_f
esq 'El alumno más bajo de 5to grado mide ', min_a
    ' y está en la posición ', min_f

esq 'El promedio de altura es de ', alt_tot/c_tot

Fin
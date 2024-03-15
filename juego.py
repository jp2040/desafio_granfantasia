import random  # Importar el módulo random para generar números aleatorios
from personaje import Personaje  # Importar la clase Personaje del módulo personaje

class Juego:
    """
    Clase que representa el juego "Gran Fantasía".

    Métodos:
        iniciar_juego(): Método estático para iniciar el juego.
    """

    @staticmethod
    def iniciar_juego():
        """
        Inicia el juego "Gran Fantasía".

        Este método permite al jugador crear un personaje, enfrentarse a un orco y tomar decisiones durante el juego.
        """
        print("¡Bienvenido a Gran Fantasía!")
        nombre_personaje = input("Por favor indique nombre de su personaje: ")
        personaje = Personaje(nombre_personaje)  # Crear un nuevo personaje con el nombre proporcionado
        print(personaje)  # Mostrar información del personaje creado

        orco = Personaje("Orco")  # Crear un orco como oponente del jugador

        while True:
            probabilidad = Personaje.calcular_probabilidad(personaje, orco)  # Calcular la probabilidad de victoria del personaje sobre el orco
            opcion = Personaje.mostrar_dialogo_enfrentamiento(personaje, orco, probabilidad)  # Mostrar el diálogo de enfrentamiento

            if opcion == "1":  # El jugador decide atacar al orco
                resultado = random.uniform(0, 1)  # Generar un número aleatorio entre 0 y 1 para determinar el resultado del enfrentamiento
                if resultado <= probabilidad:  # Si el resultado está dentro de la probabilidad de victoria
                    print("¡Le has ganado al orco, felicidades!")
                    personaje.asignar_experiencia(50)  # El personaje gana experiencia
                    orco.asignar_experiencia(-30)  # El orco pierde experiencia
                else:
                    print("¡Oh no! ¡El orco te ha ganado!")
                    personaje.asignar_experiencia(-30)  # El personaje pierde experiencia
                    orco.asignar_experiencia(50)  # El orco gana experiencia
            elif opcion == "2":  # El jugador decide huir
                print("¡Has huido! El orco ha quedado atrás.")
                break  # Salir del bucle del juego
            else:
                print("Opción inválida. Por favor seleccione 1 o 2.")

            print(personaje)  # Mostrar información del personaje después del enfrentamiento
            print(orco)  # Mostrar información del orco después del enfrentamiento

if __name__ == "__main__":
    Juego.iniciar_juego()  # Iniciar el juego cuando el script se ejecuta directamente

class Personaje:
    """
    Clase que representa un personaje en un juego.

    Attributes:
        nombre (str): El nombre del personaje.
        nivel (int): El nivel del personaje, comienza en 1.
        experiencia (int): La experiencia del personaje, comienza en 0.
    """

    def __init__(self, nombre):
        """
        Inicializa una instancia de Personaje con el nombre proporcionado.

        Args:
            nombre (str): El nombre del personaje.
        """
        self.nombre = nombre
        self.nivel = 1  # El personaje comienza en el nivel 1
        self.experiencia = 0  # El personaje comienza con 0 experiencia

    def __str__(self):
        """
        Retorna una representación de cadena del personaje.

        Returns:
            str: Representación de cadena del personaje.
        """
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"

    def obtener_estado(self):
        """
        Retorna el estado del personaje.

        Returns:
            tuple: Una tupla con el nombre, nivel y experiencia del personaje.
        """
        return self.nombre, self.nivel, self.experiencia

    def asignar_experiencia(self, exp):
        """
        Asigna experiencia al personaje y actualiza su nivel según sea necesario.

        Args:
            exp (int): La cantidad de experiencia a asignar.
        """
        self.experiencia += exp
        while self.experiencia >= 100:
            self.nivel += 1
            self.experiencia -= 100
        while self.experiencia < 0 and self.nivel > 1:
            self.nivel -= 1
            self.experiencia += 100

    def __lt__(self, otro_personaje):
        """
        Compara el nivel de este personaje con el nivel de otro personaje.

        Args:
            otro_personaje (Personaje): El otro personaje a comparar.

        Returns:
            bool: True si el nivel de este personaje es menor que el nivel del otro personaje, False de lo contrario.
        """
        return self.nivel < otro_personaje.nivel

    def __gt__(self, otro_personaje):
        """
        Compara el nivel de este personaje con el nivel de otro personaje.

        Args:
            otro_personaje (Personaje): El otro personaje a comparar.

        Returns:
            bool: True si el nivel de este personaje es mayor que el nivel del otro personaje, False de lo contrario.
        """
        return self.nivel > otro_personaje.nivel

    @staticmethod
    def calcular_probabilidad(personaje, orco):
        """
        Calcula la probabilidad de victoria del personaje sobre un orco.

        Args:
            personaje (Personaje): El personaje que se enfrenta al orco.
            orco (Personaje): El orco que se enfrenta al personaje.

        Returns:
            float: La probabilidad de victoria del personaje sobre el orco.
        """
        if personaje < orco:
            return 0.33
        elif personaje > orco:
            return 0.66
        else:
            return 0.5

    @staticmethod
    def mostrar_dialogo_enfrentamiento(personaje, orco, probabilidad):
        """
        Muestra el diálogo de enfrentamiento entre el personaje y un orco.

        Args:
            personaje (Personaje): El personaje que se enfrenta al orco.
            orco (Personaje): El orco que se enfrenta al personaje.
            probabilidad (float): La probabilidad de victoria del personaje sobre el orco.

        Returns:
            str: La opción seleccionada por el jugador.
        """
        print("¡Oh no!, ¡Ha aparecido un Orco!")
        print(f"Con tu nivel actual, tienes {probabilidad * 100}% de probabilidades de ganarle al Orco.")
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        print("¿Qué deseas hacer?")
        print("1. Atacar")
        print("2. Huir")
        opcion = input()
        return opcion

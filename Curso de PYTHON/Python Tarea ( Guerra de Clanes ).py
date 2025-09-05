import random

class Guerrero:
    def __init__(self, nombre, vida, ataque, defensa, tipo):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.tipo = tipo

    def atacar(self, objetivo):
        daño = max(0, self.ataque - objetivo.defensa)
        objetivo.recibir_daño(daño)

    def recibir_daño(self, valor):
        self.vida -= valor
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nombre} recibió {valor} de daño. Vida restante: {self.vida}")


    def curarse(self):
        curación = 10
        self.vida += curación
        print(f"{self.nombre} se curó {curación} puntos. Vida actual: {self.vida}")

    def mostrar_estado(self):
        print(f"{self.nombre} ({self.tipo}) - Vida: {self.vida}, Ataque: {self.ataque}, Defensa: {self.defensa}")

class Arquero(Guerrero):
    def __init__(self, nombre):
        super().__init__(nombre, vida=60, ataque=25, defensa=5, tipo="Arquero")

class Espadachin(Guerrero):
    def __init__(self, nombre):
        super().__init__(nombre, vida=80, ataque=20, defensa=10, tipo="Espadachín")

class Mago(Guerrero):
    def __init__(self, nombre):
        super().__init__(nombre, vida=50, ataque=30, defensa=3, tipo="Mago")

    def curarse(self):
        curación = 20
        self.vida += curación
        print(f"{self.nombre} usó magia para curarse {curación} puntos. Vida actual: {self.vida}")

class Clan:
    def __init__(self, nombre, estrategia="aleatoria"):
        self.nombre = nombre
        self.lista_guerreros = []
        self.estrategia = estrategia

    def agregar_guerrero(self, guerrero):
        self.lista_guerreros.append(guerrero)

    def seleccionar_guerrero(self):
        vivos = [g for g in self.lista_guerreros if g.vida > 0]
        return random.choice(vivos) if vivos else None

    def atacar_clan(self, objetivo_clan):
        atacante = self.seleccionar_guerrero()
        defensor = objetivo_clan.seleccionar_guerrero()
        if atacante and defensor:
            print(f"{atacante.nombre} del clan {self.nombre} ataca a {defensor.nombre} del clan {objetivo_clan.nombre}")
            atacante.atacar(defensor)

    def estado_clan(self):
        print(f"Estado del clan {self.nombre}:")
        for guerrero in self.lista_guerreros:
            guerrero.mostrar_estado()

    def esta_derrotado(self):
        return all(g.vida <= 0 for g in self.lista_guerreros)


class Batalla:
    def __init__(self, clan1, clan2):
        self.clan1 = clan1
        self.clan2 = clan2

    def iniciar(self):
        turno = 1
        while not self.verificar_ganador():
            print(f"\n🔄 Turno {turno}")
            self.turno()
            turno += 1

    def turno(self):
        self.clan1.atacar_clan(self.clan2)
        if not self.clan2.esta_derrotado():
            self.clan2.atacar_clan(self.clan1)

    def verificar_ganador(self):
        if self.clan1.esta_derrotado():
            print(f"\n🏆 ¡El clan {self.clan2.nombre} ha ganado la batalla!")
            return True
        elif self.clan2.esta_derrotado():
            print(f"\n🏆 ¡El clan {self.clan1.nombre} ha ganado la batalla!")
            return True
        return False
    

clan_azul = Clan("Azul")
clan_rojo = Clan("Rojo")

clan_azul.agregar_guerrero(Arquero("Robin"))
clan_azul.agregar_guerrero(Mago("Merlín"))
clan_azul.agregar_guerrero(Espadachin("Arturo"))

clan_rojo.agregar_guerrero(Arquero("Legolas"))
clan_rojo.agregar_guerrero(Mago("Gandalf"))
clan_rojo.agregar_guerrero(Espadachin("Boromir"))

batalla = Batalla(clan_azul, clan_rojo)
batalla.iniciar()


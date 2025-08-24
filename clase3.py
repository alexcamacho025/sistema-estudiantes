class SerVivo:
    def __init__(self, nombre):
        self.nombre = nombre

    def respirar(self):
        print(f"{self.nombre} está respirando...")

class Persona(SerVivo):
    def __init__(self, nombre, edad):
        super().__init__(nombre)
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, codigo):
        super().__init__(nombre, edad)
        self.codigo = codigo

    def estudiar(self):
        print(f"{self.nombre} está estudiando...")

    def __str__(self):
        return f"Estudiante: {self.nombre}, {self.edad} años, Código: {self.codigo}"

class SistemaEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self):
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        codigo = input("Ingrese el código: ")
        estudiante = Estudiante(nombre, edad, codigo)
        self.estudiantes.append(estudiante)
        print(" Estudiante registrado con éxito.\n")

    def mostrar_estudiantes(self):
        if not self.estudiantes:
            print("⚠️ No hay estudiantes registrados.\n")
        else:
            print("📋 Lista de estudiantes:")
            for e in self.estudiantes:
                print(e)
            print()

    def buscar_estudiante(self):
        codigo = input("Ingrese el código del estudiante: ")
        for e in self.estudiantes:
            if e.codigo == codigo:
                print(" Estudiante encontrado:")
                print(e, "\n")
                return
        print(" Estudiante no encontrado.\n")

    def menu(self):
        while True:
            print("===== Sistema de Estudiantes =====")
            print("1. Agregar estudiante")
            print("2. Mostrar estudiantes")
            print("3. Buscar estudiante")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_estudiante()
            elif opcion == "2":
                self.mostrar_estudiantes()
            elif opcion == "3":
                self.buscar_estudiante()
            elif opcion == "4":
                print("👋 Saliendo del sistema...")
                break
            else:
                print(" Opción no válida.\n")


if __name__ == "__main__":
    sistema = SistemaEstudiantes()
    sistema.menu()

import pickle

class Usuario:
    def __init__(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario

class ManejadorUsuarios:
    def __init__(self, archivo):
        self.archivo = archivo
        self.usuarios = self.cargar_usuarios()

    def crear_usuario(self, nombre_usuario):
        nuevo_usuario = Usuario(nombre_usuario)
        self.usuarios.append(nuevo_usuario)
        self.guardar_usuarios()
        print(f"El usuario '{nombre_usuario}' ha sido creado exitosamente.")

    def guardar_usuarios(self):
        with open(self.archivo, "wb") as f:
            pickle.dump(self.usuarios, f)

    def cargar_usuarios(self):
        try:
            with open(self.archivo, "rb") as f:
                usuarios = pickle.load(f)
        except FileNotFoundError:
            usuarios = []
        return usuarios

    def obtener_usuarios(self):
        return self.usuarios

    def borrar_usuario(self, nombre_usuario):
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario:
                self.usuarios.remove(usuario)
                self.guardar_usuarios()
                print(f"El usuario '{nombre_usuario}' ha sido eliminado.")
                return
        print(f"El usuario '{nombre_usuario}' no existe.")

# Ejemplo de uso
manejador = ManejadorUsuarios("usuarios.pkl")

# Crear usuario
manejador.crear_usuario("usuario1")

# Obtener usuarios
usuarios = manejador.obtener_usuarios()
for usuario in usuarios:
    print(usuario.nombre_usuario)

# Borrar usuario
manejador.borrar_usuario("usuario1")

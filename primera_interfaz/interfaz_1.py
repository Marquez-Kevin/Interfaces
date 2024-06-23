import tkinter as tk
from tkinter import font, messagebox
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import config_ventana as util_vent


class FormularioMaestroDesign(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.biblioteca = Biblioteca()  # Instancia de la biblioteca
        
        self.config_window()
        self.paneles()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.controles_cuerpo()
    
    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Python GUI')
        
        w, h = 1024, 600        
        util_vent.centrar_ventana(self, w, h)        

    def paneles(self):        
        # Crear paneles: barra superior, menú lateral y cuerpo principal
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')      

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False) 
        
        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
    
    def controles_barra_superior(self):
        # Configuración de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="Biblioteca")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        # Etiqueta de informacion
        self.labelInfo = tk.Label(self.barra_superior, text="Kevin Marquez Arenas")
        self.labelInfo.config(fg="#fff", font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelInfo.pack(side=tk.RIGHT)
    
    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
         
        # Etiqueta de perfil
        self.labelPerfil = tk.Label(self.menu_lateral, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        # Botones del menú lateral
        self.buttonRegistrarLibro = tk.Button(self.menu_lateral, command=self.mostrar_formulario_registrar_libro)
        self.buttonRegistrarUsuario = tk.Button(self.menu_lateral, command=self.mostrar_formulario_registrar_usuario)
        self.buttonRealizarPrestamo = tk.Button(self.menu_lateral, command=self.mostrar_formulario_realizar_prestamo)
        self.buttonMostrarLibros = tk.Button(self.menu_lateral, command=self.mostrar_libros)

        buttons_info = [
            ("Registrar Libro", "\uf192", self.buttonRegistrarLibro),
            ("Registrar Usuario", "\uf192", self.buttonRegistrarUsuario),
            ("Realizar Prestamo", "\uf192", self.buttonRealizarPrestamo),
            ("Mostrar Libros", "\uf192", self.buttonMostrarLibros),
        ]

        for text, icon, button in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu)                    
    
    def controles_cuerpo(self):
        # Área para mostrar información en el cuerpo principal
        self.labelCuerpo = tk.Label(self.cuerpo_principal, text="", bg=COLOR_CUERPO_PRINCIPAL)
        self.labelCuerpo.pack(side=tk.TOP, pady=10)

    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    def toggle_panel(self):
        # Alternar visibilidad del menú lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    def limpiar_cuerpo(self):
        # Limpiar el contenido del cuerpo principal
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()

    def mostrar_formulario_registrar_libro(self):
        self.limpiar_cuerpo()

        # Crear campos para ingresar la información del libro
        tk.Label(self.cuerpo_principal, text="Registrar Libro", bg=COLOR_CUERPO_PRINCIPAL).pack(pady=10)
        tk.Label(self.cuerpo_principal, text="Título:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_titulo = tk.Entry(self.cuerpo_principal)
        entry_titulo.pack()

        tk.Label(self.cuerpo_principal, text="ISBN:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_isbn = tk.Entry(self.cuerpo_principal)
        entry_isbn.pack()

        tk.Label(self.cuerpo_principal, text="Autor (Nombre):", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_autor_nombre = tk.Entry(self.cuerpo_principal)
        entry_autor_nombre.pack()

        tk.Label(self.cuerpo_principal, text="Autor (Apellido):", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_autor_apellido = tk.Entry(self.cuerpo_principal)
        entry_autor_apellido.pack()

        tk.Label(self.cuerpo_principal, text="Categoría:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_categoria = tk.Entry(self.cuerpo_principal)
        entry_categoria.pack()

        def registrar_libro():
            titulo = entry_titulo.get()
            isbn = entry_isbn.get()
            autor_nombre = entry_autor_nombre.get()
            autor_apellido = entry_autor_apellido.get()
            categoria_nombre = entry_categoria.get()

            autor = Autor(autor_nombre, autor_apellido)
            categoria = Categoria(categoria_nombre)
            libro = Libro(titulo, isbn, autor, categoria)
            self.biblioteca.registrar_libro(libro)
            messagebox.showinfo("Registro de Libro", "Libro registrado exitosamente")

        tk.Button(self.cuerpo_principal, text="Registrar", command=registrar_libro).pack(pady=10)

    def mostrar_formulario_registrar_usuario(self):
        self.limpiar_cuerpo()

        # Crear campos para ingresar la información del usuario
        tk.Label(self.cuerpo_principal, text="Registrar Usuario", bg=COLOR_CUERPO_PRINCIPAL).pack(pady=10)
        tk.Label(self.cuerpo_principal, text="Nombre:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_nombre = tk.Entry(self.cuerpo_principal)
        entry_nombre.pack()

        tk.Label(self.cuerpo_principal, text="Apellido:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_apellido = tk.Entry(self.cuerpo_principal)
        entry_apellido.pack()

        tk.Label(self.cuerpo_principal, text="ID Usuario:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_id_usuario = tk.Entry(self.cuerpo_principal)
        entry_id_usuario.pack()

        def registrar_usuario():
            nombre = entry_nombre.get()
            apellido = entry_apellido.get()
            id_usuario = entry_id_usuario.get()

            usuario = Usuario(nombre, apellido, id_usuario)
            self.biblioteca.registrar_usuario(usuario)
            messagebox.showinfo("Registro de Usuario", "Usuario registrado exitosamente")

        tk.Button(self.cuerpo_principal, text="Registrar", command=registrar_usuario).pack(pady=10)

    def mostrar_formulario_realizar_prestamo(self):
        self.limpiar_cuerpo()

        # Crear campos para ingresar la información del préstamo
        tk.Label(self.cuerpo_principal, text="Realizar Préstamo", bg=COLOR_CUERPO_PRINCIPAL).pack(pady=10)
        tk.Label(self.cuerpo_principal, text="ID Usuario:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_id_usuario = tk.Entry(self.cuerpo_principal)
        entry_id_usuario.pack()

        tk.Label(self.cuerpo_principal, text="ISBN del Libro:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_isbn = tk.Entry(self.cuerpo_principal)
        entry_isbn.pack()

        def realizar_prestamo():
            id_usuario = entry_id_usuario.get()
            isbn = entry_isbn.get()

            usuario = next((u for u in self.biblioteca.usuarios if u.id_usuario == id_usuario), None)
            libro = next((l for l in self.biblioteca.libros if l.isbn == isbn), None)

            if usuario and libro:
                prestamo = Prestamo(libro, usuario, "2023-01-01", "2023-02-01")
                self.biblioteca.realizar_prestamo(prestamo)
                messagebox.showinfo("Realizar Préstamo", "Préstamo realizado exitosamente")
            else:
                messagebox.showerror("Error", "Usuario o Libro no encontrado")

        tk.Button(self.cuerpo_principal, text="Prestar", command=realizar_prestamo).pack(pady=10)

    def mostrar_libros(self):
        self.limpiar_cuerpo()
        
        # Mostrar los libros registrados en la biblioteca
        libros_info = self.biblioteca.mostrar_libros()
        libros_str = "\n".join(libros_info)
        
        label_libros = tk.Label(self.cuerpo_principal, text=libros_str, bg=COLOR_CUERPO_PRINCIPAL)
        label_libros.pack(pady=10)


# Definición de clases para la gestión de la biblioteca

class Libro:
    def __init__(self, titulo, isbn, autor, categoria):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.categoria = categoria

    def mostrar_info(self):
        return f"Título: {self.titulo}, ISBN: {self.isbn}, Autor: {self.autor.mostrar_info()}, Categoría: {self.categoria.mostrar_info()}"


class Autor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_info(self):
        return f"{self.nombre} {self.apellido}"


class Usuario:
    def __init__(self, nombre, apellido, id_usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.id_usuario = id_usuario

    def mostrar_info(self):
        return f"Nombre: {self.nombre} {self.apellido}, ID: {self.id_usuario}"


class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def mostrar_info(self):
        return f"Libro: {self.libro.titulo}, Usuario: {self.usuario.nombre}, Fecha de Préstamo: {self.fecha_prestamo}, Fecha de Devolución: {self.fecha_devolucion}"


class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        return self.nombre


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def registrar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def realizar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def devolver_libro(self, prestamo):
        self.prestamos.remove(prestamo)

    def mostrar_libros(self):
        return [libro.mostrar_info() for libro in self.libros]


if __name__ == "__main__":
    app = FormularioMaestroDesign()
    app.mainloop()

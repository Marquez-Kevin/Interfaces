import tkinter as tk
from tkinter import font, messagebox
import config_ventana_4 as util_vent

# Definición de las clases del sistema de gestión del Mundial de Fútbol

class Equipo:
    def __init__(self, nombre, entrenador):
        self.nombre = nombre
        self.entrenador = entrenador
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def mostrar_info(self):
        jugadores_info = ", ".join([jugador.mostrar_info() for jugador in self.jugadores])
        return f"Equipo: {self.nombre}, Entrenador: {self.entrenador}, Jugadores: {jugadores_info}"


class Jugador:
    def __init__(self, nombre, edad, posicion):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion

    def mostrar_info(self):
        return f"{self.nombre} ({self.posicion}, {self.edad} años)"


class Partido:
    def __init__(self, equipo_local, equipo_visitante, estadio):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.estadio = estadio
        self.resultado = None

    def jugar_partido(self, resultado):
        self.resultado = resultado

    def mostrar_resultado(self):
        return f"{self.equipo_local.nombre} vs {self.equipo_visitante.nombre} - Resultado: {self.resultado}, Estadio: {self.estadio.nombre}"


class Grupo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def mostrar_info(self):
        equipos_info = ", ".join([equipo.nombre for equipo in self.equipos])
        return f"Grupo: {self.nombre}, Equipos: {equipos_info}"


class Estadio:
    def __init__(self, nombre, ciudad, capacidad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.capacidad = capacidad

    def mostrar_info(self):
        return f"Estadio: {self.nombre}, Ciudad: {self.ciudad}, Capacidad: {self.capacidad}"


class Mundial:
    def __init__(self):
        self.grupos = []
        self.estadios = []

    def registrar_grupo(self, grupo):
        self.grupos.append(grupo)

    def registrar_estadio(self, estadio):
        self.estadios.append(estadio)

    def generar_fixture(self):
        # Ejemplo de generación de fixture para demostración
        # En un caso real, este método debería ser más complejo
        partidos = []
        for grupo in self.grupos:
            equipos_grupo = grupo.equipos
            num_equipos = len(equipos_grupo)
            for i in range(num_equipos):
                for j in range(i + 1, num_equipos):
                    partido = Partido(equipos_grupo[i], equipos_grupo[j], self.estadios[0])
                    partidos.append(partido)
        return partidos


# Interfaz gráfica adaptada para el Sistema de Gestión de un Mundial de Fútbol

class FormularioMundialDesign(tk.Tk):
    def __init__(self):
        super().__init__()

        self.mundial = Mundial()  # Instancia del Mundial

        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()

    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Sistema de Gestión de un Mundial de Fútbol')

        w, h = 1024, 600
        util_vent.centrar_ventana(self, w, h)

    def paneles(self):
        # Crear paneles: barra superior, menú lateral y cuerpo principal
        self.barra_superior = tk.Frame(self, bg="#333333", height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')

        self.menu_lateral = tk.Frame(self, bg="#444444", width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        self.cuerpo_principal = tk.Frame(self, bg="#555555")
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def controles_barra_superior(self):
        # Configuración de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="Mundial de Fútbol")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg="#333333", pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg="#333333", fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        # Etiqueta de información
        self.labelInfo = tk.Label(self.barra_superior, text="Gestión de un Mundial de Fútbol")
        self.labelInfo.config(fg="#fff", font=("Roboto", 10), bg="#333333", padx=10, width=25)
        self.labelInfo.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)

        # Etiqueta de perfil
        self.labelPerfil = tk.Label(self.menu_lateral, bg="#444444")
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        # Botones del menú lateral
        self.buttonRegistrarEquipo = tk.Button(self.menu_lateral, command=self.mostrar_formulario_registrar_equipo)
        self.buttonRegistrarJugador = tk.Button(self.menu_lateral, command=self.mostrar_formulario_registrar_jugador)
        self.buttonCrearPartido = tk.Button(self.menu_lateral, command=self.mostrar_formulario_crear_partido)
        self.buttonMostrarGrupos = tk.Button(self.menu_lateral, command=self.mostrar_grupos)
        self.buttonMostrarEstadios = tk.Button(self.menu_lateral, command=self.mostrar_estadios)

        buttons_info = [
            ("Registrar Equipo", "\uf11b", self.buttonRegistrarEquipo),
            ("Registrar Jugador", "\uf11b", self.buttonRegistrarJugador),
            ("Crear Partido", "\uf11b", self.buttonCrearPartido),
            ("Mostrar Grupos", "\uf11b", self.buttonMostrarGrupos),
            ("Mostrar Estadios", "\uf11b", self.buttonMostrarEstadios),
        ]

        for text, icon, button in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu)

    def controles_cuerpo(self):
        # Área para mostrar información en el cuerpo principal
        self.labelCuerpo = tk.Label(self.cuerpo_principal, text="", bg="#555555")
        self.labelCuerpo.pack(side=tk.TOP, pady=10)

    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome,
                      bd=0, bg="#444444", fg="white", width=ancho_menu, height=alto_menu)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg="#666666", fg='white')

    def on_leave(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg="#444444", fg='white')

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


    def mostrar_formulario_registrar_equipo(self):
        self.limpiar_cuerpo()

        # Campos para registrar equipo
        label_titulo = tk.Label(self.cuerpo_principal, text="Registrar Equipo", bg="#555555", fg="white",
                                font=("Roboto", 14, "bold"))
        label_titulo.pack(pady=10)

        label_nombre = tk.Label(self.cuerpo_principal, text="Nombre del Equipo:", bg="#555555", fg="white")
        label_nombre.pack()
        entry_nombre = tk.Entry(self.cuerpo_principal)
        entry_nombre.pack()

        label_entrenador = tk.Label(self.cuerpo_principal, text="Nombre del Entrenador:", bg="#555555", fg="white")
        label_entrenador.pack()
        entry_entrenador = tk.Entry(self.cuerpo_principal)
        entry_entrenador.pack()

        button_registrar = tk.Button(self.cuerpo_principal, text="Registrar Equipo", bg="#4CAF50", fg="white",
                                     command=lambda: self.registrar_equipo(entry_nombre.get(), entry_entrenador.get()))
        button_registrar.pack(pady=10)

    def registrar_equipo(self, nombre, entrenador):
        equipo = Equipo(nombre, entrenador)
        self.mundial.registrar_grupo(Grupo(nombre))
        self.labelCuerpo.config(text=f"Equipo '{nombre}' registrado correctamente.", fg="#4CAF50")

    def mostrar_formulario_registrar_jugador(self):
        self.limpiar_cuerpo()

        # Campos para registrar jugador
        label_titulo = tk.Label(self.cuerpo_principal, text="Registrar Jugador", bg="#555555", fg="white",
                                font=("Roboto", 14, "bold"))
        label_titulo.pack(pady=10)

        label_nombre = tk.Label(self.cuerpo_principal, text="Nombre del Jugador:", bg="#555555", fg="white")
        label_nombre.pack()
        entry_nombre = tk.Entry(self.cuerpo_principal)
        entry_nombre.pack()

        label_edad = tk.Label(self.cuerpo_principal, text="Edad del Jugador:", bg="#555555", fg="white")
        label_edad.pack()
        entry_edad = tk.Entry(self.cuerpo_principal)
        entry_edad.pack()

        label_posicion = tk.Label(self.cuerpo_principal, text="Posición del Jugador:", bg="#555555", fg="white")
        label_posicion.pack()
        entry_posicion = tk.Entry(self.cuerpo_principal)
        entry_posicion.pack()

        button_registrar = tk.Button(self.cuerpo_principal, text="Registrar Jugador", bg="#4CAF50", fg="white",
                                     command=lambda: self.registrar_jugador(entry_nombre.get(), entry_edad.get(), entry_posicion.get()))
        button_registrar.pack(pady=10)

    def registrar_jugador(self, nombre, edad, posicion):
        jugador = Jugador(nombre, edad, posicion)
        # Se asume que el usuario debe seleccionar un equipo antes de registrar un jugador,
        # aquí se omite la selección por simplicidad.
        equipo_dummy = self.mundial.grupos[0].equipos[0]
        equipo_dummy.agregar_jugador(jugador)
        self.labelCuerpo.config(text=f"Jugador '{nombre}' registrado correctamente para el equipo '{equipo_dummy.nombre}'.", fg="#4CAF50")

    def mostrar_formulario_crear_partido(self):
        self.limpiar_cuerpo()

        # Campos para crear partido
        label_titulo = tk.Label(self.cuerpo_principal, text="Crear Partido", bg="#555555", fg="white",
                                font=("Roboto", 14, "bold"))
        label_titulo.pack(pady=10)

        label_equipo_local = tk.Label(self.cuerpo_principal, text="Equipo Local:", bg="#555555", fg="white")
        label_equipo_local.pack()
        combo_equipo_local = tk.StringVar(self.cuerpo_principal)
        combo_equipo_local.set("Seleccionar Equipo")
        opciones_equipos = [equipo.nombre for grupo in self.mundial.grupos for equipo in grupo.equipos]
        dropdown_equipo_local = tk.OptionMenu(self.cuerpo_principal, combo_equipo_local, *opciones_equipos)
        dropdown_equipo_local.pack()

        label_equipo_visitante = tk.Label(self.cuerpo_principal, text="Equipo Visitante:", bg="#555555", fg="white")
        label_equipo_visitante.pack()
        combo_equipo_visitante = tk.StringVar(self.cuerpo_principal)
        combo_equipo_visitante.set("Seleccionar Equipo")
        dropdown_equipo_visitante = tk.OptionMenu(self.cuerpo_principal, combo_equipo_visitante, *opciones_equipos)
        dropdown_equipo_visitante.pack()

        label_estadio = tk.Label(self.cuerpo_principal, text="Estadio:", bg="#555555", fg="white")
        label_estadio.pack()
        combo_estadio = tk.StringVar(self.cuerpo_principal)
        combo_estadio.set("Seleccionar Estadio")
        opciones_estadios = [estadio.nombre for estadio in self.mundial.estadios]
        dropdown_estadio = tk.OptionMenu(self.cuerpo_principal, combo_estadio, *opciones_estadios)
        dropdown_estadio.pack()

        button_crear_partido = tk.Button(self.cuerpo_principal, text="Crear Partido", bg="#4CAF50", fg="white",
                                         command=lambda: self.crear_partido(combo_equipo_local.get(), combo_equipo_visitante.get(), combo_estadio.get()))
        button_crear_partido.pack(pady=10)

    def crear_partido(self, nombre_equipo_local, nombre_equipo_visitante, nombre_estadio):
        equipo_local = next((equipo for grupo in self.mundial.grupos for equipo in grupo.equipos if equipo.nombre == nombre_equipo_local), None)
        equipo_visitante = next((equipo for grupo in self.mundial.grupos for equipo in grupo.equipos if equipo.nombre == nombre_equipo_visitante), None)
        estadio = next((estadio for estadio in self.mundial.estadios if estadio.nombre == nombre_estadio), None)

        if equipo_local and equipo_visitante and estadio:
            partido = Partido(equipo_local, equipo_visitante, estadio)
            # En un caso real, este método debería incluir más lógica como el manejo de resultados, etc.
            self.labelCuerpo.config(text=f"Partido entre '{equipo_local.nombre}' y '{equipo_visitante.nombre}' creado correctamente en el estadio '{estadio.nombre}'.", fg="#4CAF50")
        else:
            messagebox.showwarning("Error", "Selecciona un equipo y estadio válidos.")

    def mostrar_grupos(self):
        self.limpiar_cuerpo()

        # Mostrar información de los grupos
        label_titulo = tk.Label(self.cuerpo_principal, text="Grupos del Mundial", bg="#555555", fg="white",
                                font=("Roboto", 14, "bold"))
        label_titulo.pack(pady=10)

        for grupo in self.mundial.grupos:
            label_grupo = tk.Label(self.cuerpo_principal, text=grupo.mostrar_info(), bg="#555555", fg="white")
            label_grupo.pack()

    def mostrar_estadios(self):
        self.limpiar_cuerpo()

        # Mostrar información de los estadios
        label_titulo = tk.Label(self.cuerpo_principal, text="Estadios del Mundial", bg="#555555", fg="white",
                                font=("Roboto", 14, "bold"))
        label_titulo.pack(pady=10)

        for estadio in self.mundial.estadios:
            label_estadio = tk.Label(self.cuerpo_principal, text=estadio.mostrar_info(), bg="#555555", fg="white")
            label_estadio.pack()

# Función principal para ejecutar la interfaz
if __name__ == "__main__":
    app = FormularioMundialDesign()
    app.mainloop()


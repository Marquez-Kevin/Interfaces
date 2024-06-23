import tkinter as tk
from tkinter import font, messagebox
from config_2 import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import config_ventana_2 as util_ventana



class Curso:
    def __init__(self, nombre, profesor, horario):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []
        self.horario = horario

    def mostrar_info(self):
        estudiantes_info = ", ".join([estudiante.mostrar_info() for estudiante in self.estudiantes])
        return f"Curso: {self.nombre}, Profesor: {self.profesor.mostrar_info()}, Estudiantes: [{estudiantes_info}], Horario: {self.horario.mostrar_info()}"

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)


class Profesor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.asignaturas = []

    def mostrar_info(self):
        asignaturas_info = ", ".join([asignatura.mostrar_info() for asignatura in self.asignaturas])
        return f"Profesor: {self.nombre} {self.apellido}, Asignaturas: [{asignaturas_info}]"


class Estudiante:
    def __init__(self, nombre, apellido, id_estudiante):
        self.nombre = nombre
        self.apellido = apellido
        self.id_estudiante = id_estudiante
        self.cursos = []

    def mostrar_info(self):
        return f"Estudiante: {self.nombre} {self.apellido}, ID: {self.id_estudiante}"


class Asignatura:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor

    def mostrar_info(self):
        return f"Asignatura: {self.nombre}, Profesor: {self.profesor.mostrar_info()}"


class Evaluacion:
    def __init__(self, curso, estudiante, nota):
        self.curso = curso
        self.estudiante = estudiante
        self.nota = nota

    def mostrar_info(self):
        return f"Evaluacion: Curso: {self.curso.nombre}, Estudiante: {self.estudiante.mostrar_info()}, Nota: {self.nota}"


class Horario:
    def __init__(self, dia, hora_inicio, hora_fin):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def mostrar_info(self):
        return f"Horario: {self.dia}, De: {self.hora_inicio} a {self.hora_fin}"

class FormularioMaestroDesign(tk.Tk):

    def __init__(self):
        super().__init__()

        self.cursos = []
        self.profesores = []
        self.estudiantes = []

        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()

    def config_window(self):
        self.title('Sistema de Gestión de Cursos')
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h)

    def paneles(self):
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome', size=12)

        self.labelTitulo = tk.Label(self.barra_superior, text="Gestión de Cursos")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=20)
        self.labelTitulo.pack(side=tk.LEFT)

        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        self.labelInfo = tk.Label(self.barra_superior, text="Sistema de Gestión")
        self.labelInfo.config(fg="#fff", font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelInfo.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)

        self.labelPerfil = tk.Label(self.menu_lateral, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        self.buttonRegistrarCurso = tk.Button(self.menu_lateral, command=self.mostrar_formulario_registrar_curso)
        self.buttonRegistrarProfesor = tk.Button(self.menu_lateral, command=self.mostrar_formulario_registrar_profesor)
        self.buttonRegistrarEstudiante = tk.Button(self.menu_lateral, command=self.mostrar_formulario_registrar_estudiante)
        self.buttonMostrarCursos = tk.Button(self.menu_lateral, command=self.mostrar_cursos)

        buttons_info = [
            ("Registrar Curso", "\uf192", self.buttonRegistrarCurso),
            ("Registrar Profesor", "\uf192", self.buttonRegistrarProfesor),
            ("Registrar Estudiante", "\uf192", self.buttonRegistrarEstudiante),
            ("Mostrar Cursos", "\uf192", self.buttonMostrarCursos),
        ]

        for text, icon, button in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu)

    def controles_cuerpo(self):
        self.labelCuerpo = tk.Label(self.cuerpo_principal, text="", bg=COLOR_CUERPO_PRINCIPAL)
        self.labelCuerpo.pack(side=tk.TOP, pady=10)

    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    def limpiar_cuerpo(self):
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()

    def mostrar_formulario_registrar_curso(self):
        self.limpiar_cuerpo()

        tk.Label(self.cuerpo_principal, text="Registrar Curso", bg=COLOR_CUERPO_PRINCIPAL).pack(pady=10)
        tk.Label(self.cuerpo_principal, text="Nombre del Curso:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_nombre = tk.Entry(self.cuerpo_principal)
        entry_nombre.pack()

        tk.Label(self.cuerpo_principal, text="Nombre del Profesor:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_profesor = tk.Entry(self.cuerpo_principal)
        entry_profesor.pack()

        tk.Label(self.cuerpo_principal, text="Horario (día, hora_inicio, hora_fin):", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_horario = tk.Entry(self.cuerpo_principal)
        entry_horario.pack()

        def registrar_curso():
            nombre = entry_nombre.get()
            profesor_nombre = entry_profesor.get()
            horario_info = entry_horario.get().split(', ')

            profesor = next((p for p in self.profesores if p.nombre == profesor_nombre), None)
            if not profesor:
                messagebox.showerror("Error", "Profesor no encontrado")
                return

            horario = Horario(*horario_info)
            curso = Curso(nombre, profesor, horario)
            self.cursos.append(curso)
            messagebox.showinfo("Registro de Curso", "Curso registrado exitosamente")

        tk.Button(self.cuerpo_principal, text="Registrar", command=registrar_curso).pack(pady=10)

    def mostrar_formulario_registrar_profesor(self):
        self.limpiar_cuerpo()

        tk.Label(self.cuerpo_principal, text="Registrar Profesor", bg=COLOR_CUERPO_PRINCIPAL).pack(pady=10)
        tk.Label(self.cuerpo_principal, text="Nombre:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_nombre = tk.Entry(self.cuerpo_principal)
        entry_nombre.pack()

        tk.Label(self.cuerpo_principal, text="Apellido:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_apellido = tk.Entry(self.cuerpo_principal)
        entry_apellido.pack()

        def registrar_profesor():
            nombre = entry_nombre.get()
            apellido = entry_apellido.get()

            profesor = Profesor(nombre, apellido)
            self.profesores.append(profesor)
            messagebox.showinfo("Registro de Profesor", "Profesor registrado exitosamente")

        tk.Button(self.cuerpo_principal, text="Registrar", command=registrar_profesor).pack(pady=10)

    def mostrar_formulario_registrar_estudiante(self):
        self.limpiar_cuerpo()

        tk.Label(self.cuerpo_principal, text="Registrar Estudiante", bg=COLOR_CUERPO_PRINCIPAL).pack(pady=10)
        tk.Label(self.cuerpo_principal, text="Nombre:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_nombre = tk.Entry(self.cuerpo_principal)
        entry_nombre.pack()

        tk.Label(self.cuerpo_principal, text="Apellido:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_apellido = tk.Entry(self.cuerpo_principal)
        entry_apellido.pack()

        tk.Label(self.cuerpo_principal, text="ID Estudiante:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_id_estudiante = tk.Entry(self.cuerpo_principal)
        entry_id_estudiante.pack()

        def registrar_estudiante():
            nombre = entry_nombre.get()
            apellido = entry_apellido.get()
            id_estudiante = entry_id_estudiante.get()

            estudiante = Estudiante(nombre, apellido, id_estudiante)
            self.estudiantes.append(estudiante)
            messagebox.showinfo("Registro de Estudiante", "Estudiante registrado exitosamente")

        tk.Button(self.cuerpo_principal, text="Registrar", command=registrar_estudiante).pack(pady=10)

    def mostrar_cursos(self):
        self.limpiar_cuerpo()

        cursos_info = [curso.mostrar_info() for curso in self.cursos]
        cursos_str = "\n\n".join(cursos_info)

        label_cursos = tk.Label(self.cuerpo_principal, text=cursos_str, bg=COLOR_CUERPO_PRINCIPAL)
        label_cursos.pack(pady=10)


if __name__ == "__main__":
    app = FormularioMaestroDesign()
    app.mainloop()

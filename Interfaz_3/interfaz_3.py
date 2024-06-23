import tkinter as tk
from tkinter import font, messagebox
from config_3 import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import config_ventana_3 as util_ventana


class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Categoria: {self.categoria.mostrar_info()}"


class Cliente:
    def __init__(self, nombre, apellido, id_cliente):
        self.nombre = nombre
        self.apellido = apellido
        self.id_cliente = id_cliente

    def mostrar_info(self):
        return f"Cliente: {self.nombre} {self.apellido}, ID: {self.id_cliente}"


class Orden:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []
        self.total = 0

    def agregar_item(self, item):
        self.items.append(item)

    def calcular_total(self):
        self.total = sum(item.calcular_subtotal() for item in self.items)
        return self.total

    def mostrar_info(self):
        items_info = "\n".join([item.mostrar_info() for item in self.items])
        return f"Orden del Cliente: {self.cliente.mostrar_info()}\nItems:\n{items_info}\nTotal: {self.calcular_total()}"


class ItemOrden:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.producto.precio * self.cantidad

    def mostrar_info(self):
        return f"Item: {self.producto.mostrar_info()}, Cantidad: {self.cantidad}, Subtotal: {self.calcular_subtotal()}"


class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        return f"Categoria: {self.nombre}"


class Tienda:
    def __init__(self):
        self.productos = []
        self.clientes = []
        self.ordenes = []
        self.categorias = []

    def registrar_producto(self, producto):
        self.productos.append(producto)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def crear_orden(self, orden):
        self.ordenes.append(orden)

    def mostrar_productos(self):
        return "\n".join([producto.mostrar_info() for producto in self.productos])

class FormularioMaestroDesign(tk.Tk):

    def __init__(self):
        super().__init__()

        self.tienda = Tienda()

        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()

    def config_window(self):
        self.title('Sistema de Gestión de Tienda')
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

        self.labelTitulo = tk.Label(self.barra_superior, text="Gestión de Tienda")
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

        self.buttonRegistrarProducto = tk.Button(self.menu_lateral, command=self.mostrar_formulario_registrar_producto)
        self.buttonRegistrarCliente = tk.Button(self.menu_lateral, command=self.mostrar_formulario_registrar_cliente)
        self.buttonCrearOrden = tk.Button(self.menu_lateral, command=self.mostrar_formulario_crear_orden)
        self.buttonMostrarProductos = tk.Button(self.menu_lateral, command=self.mostrar_productos)

        buttons_info = [
            ("Registrar Producto", "\uf192", self.buttonRegistrarProducto),
            ("Registrar Cliente", "\uf192", self.buttonRegistrarCliente),
            ("Crear Orden", "\uf192", self.buttonCrearOrden),
            ("Mostrar Productos", "\uf192", self.buttonMostrarProductos),
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

    def mostrar_formulario_registrar_producto(self):
        self.limpiar_cuerpo()

        tk.Label(self.cuerpo_principal, text="Registrar Producto", bg=COLOR_CUERPO_PRINCIPAL).pack(pady=10)
        tk.Label(self.cuerpo_principal, text="Nombre del Producto:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_nombre = tk.Entry(self.cuerpo_principal)
        entry_nombre.pack()

        tk.Label(self.cuerpo_principal, text="Precio del Producto:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_precio = tk.Entry(self.cuerpo_principal)
        entry_precio.pack()

        tk.Label(self.cuerpo_principal, text="Categoria del Producto:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_categoria = tk.Entry(self.cuerpo_principal)
        entry_categoria.pack()

        def registrar_producto():
            nombre = entry_nombre.get()
            precio = float(entry_precio.get())
            categoria_nombre = entry_categoria.get()

            categoria = next((c for c in self.tienda.categorias if c.nombre == categoria_nombre), None)
            if not categoria:
                categoria = Categoria(categoria_nombre)
                self.tienda.categorias.append(categoria)

            producto = Producto(nombre, precio, categoria)
            self.tienda.registrar_producto(producto)
            messagebox.showinfo("Registro de Producto", "Producto registrado exitosamente")

        tk.Button(self.cuerpo_principal, text="Registrar", command=registrar_producto).pack(pady=10)

    def mostrar_formulario_registrar_cliente(self):
        self.limpiar_cuerpo()

        tk.Label(self.cuerpo_principal, text="Registrar Cliente", bg=COLOR_CUERPO_PRINCIPAL).pack(pady=10)
        tk.Label(self.cuerpo_principal, text="Nombre:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_nombre = tk.Entry(self.cuerpo_principal)
        entry_nombre.pack()

        tk.Label(self.cuerpo_principal, text="Apellido:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_apellido = tk.Entry(self.cuerpo_principal)
        entry_apellido.pack()

        tk.Label(self.cuerpo_principal, text="ID Cliente:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_id_cliente = tk.Entry(self.cuerpo_principal)
        entry_id_cliente.pack()

        def registrar_cliente():
            nombre = entry_nombre.get()
            apellido = entry_apellido.get()
            id_cliente = entry_id_cliente.get()

            cliente = Cliente(nombre, apellido, id_cliente)
            self.tienda.registrar_cliente(cliente)
            messagebox.showinfo("Registro de Cliente", "Cliente registrado exitosamente")

        tk.Button(self.cuerpo_principal, text="Registrar", command=registrar_cliente).pack(pady=10)

    def mostrar_formulario_crear_orden(self):
        self.limpiar_cuerpo()

        tk.Label(self.cuerpo_principal, text="Crear Orden", bg=COLOR_CUERPO_PRINCIPAL).pack(pady=10)
        tk.Label(self.cuerpo_principal, text="ID Cliente:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_id_cliente = tk.Entry(self.cuerpo_principal)
        entry_id_cliente.pack()

        tk.Label(self.cuerpo_principal, text="Nombre del Producto:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_nombre_producto = tk.Entry(self.cuerpo_principal)
        entry_nombre_producto.pack()

        tk.Label(self.cuerpo_principal, text="Cantidad:", bg=COLOR_CUERPO_PRINCIPAL).pack()
        entry_cantidad = tk.Entry(self.cuerpo_principal)
        entry_cantidad.pack()

        def crear_orden():
            id_cliente = entry_id_cliente.get()
            nombre_producto = entry_nombre_producto.get()
            cantidad = int(entry_cantidad.get())

            cliente = next((c for c in self.tienda.clientes if c.id_cliente == id_cliente), None)
            if not cliente:
                messagebox.showerror("Error", "Cliente no encontrado")
                return

            producto = next((p for p in self.tienda.productos if p.nombre == nombre_producto), None)
            if not producto:
                messagebox.showerror("Error", "Producto no encontrado")
                return

            orden = next((o for o in self.tienda.ordenes if o.cliente.id_cliente == id_cliente), None)
            if not orden:
                orden = Orden(cliente)
                self.tienda.crear_orden(orden)

            item_orden = ItemOrden(producto, cantidad)
            orden.agregar_item(item_orden)
            orden.calcular_total()

            messagebox.showinfo("Orden Creada", "Orden creada exitosamente")

        tk.Button(self.cuerpo_principal, text="Crear Orden", command=crear_orden).pack(pady=10)

    def mostrar_productos(self):
        self.limpiar_cuerpo()

        productos_info = self.tienda.mostrar_productos()

        label_productos = tk.Label(self.cuerpo_principal, text=productos_info, bg=COLOR_CUERPO_PRINCIPAL)
        label_productos.pack(pady=10)


if __name__ == "__main__":
    app = FormularioMaestroDesign()
    app.mainloop()

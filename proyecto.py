from tkinter import *


class Login:

    def __init__(self, prueba):

        self.ventana = prueba
        self.ventana.title("Login con Python")
        self.ventana.geometry("400x310")
        self.label=Label(text="Sistema de acceso",bg="#02AC66",fg="white",width=300,height=3,
            font=("Calibri",15)).pack()
        self.label=Label(text="").pack()  

        self.button1=Button(text="Iniciar sesion",bg="#02AC66",fg="white",width=30,height=3,command=self.iniciar_sesion).pack()  
        self.label=Label(text="",pady=10).pack()

        self.button2=Button(text="Registrar",bg="#02AC66",fg="white",width=30,height=3,command=self.registro).pack()


    def iniciar_sesion(self):
            self.ventana1 = Toplevel()
            self.ventana1.title("Iniciar sesion")
            self.ventana1.geometry("400x250")
            self.label=Label(self.ventana1,text="Ingrese su usuario y contraseña",bg="teal",fg="white",width=300,height=3,
            font=("Calibri",15)).pack()

            self.label=Label(self.ventana1,text="Usuario").pack(pady=10)
            self.usuario_entry = Entry(self.ventana1)
            self.usuario_entry.pack()

            self.label=Label(self.ventana1,text="Contraseña").pack(pady=10)
            self.usuario_contraseña = Entry(self.ventana1)
            self.usuario_contraseña.pack()

            self.button=Button(self.ventana1,text="Iniciar session").pack(pady=15)

    def registro(self):
            self.ventana2 = Toplevel()
            self.ventana2.title("Registro")
            self.ventana2.geometry("400x250")
            self.label=Label(self.ventana2,text="Registro de usuario",bg="teal",fg="white",width=300,height=3,
            font=("Calibri",15)).pack()

            self.label=Label(self.ventana2,text="Usuario").pack(pady=10)
            self.usuario_entry = Entry(self.ventana2)
            self.usuario_entry.pack()

            self.label=Label(self.ventana2,text="Contraseña").pack(pady=10)
            self.usuario_contraseña = Entry(self.ventana2)
            self.usuario_contraseña.pack()

            self.button=Button(self.ventana2,text="Registrar").pack(pady=15)






if __name__ == '__main__':
    prueba = Tk()
    resultado = Login(prueba)  
    prueba.mainloop()  
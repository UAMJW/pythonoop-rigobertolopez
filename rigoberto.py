class Persona:
    def inicializar(self,nom,apellido):
        self.nombre=nom
        self.apellido=apellido
    def imprimir(self):
        print ('Nombre:');
        print (self.nombre);
        print('Apellido:');
        print(self.apellido);

persona1=Persona()
persona1.inicializar('Rigoberto','Lopez')
persona1.imprimir()

persona2=Persona()
persona2.inicializar('Juan','Perez')
persona2.imprimir()
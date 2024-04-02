from django.db import models

class TipoPermiso(models.Model):
    nombre = models.CharField(max_length=45, blank=False, null=False)
        
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=45, blank=False, null=False)
    apellido = models.CharField(max_length=45, blank=False, null=False)
    email = models.EmailField(max_length=45, blank=False, null=False)
    contrasena = models.CharField(max_length=45, blank=False, null=False)
    tipo_permiso = models.ManyToManyField(TipoPermiso, through='UsuarioPermiso')

    
class UsuarioPermiso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo_permiso = models.ForeignKey(TipoPermiso, on_delete=models.CASCADE)
    
    
class Coleccion(models.Model):
    nombre = models.CharField(max_length=45, blank=False, null=False)
    descripcion = models.TextField(max_length=200)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    coleccion_compartida = models.ManyToManyField(UsuarioPermiso, db_table='coleccion_compartida')


class TipoEquipo(models.Model):
    nombre = models.CharField(max_length=45, blank=False, null=False)
    descripcion = models.TextField(max_length=200)


class Equipo(models.Model):
    tipo_equipo = models.ForeignKey(TipoEquipo, on_delete=models.CASCADE)
    marca = models.CharField(max_length=45, blank=False, null=False)
    modelo = models.CharField(max_length=45, blank=False, null=False)
    descripcion = models.TextField(max_length=200)
    tasa_muestreo = models.CharField(max_length=45)
    rango_frecuencias = models.CharField(max_length=45)

    
class Departamento(models.Model):
    codigo_departamento = models.CharField(max_length=10, blank=False, null=False)
    nombre = models.CharField(max_length=45, blank=False, null=False)
    

class Municipio(models.Model):
    codigo_municipio = models.CharField(max_length=10, blank=False, null=False)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=45, blank=False, null=False)
    
    class Meta:
        unique_together = [['codigo_municipio', 'departamento']]

class Ubicacion(models.Model):
    longitud = models.CharField(max_length=45, blank=False, null=False)
    latitud = models.CharField(max_length=45, blank=False, null=False)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    
    
class Audio(models.Model):
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)    
    coleccion = models.ManyToManyField(Coleccion, db_table='coleccion_audio')
    nombre_archivo = models.CharField(max_length=50, blank=False, null=False)
    ruta = models.CharField(max_length=45, blank=False, null=False)
    fecha_creacion = models.DateField()
    creador = models.CharField(max_length=45, blank=False, null=False)

    
class TipoEtiqueta(models.Model):
    nombre = models.CharField(max_length=45, blank=False, null=False)
    descripcion = models.TextField(max_length=200) 
       
class Etiqueta(models.Model):
    tipo_etiqueta = models.ForeignKey(TipoEtiqueta, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=45, blank=False, null=False)
    descripcion = models.TextField(max_length=200)
       
    class Meta:
        unique_together = [['id', 'tipo_etiqueta']]
    
class Anotacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE)
    tiempo_inicio = models.TimeField(blank=False, null=False)
    tiempo_final = models.TimeField(blank=False, null=False)


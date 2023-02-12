from django.db import models

# Create your models here.
class Room (models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion", max_length=200)
    price = models.IntegerField(verbose_name="Precio")
    pais = models.CharField(max_length=100, verbose_name="Pais")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    dateI = models.DateField(verbose_name="Fecha de inicio")
    dateF = models.DateField(verbose_name="Fecha de fin")
    image1 = models.ImageField(verbose_name="Imagen 1", upload_to= "rooms")
    image2 = models.ImageField(verbose_name="Imagen 2", upload_to= "rooms")
    image3 = models.ImageField(verbose_name="Imagen 3", upload_to= "rooms")
    image4 = models.ImageField(verbose_name="Imagen 4", upload_to= "rooms")
    nom = models.CharField(max_length=100, verbose_name="Nombres")
    apell = models.CharField(max_length=100, verbose_name="Apellidos")
    cell = models.CharField(max_length=20, verbose_name="Celular")
    email = models.CharField(max_length=100, verbose_name="Email")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'
        ordering = ["-created"]
    def __str__(self):
        return self.title
    
class Reservation(models.Model):
    date = models.DateField(verbose_name="Fecha de Reservacion")
    cliente = models.CharField(verbose_name="Cliente", max_length=100)
    mail = models.EmailField(verbose_name="Email")
    room = models.CharField(max_length=100,verbose_name="Habitacion")
    user = models.CharField(max_length=100,verbose_name="Usuario")
    class Meta:
        verbose_name = 'Reservacion'
        verbose_name_plural = 'Reservaciones'
        ordering = ["-date"]
    def __str__(self):
        return self.cliente

class About (models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to= "about")
    description_security = models.TextField(verbose_name="Descripcion de Seguridad")
    description_price = models.TextField(verbose_name="Descripcion de Precio")
    description_availability = models.TextField(verbose_name="Descripcion de Disponibilidad")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Nosotro'
        verbose_name_plural = 'Nosotros'
        ordering = ["-created"]
    def __str__(self):
        return self.title 

class Blog (models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    date = models.DateField(verbose_name="Fecha")
    author = models.CharField(max_length=100, verbose_name="Autor")
    image = models.ImageField(verbose_name="Imagen", upload_to="blog")
    description = models.TextField(verbose_name="Descripcion")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
        ordering = ["-created"]
    def __str__(self):
        return self.title 

class Testimony(models.Model):
    description = models.TextField(verbose_name="Descripcion")
    author = models.CharField(max_length=200, verbose_name="Autor")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimoniales'
        ordering = ["-created"]
    def __str__(self):
        return self.author
    
class Asesoria (models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    mail = models.CharField(max_length=200, verbose_name="E-mail")
    cell = models.CharField(max_length=100, verbose_name="Telefono")
    msg = models.TextField(verbose_name="Mensaje")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Asesoria'
        verbose_name_plural = 'Asesorias'
        ordering = ["-created"]
    def __str__(self):
        return self.name
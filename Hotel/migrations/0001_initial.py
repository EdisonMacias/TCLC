# Generated by Django 4.0.5 on 2023-01-26 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('image', models.ImageField(upload_to='about', verbose_name='Imagen')),
                ('image_security', models.ImageField(upload_to='about', verbose_name='Imagen de Seguridad')),
                ('description_security', models.TextField(verbose_name='Descripcion de Seguridad')),
                ('image_price', models.ImageField(upload_to='about', verbose_name='Imagen de Precio')),
                ('description_price', models.TextField(verbose_name='Descripcion de Precio')),
                ('image_availability', models.ImageField(upload_to='about', verbose_name='Imagen de Disponibilidad')),
                ('description_availability', models.TextField(verbose_name='Descripcion de Disponibilidad')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')),
            ],
            options={
                'verbose_name': 'Nosotro',
                'verbose_name_plural': 'Nosotros',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Asesoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('mail', models.CharField(max_length=200, verbose_name='E-mail')),
                ('cell', models.CharField(max_length=100, verbose_name='Telefono')),
                ('msg', models.TextField(verbose_name='Mensaje')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')),
            ],
            options={
                'verbose_name': 'Asesoria',
                'verbose_name_plural': 'Asesorias',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('author', models.CharField(max_length=100, verbose_name='Autor')),
                ('image', models.ImageField(upload_to='blog', verbose_name='Imagen')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Fecha de Reservacion')),
                ('cliente', models.CharField(max_length=100, verbose_name='Cliente')),
                ('mail', models.EmailField(max_length=254, verbose_name='Email')),
                ('room', models.CharField(max_length=100, verbose_name='Habitacion')),
                ('user', models.CharField(max_length=100, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Reservacion',
                'verbose_name_plural': 'Reservaciones',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('description', models.TextField(max_length=200, verbose_name='Descripcion')),
                ('price', models.IntegerField(verbose_name='Precio')),
                ('pais', models.CharField(max_length=100, verbose_name='Pais')),
                ('ciudad', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('autor', models.CharField(max_length=100, verbose_name='Autor')),
                ('dateI', models.DateField(verbose_name='Fecha de inicio')),
                ('dateF', models.DateField(verbose_name='Fecha de inicio')),
                ('image1', models.ImageField(upload_to='rooms', verbose_name='Imagen 1')),
                ('image2', models.ImageField(upload_to='rooms', verbose_name='Imagen 2')),
                ('image3', models.ImageField(upload_to='rooms', verbose_name='Imagen 3')),
                ('image4', models.ImageField(upload_to='rooms', verbose_name='Imagen 4')),
                ('nom', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apell', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('cell', models.CharField(max_length=20, verbose_name='Celular')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('author', models.CharField(max_length=200, verbose_name='Autor')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimoniales',
                'ordering': ['-created'],
            },
        ),
    ]

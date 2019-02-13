# Generated by Django 2.1.1 on 2018-10-10 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recog', '0027_auto_20181004_0419'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['-FehaRegistro'], 'verbose_name': 'Persona', 'verbose_name_plural': 'Personas'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Perfil', 'verbose_name_plural': 'Perfiles'},
        ),
        migrations.AddField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Fue Modificado en:'),
        ),
        migrations.AlterField(
            model_name='person',
            name='ApellidoMaterno',
            field=models.CharField(help_text='Introduzca un apellido correcto', max_length=35, verbose_name='Apellido Materno'),
        ),
        migrations.AlterField(
            model_name='person',
            name='ApellidoPaterno',
            field=models.CharField(help_text='Introduzca un apellido correcto', max_length=35, verbose_name='Apellido Paterno'),
        ),
        migrations.AlterField(
            model_name='person',
            name='Cabello',
            field=models.CharField(choices=[('N', 'Negro'), ('B', 'Blanco'), ('C', 'Cafe'), ('R', 'Rojo'), ('RU', 'Rubio')], default='N', max_length=5, verbose_name='Color de Cabello'),
        ),
        migrations.AlterField(
            model_name='person',
            name='Ci',
            field=models.CharField(help_text='Introduzca un numero de CI. correcto', max_length=10, unique=True, verbose_name='Cédula de Identidad'),
        ),
        migrations.AlterField(
            model_name='person',
            name='Contextura',
            field=models.CharField(choices=[('D', 'Delgada'), ('M', 'Mediana'), ('S', 'Semigruesa'), ('G', 'Gruesa')], default='D', max_length=5, verbose_name='Tipo de Contextura'),
        ),
        migrations.AlterField(
            model_name='person',
            name='Direccion',
            field=models.CharField(max_length=50, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='person',
            name='Estado',
            field=models.BooleanField(default=False, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='person',
            name='FehaDesaparicion',
            field=models.DateField(verbose_name='Desaparición en Fecha:'),
        ),
        migrations.AlterField(
            model_name='person',
            name='FehaRegistro',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='person',
            name='Nombres',
            field=models.CharField(help_text='Introduzca un nombre correcto', max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='person',
            name='Ojos',
            field=models.CharField(choices=[('N', 'Negro'), ('V', 'Verde'), ('C', 'Cafe'), ('CE', 'Celeste')], default='N', max_length=5, verbose_name='Color de Ojos'),
        ),
        migrations.AlterField(
            model_name='person',
            name='Tez',
            field=models.CharField(choices=[('C', 'Clara'), ('T', 'Trigueña'), ('M', 'Morena')], default='C', max_length=5, verbose_name='Tono de Piel'),
        ),
        migrations.AlterField(
            model_name='person',
            name='faceData',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='facePicture',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='faces/%m/%d/%Y', verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='person',
            name='referencia',
            field=models.TextField(max_length=50, null=True, verbose_name='Referencias'),
        ),
        migrations.AlterField(
            model_name='person',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Registrado/Actualizado por:'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='institucion',
            field=models.CharField(max_length=50, verbose_name='Institución'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lug_trabajo',
            field=models.CharField(max_length=50, verbose_name='Lugar de trabajo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(null=True, unique=True, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profesion',
            field=models.CharField(max_length=50, null=True, verbose_name='Profesión'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='unidad',
            field=models.CharField(max_length=50, verbose_name='Unidad de Trabajo'),
        ),
    ]
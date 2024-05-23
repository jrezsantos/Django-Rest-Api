# Generated by Django 5.0.6 on 2024-05-23 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciador', '0002_listapedidosusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='codigo_item',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='nome',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='ListaPedidosUsuario',
        ),
    ]
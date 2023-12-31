# Generated by Django 4.2.5 on 2023-10-05 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuapp', '0002_estoque'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemEstoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('quantidade', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Estoque',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]

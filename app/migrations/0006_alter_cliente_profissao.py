# Generated by Django 4.1.3 on 2023-02-07 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_alter_dependente_titular_alter_atendente_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="profissao",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
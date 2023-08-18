# Generated by Django 4.2.3 on 2023-08-03 14:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=50, null=True)),
                ('adresse', models.CharField(blank=True, max_length=50, null=True)),
                ('telephone', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id_commande', models.IntegerField(primary_key=True, serialize=False)),
                ('dateC', models.DateField(default=datetime.date.today)),
                ('montant', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='App.client')),
            ],
        ),
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id_marque', models.IntegerField(primary_key=True, serialize=False)),
                ('designation', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id_produit', models.IntegerField(primary_key=True, serialize=False)),
                ('designation', models.CharField(blank=True, max_length=50, null=True)),
                ('prix', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('marque', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='App.marque')),
            ],
        ),
        migrations.CreateModel(
            name='LigneCommande',
            fields=[
                ('id_ligneCommande', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today)),
                ('prix', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('commande', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='App.commande')),
                ('produit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='App.produit')),
            ],
        ),
    ]
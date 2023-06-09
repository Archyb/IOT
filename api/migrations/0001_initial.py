# Generated by Django 4.2.1 on 2023-05-23 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConditionTransport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature_min', models.DecimalField(decimal_places=2, max_digits=5)),
                ('temperature_max', models.DecimalField(decimal_places=2, max_digits=5)),
                ('temperature_unite', models.CharField(max_length=20)),
                ('hygiene', models.TextField()),
                ('emballage', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Grossiste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=100)),
                ('code_postal', models.CharField(max_length=10)),
                ('pays', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Marchandise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('quantite', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unite', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Revendeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=100)),
                ('code_postal', models.CharField(max_length=10)),
                ('pays', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('conditions_transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.conditiontransport')),
                ('documents', models.ManyToManyField(to='api.document')),
                ('grossiste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.grossiste')),
                ('marchandise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.marchandise')),
                ('revendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.revendeur')),
            ],
        ),
    ]

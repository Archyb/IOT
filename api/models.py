from django.db import models

class Grossiste(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=10)
    pays = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Revendeur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=10)
    pays = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Marchandise(models.Model):
    type = models.CharField(max_length=100)
    quantite = models.DecimalField(max_digits=10, decimal_places=2)
    unite = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class ConditionTransport(models.Model):
    temperature_min = models.DecimalField(max_digits=5, decimal_places=2)
    temperature_max = models.DecimalField(max_digits=5, decimal_places=2)
    temperature_unite = models.CharField(max_length=20)
    hygiene = models.TextField()
    emballage = models.TextField()

    def __str__(self):
        return f"Conditions de transport ({self.temperature_min}°C - {self.temperature_max}°C)"


class Document(models.Model):
    type = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.numero


class Transport(models.Model):
    transaction_id = models.CharField(max_length=50)
    date = models.DateField()
    grossiste = models.ForeignKey(Grossiste, on_delete=models.CASCADE)
    revendeur = models.ForeignKey(Revendeur, on_delete=models.CASCADE)
    marchandise = models.ForeignKey(Marchandise, on_delete=models.CASCADE)
    conditions_transport = models.ForeignKey(ConditionTransport, on_delete=models.CASCADE)
    documents = models.ManyToManyField(Document)

    def __str__(self):
        return self.transaction_id

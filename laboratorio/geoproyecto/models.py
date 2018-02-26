from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.utils import timezone

class Municipality(models.Model):
    class Meta:
        verbose_name_plural = 'Municipalidades'
        verbose_name = 'Municipalidad'
        
    name = models.CharField("Nombre", max_length=75, null=False)
    desc = models.TextField("Descripción", null=True)
    lat = models.DecimalField("Latitud", max_digits=9, decimal_places=6)
    long = models.DecimalField("Longitud", max_digits=9, decimal_places=6)
    zoom = models.PositiveSmallIntegerField("Zoom")
    
    def __str__(self):
        return 'Municipalidad '+self.name

class RateItem(models.Model):
    name = models.CharField("Nombre", max_length=75, null=False)

    def __str__(self):
        return 'RateItem '+self.name
    
class Project(models.Model):
    class Meta:
        verbose_name_plural = 'Proyectos'
        verbose_name = 'Proyecto'

    #types
    project_type_choices = (
        ('APOT','Agua Potable'),
        ('ALC','Alcantarillado'),
        ('DEP','Deporte'),
        ('EDU','Educación'),
        ('IVIAL','Infraestructura vial'),
        ('SAL','Salud'),
    )

    municipality = models.ForeignKey(Municipality, on_delete=models.PROTECT)    
    name = models.CharField("Nombre", max_length=250, null=False)
    desc = models.TextField("Descripción", null=True, blank=True)
    active = models.BooleanField('Activo', default=True)
    project_type = models.CharField(
        "Tipo",
        max_length = 5,
        choices = project_type_choices,
        default = 'APOT'
    )
    lat = models.DecimalField("Latitud", max_digits=9, decimal_places=6)
    long = models.DecimalField("Longitud", max_digits=9, decimal_places=6)
    firm = models.CharField("Empresa", max_length=125, null=False)
    pic = models.ImageField("Fotografia", upload_to = 'projects', null=True, blank=True)
    ammount = models.DecimalField("Monto", max_digits=12, decimal_places=2)
    execution = models.FloatField("Porcentaje de avance", validators = [
                                                            MaxValueValidator(100),
                                                            MinValueValidator(0)
                                                        ])
    budgetExec = models.FloatField("Porcentaje de ejecucion presupuestaria", validators = [
                                                                                MaxValueValidator(100),
                                                                                MinValueValidator(0)
                                                                            ])

    
    def __str__(self):
        return 'Proyecto '+self.name

class Rate(models.Model):
    rate_item = models.ForeignKey(RateItem, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    ip = models.CharField("IP", max_length=15,null=False)
    value = models.IntegerField("Valor", validators = [
                                                MaxValueValidator(3),
                                                MinValueValidator(1)
                                            ])
    vote_date = models.DateTimeField("Fecha", default=timezone.now)

    def __str__(self):
        return 'Rate ' + self.rate_item.name + ' made by ' + self.ip + ' on ' + str(self.vote_date)


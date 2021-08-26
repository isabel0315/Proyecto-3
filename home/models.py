from django.db import models

class categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)

    def __str__(self):
    	return self.nombre

class marca(models.Model):
   nombre =models.CharField(max_length=120)

   def __str__(self):
       return self.nombre

class producto (models.Model):
	nombre      = models.CharField(max_length = 100)
	descripcion = models.TextField(max_length = 500)
	status      = models.BooleanField(default = True)
	precio      = models.DecimalField(max_digits= 20, decimal_places= 2, default= 0.00)
	stock       = models.IntegerField()
	categorias  = models.ForeignKey(categoria, on_delete=models.CASCADE)
	marca       = models.ManyToManyField(marca)


	def _str_(self):
		return self.nombre




         

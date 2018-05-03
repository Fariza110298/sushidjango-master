from django.db import models

# Create your models here.
class Sushitype(models.Model):
    """
    Model representing  sushitype (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Dobavite type sushi (e.g. Science Fiction, French Poetry etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class SpisokMenu(models.Model):
    """
    Model representing a  SpisokMenu (but not a specific copy of a SpisokMenu).
    """
    sushiname = models.CharField(max_length=200)
    sponsor = models.ForeignKey('Sponsor', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple
    # Author as a string rather than object because it hasn't been declared yet in the file.
    resept = models.TextField(max_length=1000, help_text='SushiResept')
    sushiprice = models.CharField('SushiPrice',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">SushiPrice number</a>')
    sushitype = models.ManyToManyField(Sushitype, help_text='Sushitype')
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.sushiname
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this spisokmenu.
        """
        return reverse('spisokmenu-detail', args=[str(self.id)])

class Sponsor(models.Model):
    """
    Model representing an author.
    """
    sponsor_name = models.CharField(max_length=100)
    sponsor_kala = models.CharField(max_length=100)
    zakaz_product = models.DateField(null=True, blank=True)
    printitya_zakaz = models.DateField('printitya_zakaz', null=True, blank=True)

    class Meta:
        ordering = ["sponsor_kala","sponsor_name"]
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('sponsor-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.sponsor_kala,self.sponsor_name)
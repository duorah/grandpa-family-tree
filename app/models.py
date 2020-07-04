from django.db import models
import datetime

# Create your models here.
class Person(models.Model):
    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
    ORIGIN_CHOICES = [('P', 'Patrilineal'), ('I', 'Inherited'), ('M', 'Matrilineal'), ('T', 'Taken')]
    
    person_id = models.CharField(max_length=10, blank=True)
    title = models.CharField(max_length=10, blank=True)
    nickname = models.CharField(max_length=20, blank=True)
    callname = models.CharField(max_length=100, blank=True)
    givenname = models.CharField(max_length=100)
    suffix = models.CharField(max_length=10, blank=True, null=True)
    surname = models.CharField(max_length=100)
    origin = models.CharField(max_length=2, choices=ORIGIN_CHOICES, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='U')
    birthdate = models.DateField(default=datetime.date.fromisoformat('1960-01-01'))
    deathdate = models.DateField(default=datetime.date.fromisoformat('1960-01-01'))
    email = models.EmailField(max_length=256, default="", blank=True)
    social = models.CharField(max_length=256, default="", blank=True)
    picture = models.ImageField(upload_to='pic_filter/', default='pic_folder/None/no-img.jpg')
    spouse = models.ForeignKey('self', on_delete=models.CASCADE, related_name='Spouse', null=True, default=None,
                               limit_choices_to={'gender': ''}, blank=True)
    father = models.ForeignKey('self', on_delete=models.CASCADE, limit_choices_to={'gender': 'M'},
                               null=True, related_name='Father', default=None, blank=True)
    mother = models.ForeignKey('self', on_delete=models.CASCADE, related_name='Mother', default=None,
                               null=True, limit_choices_to={'gender': 'F'}, blank=True)
    children = models.ManyToManyField('self', blank=True, symmetrical=False)
    
    def save(self, *args, **kwargs):
        add = not self.pk
        super(Person, self).save(*args, **kwargs)
        if add:
            self.person_id = '[I%04d]' % self.id
            super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return self.givenname + ' '  + self.surname

    def _children(self):
        return ', '.join(c.givenname for c in self.children.all())

    class Meta:
        verbose_name_plural = "People"
        
    
class Family(models.Model):
    
    family = models.CharField(max_length=10, blank=True)
    husband = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name='Husband', default=None,
                               blank=True)
    wife = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='Wife', default=None,
                               null=True, blank=True)
    children = models.ManyToManyField(Person, default=None, null=True)
    marriagedate = models.DateField(default=datetime.date.fromisoformat('1960-01-01'))
    
    def save(self, *args, **kwargs):
        add = not self.pk
        super(Family, self).save(*args, **kwargs)
        if add:
            self.family = '[F%04d]' % self.id
            super(Family, self).save(*args, **kwargs)

    def _children(self):
        return ', '.join(c.givenname for c in self.children.all())

    class Meta:
        verbose_name_plural = "Families"


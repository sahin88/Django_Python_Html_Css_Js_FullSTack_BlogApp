from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
class home_model(models.Model):
    id = models.AutoField(primary_key=True)
    main_image = models.ImageField(
        upload_to='home/images', blank=True)
    hello_message=models.CharField(max_length=255,blank=True)
    i_message=models.CharField(max_length=255,blank=True)
    my_message=models.CharField(max_length=255,blank=True)


    def __str__(self):
        return self.hello_message

    def save(self, *args, **kwargs):
        if not self.id and home_model.objects.exists():
     
            raise ValidationError('There is can be only one JuicerBaseSettings instance')
        return super(home_model, self).save(*args, **kwargs)

class about_model(models.Model):
    id = models.AutoField(primary_key=True)
    about_image = models.ImageField(
        upload_to='about/images', blank=True)

    about_me =models.TextField(blank=True)
    image_1=models.ImageField(
        upload_to='about/photo_gallery', blank=True)
    image_2=models.ImageField(
        upload_to='about/photo_gallery', blank=True)
    image_3=models.ImageField(
        upload_to='about/photo_gallery', blank=True)
    image_4=models.ImageField(
        upload_to='about/photo_gallery', blank=True)
    image_5=models.ImageField(
        upload_to='about/photo_gallery', blank=True)
    image_6=models.ImageField(
        upload_to='about/photo_gallery', blank=True)

    def save(self, *args, **kwargs):
        if not self.id and about_model.objects.exists():
            raise ValidationError('There is can be only one JuicerBaseSettings instance')
        return super(about_model, self).save(*args, **kwargs)


class contacts_model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.CharField( max_length=255,blank=False)
    subject = models.CharField(max_length=255)
    phone_nr = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name
    # def save(self, *args, **kwargs):
    #     if not self.id and contacts_model.objects.exists():
    #         raise ValidationError('There is can be only one JuicerBaseSettings instance')
    #     return super(contacts_model, self).save(*args, **kwargs)

class contactinfo_model(models.Model):
    id = models.AutoField(primary_key=True)
    adress = models.CharField(max_length=250)
    email = models.CharField(max_length=255)
    phone_nr = models.CharField(max_length=255)


    def save(self, *args, **kwargs):
        if not self.id and contactinfo_model.objects.exists():
            raise ValidationError('There is can be only one JuicerBaseSettings instance')
        return super(contactinfo_model, self).save(*args, **kwargs)

class related_fields(models.Model):
    id= models.AutoField(primary_key=True)
    topics= models.CharField(blank=True, max_length=50)


    def __str__(self):
        return self.topics


class post_detail_model(models.Model):
    id = models.AutoField(primary_key=True)
    post_date=models.DateTimeField(auto_now_add=True, blank=True)
    post_head=models.CharField(blank=True, max_length=255)
    post_image_one= models.ImageField(blank=True, upload_to='post/images')
    post_text_one=models.TextField(blank=True)
    post_image_two=models.ImageField(blank=True, upload_to='post/images')
    post_text_two=models.TextField(blank=True)
    related_topics= models.ManyToManyField(related_fields)






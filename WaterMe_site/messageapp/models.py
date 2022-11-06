from django.db import models
from twilio.rest import Client
from django.core.cache import cache

class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def set_cache(self):
        cache.set(self.__class__.__name__, self)
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        self.set_cache()


    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


class TwilioAccount(SingletonModel):
    ssid = models.CharField(max_length= 80)
    authToken = models.CharField(max_length=80)

    def getssid(self):
        return self.ssid
    
    def getAuthToken(self):
        return self.authToken
    


class Plant(models.Model):
    plantid = models.AutoField(primary_key=True)
    plantName = models.CharField(max_length=255)

    def __str__(self):
        return self.plantName



class SensorData(models.Model):
    sensorid = models.AutoField(primary_key=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    temperature = models.IntegerField()
    humidity = models.IntegerField()

    def gethumidity(self):
        return self.humidity
    
    def gettemperature(self):
        return self.temperature


class Message(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=250)
    receiver = models.CharField(max_length=250)
    message = models.CharField(max_length=500)


    def __str__(self):
        return self.message + ' '
    
    def save(self, *arg, **kwargs):
        humidity = SensorData.gethumidity()
        if humidity < 60:
            pass
        if humidity > 70:
            pass

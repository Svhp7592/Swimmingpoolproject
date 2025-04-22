from django.db import models

# Create your models here.


class login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=225)
    password=models.CharField(max_length=225)
    usertype=models.CharField(max_length=225)
    
    
class parking_location(models.Model):
    location_id=models.AutoField(primary_key=True)
    location_name=models.CharField(max_length=225)
    place=models.CharField(max_length=225)

    latitude=models.CharField(max_length=225)
    longitude=models.CharField(max_length=225)
    description=models.CharField(max_length=225)
    
 

class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"
  

    location=models.ForeignKey(parking_location,on_delete=models.CASCADE)
    aamount=models.CharField(max_length=225)
  

class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=225)
    lname=models.CharField(max_length=225)
    hname=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    encode=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    latitude=models.CharField(max_length=225)
    longitude=models.CharField(max_length=225)
    

class booking(models.Model):
    book_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    starting_date=models.CharField(max_length=225)
    starting_time=models.CharField(max_length=225)
    ending_date=models.CharField(max_length=225)
    ending_time=models.CharField(max_length=225)
    slot=models.ForeignKey(slot,on_delete=models.CASCADE)
    amount=models.CharField(max_length=225)
    status=models.CharField(max_length=225)
    

class payment(models.Model):
    pay_id=models.AutoField(primary_key=True)
    book=models.ForeignKey(booking,on_delete=models.CASCADE)
    amount=models.CharField(max_length=225)
    mode_of_payment=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    status=models.CharField(max_length=225)
    

class complaint(models.Model):
    complaint_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    description=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    solution=models.CharField(max_length=225)
   
    status=models.CharField(max_length=225)
    
   

 


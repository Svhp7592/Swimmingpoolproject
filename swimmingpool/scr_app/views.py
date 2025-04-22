from django.shortcuts import render,HttpResponse

from scr_app.models import *
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.http import JsonResponse

# Create your views here.



def home(request):
    return render(request,'home.html')


def adminhome(request):
    return render(request,'adminhome.html')

def userhome(request):
    return render(request,'userhome.html')



def logins(request):
    if request.method=='POST':
        uname=request.POST['uname']
        psw=request.POST['psw']
        
        try:
            lg=login.objects.get(username=uname,password=psw)
            print(lg,"///////////////")
            
            request.session['login_id']=lg.pk
            lid=request.session['login_id']
            
            if lg.usertype=='admin':
                return HttpResponse("<script>alert('login successfull');window.location='adminhome';</script>")
            
            
            elif lg.usertype=='user':
                q=user.objects.get(login_id=lid)
                if q:
                    
                    request.session['user_id']=q.pk
                    
                    return HttpResponse("<script>alert('login successfull');window.location='userhome';</script>")
            
            
        except:
            return HttpResponse("<script>alert('login Failed...!!!!');window.location='login';</script>")
    

    return render(request,'login.html')


def manage_parking_location(request):
    q=parking_location.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        place=request.POST['place']
        latitude=request.POST['lati']
        longitude=request.POST['longi']
        des=request.POST['des']
        t=parking_location(location_name=name,place=place,latitude=latitude,longitude=longitude,description=des)
        t.save()
        return HttpResponse("<script>alert('Added successfully');window.location='/manage_parking_location';</script>")
    return render(request,'parkin_location_registration.html',{'q':q})


def user_reg(request):
    
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        
        hname=request.POST['hname']
        

        place=request.POST['place']
        encode=request.POST['encode']
        latitude=request.POST['lati']
        longitude=request.POST['longi']
        phone=request.POST['phone']
        email=request.POST['email']
        uname=request.POST['uname']
        psw=request.POST['psw']
        
        
        c=login(username=uname,password=psw,usertype='user')
        c.save()
        
        t=user(fname=fname,lname=lname,hname=hname,place=place,latitude=latitude,longitude=longitude,encode=encode,phone=phone,email=email,login=c)
        t.save()
        return HttpResponse("<script>alert('Added successfully');window.location='/login';</script>")
    return render(request,'user_reg.html')



# def slot_reg(request):
#     q=slot.objects.all()
#     d=parking_location.objects.all()
#     if request.method=='POST':
#         sd=request.POST['sd']
        
#         location=request.POST['location']
#         amount=request.POST['amount']
        
       
#         t=slot(slot_description=sd,slot_status='pending',location_id=location,aamount=amount)
#         t.save()
#         return HttpResponse("<script>alert('Added successfully');window.location='/slot_reg';</script>")
#     return render(request,'slot_registration.html',{'q':q,'d':d})
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import slot, parking_location
import qrcode

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        # border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    return img

def slot_reg(request):
    q = slot.objects.all()
    d = parking_location.objects.all()
    
    if request.method == 'POST':
        sd = request.POST['sd']
        location = request.POST['location']
        amount = request.POST['amount']
        
        t = slot(
            slot_description=sd,
            slot_status='free',
            location_id=location,
            aamount=amount,
            # qrcode=qr_code_filename 
            # Assuming 'qrcode' is the name of the column for storing QR code filename
        )
        t.save()
        
        obj=t.pk
        
        # Generate QR code
        qr_code_data = f"Slot ID: {obj}, Location: {location}, Amount: {amount}"
        qr_code_img = generate_qr_code(qr_code_data)
        
        # Save QR code image to a file
        qr_code_filename = f"qr_code_{sd}.png"
        qr_code_path = os.path.join(settings.MEDIA_ROOT, qr_code_filename)
        qr_code_img.save(qr_code_path)

        # Now, save the slot data along with the QR code filename in the database
        
        c=slot.objects.get(slot_id=obj)
        
        if c:
            c.qrcode=qr_code_filename
            c.save()
       

        return HttpResponse("<script>alert('Added successfully');window.location='/slot_reg';</script>")
    
    return render(request, 'slot_registration.html', {'q': q, 'd': d})



       



def admin_view_complaint(request):
  
 
    cus=complaint.objects.all()
   

    return render(request,'admin_view_complaint_and_send_reply.html',{'q':cus})

from datetime import *

def user_view_complaint(request):
  
 
    cus=complaint.objects.all()
    if request.method=='POST':
        complain=request.POST['comp']
        
       
        
        current_date = datetime.now().strftime('%Y-%m-%d')
       
        t=complaint(description=complain,date=current_date,status='pending',solution='pending',user_id=request.session['user_id'])
        t.save()
        return HttpResponse("<script>alert('Added successfully');window.location='/user_view_complaints';</script>")

    return render(request,'user_send_complaint.html',{'q':cus})


def slot_status(request):
  
 
    cus=slot.objects.all()
    

    return render(request,'view_slots.html',{'q':cus})

def admin_view_user(request):
  
 
    cus=user.objects.all()

    return render(request,'view_user.html',{'q':cus})


def admin_view_booking(request):
  
 
    cus=booking.objects.all()

    return render(request,'view_booking.html',{'q':cus})


def admin_view_payment(request):
  
 
    cus=payment.objects.all()

    return render(request,'view_payments_reports.html',{'q':cus})



def send_reply(request,id):
    
    q=complaint.objects.get(complaint_id=id)
    if request.method=='POST':
        q.solution=request.POST['reply']
        q.status='replied'
        q.save()
        
        return HttpResponse("<script>alert('Replied');window.location='/admin_view_complaint';</script>")
    

    return render(request,'send_reply.html')



def view_profile(request):
  
 
    cus=user.objects.filter(user_id=request.session['user_id'])

    return render(request,'user_profile.html',{'q':cus})

# def view_near(request):
  
 
#     cus=parking_location.objects.all()

#     return render(request,'user_nearby_location.html',{'q':cus})
import requests
from django.shortcuts import render
from .models import parking_location
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def view_near(request):
    try:
        # Retrieve current location
        current_location = get_location()
        if current_location:
            latitude, longitude = map(float, current_location.get('loc').split(','))

            # Retrieve parking locations
            parking_locations = parking_location.objects.all()

            # Calculate distance from current location to each parking location
            for location in parking_locations:
                location_latitude = float(location.latitude)
                location_longitude = float(location.longitude)
                distance = geodesic((latitude, longitude), (location_latitude, location_longitude)).kilometers
                location.distance_from_current = distance  # Add distance to the parking location object

            # Sort parking locations by distance in ascending order
            parking_locations = sorted(parking_locations, key=lambda x: x.distance_from_current)

            # Pass parking locations to the template and render the HTML page
            return render(request, 'user_nearby_location.html', {'q': parking_locations})
        else:
            return render(request, 'error.html')
    except Exception as e:
        print(f"Error: {e}")
        return render(request, 'error.html')

def get_location():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def get_location_from_coordinates(latitude, longitude):
    geolocator = Nominatim(user_agent="reverse_geocoding_example")
    
    try:
        location = geolocator.reverse((latitude, longitude), language='en')
        return location.address if location else None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    
  





def slots(request,id):
  
 
    cus=slot.objects.filter(location_id=id)

    return render(request,'user_view_slot_status.html',{'q':cus})



def user_booking(request,id,am):
  
 
    
    if request.method=='POST':
        sd=request.POST['start_date']
        st=request.POST['start_time']
        
        # ed=request.POST['ending_date']
        # et=request.POST['ending_time']
        
        
       
        
        # current_date = datetime.now().strftime('%Y-%m-%d')
       
        t=booking(starting_date=sd,starting_time=st,ending_date='pending',ending_time='pending',user_id=request.session['user_id'],slot_id=id,status='pending',amount=am)
        t.save()
        
        f=slot.objects.get(slot_id=id)
        if f:
            f.slot_status='reserved'
            f.save()
        return HttpResponse("<script>alert('Reserved successfully');window.location='/user_view_booking';</script>")

    return render(request,'user_book_slot.html')




def user_view_booking(request):
  
 
    cus=booking.objects.filter(user_id=request.session['user_id'])

    return render(request,'user_view_booking.html',{'q':cus})


def scanner(request,id):
    # Fetch any additional data needed for the scanner page
    # For example, you might want to retrieve some default slot details or other information
    slot_details = {
        'id': 1,  # Example slot ID
        'slot_description': 'Example slot description',
        'location': 'Example location'
    }
    
    # Render the scanner.html template with the slot_details context
    return render(request, 'scanner.html', {'slot_details': slot_details})


def occupied(request):
    # Retrieve the QR code data from the URL parameters
    qr_code_data = request.GET.get('qrData', None)
    book_id = request.GET.get('book_id', None)

    # Initialize variables to store the extracted data
    slot_id = None
    slot_description = None
    location = None

    # Split the QR code data string if it's not None and contains the delimiter
    if qr_code_data:
        parts = qr_code_data.split(',')  # Assuming data is separated by comma
        if len(parts) >= 3:
            slot_description = parts[0].split(':')[1].strip()  # Extracting slot ID
            slot_id = parts[1].split(':')[1].strip()  # Extracting slot description
            location = parts[2].split(':')[1].strip()  # Extracting location

    # You can now use slot_id, slot_description, and location as needed in your view logic
    print("Book ID:", book_id)
    print("Slot ID:", slot_id)
    print("Slot Description:", slot_description)
    print("Location:", location)
    
    dd=slot.objects.get(slot_id=slot_id)
    
    ff=booking.objects.get(book_id=book_id)
    if dd and ff:
        dd.slot_status='occupied'
        dd.save()
        
        ff.status='occupied'
        ff.save()
        
        
        
        return HttpResponse("<script>alert('Occupied successfully');window.location='/user_view_booking';</script>")
    
    
    return render(request, 'occupied.html', {'slot_id': slot_id, 'slot_description': slot_description, 'location': location})



from django.shortcuts import render
from datetime import datetime

def pay(request, id, ids):
    print("kkkkk.......")
    z = booking.objects.get(book_id=id)
    v = slot.objects.get(slot_id=ids)
    
    am=v.aamount
    
    sd = z.starting_date
    st = z.starting_time
    dt = sd + ' ' + st
    print("DT : ", dt)

    # Combine starting date and time
    starting_datetime = datetime.strptime(dt, '%Y-%m-%d %H:%M')

    # Current date and time
    current_datetime = datetime.now()

    # Check if the current date and time are later than the starting date and time
    if current_datetime < starting_datetime:
        print("Error: Current date and time is earlier than the starting date and time.")
        total_cost = 0  # Set the total cost to 0 or handle it differently based on your requirements
    else:
        # Calculate the time difference
        time_difference = current_datetime - starting_datetime

        # Total difference in hours
        total_hours = time_difference.total_seconds() / 3600
        
                
        # Convert total hours to a timedelta object
        time_delta = timedelta(hours=total_hours)

        # Extract days, hours, minutes, and seconds from the timedelta
        days = time_delta.days
        hours, remainder = divmod(time_delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        print("Total Time: {} days, {} hours, {} minutes, {} seconds".format(days, hours, minutes, seconds))
                
        # Assign the total time to a variable
        total_time = {
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        }
        # Charge rate
        print("total_time : ",total_time)
        charge_rate_per_hour = am  # in rupees
        
        print(type(total_hours),"////////////////")
        
        print(type(charge_rate_per_hour),"///////////////////")
        

        # Total cost
        total_cost = total_hours * float(charge_rate_per_hour)
        print(type(total_cost))
        rounded_number = round(total_cost, 2)
        

    # Print the results
    print("Total Difference in Hours:", total_hours)
    print("Total Cost: {} rupees".format(total_cost))

    context = {
        'days': days,
        'hours' : hours,
        'minutes' : minutes,
        'total_cost': rounded_number
    }
    
    if request.method=='POST':
        current_date = current_datetime.date()
        current_time = current_datetime.time()
        v.slot_status='free'
        z.status='paid'
        z.amount=rounded_number
        z.ending_date=current_date
        z.ending_time=current_time
        v.save()
        z.save()
        return HttpResponse("<script>alert('Paid successfully');window.location='/user_view_booking';</script>")
    
        

    return render(request, 'payment.html', context)





    


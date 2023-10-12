
import requests
import os
from datetime import datetime

api = '5297e5ab64fe92bf6658c5855088e864'
fvrt_city = []
location = input("Enter the city name: ")

url= "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api
link = requests.get(url)
data = link.json()

#create variables to store and display data
temp_city = ((data['main']['temp']) - 273.15)
weather_desc = data['weather'][0]['description']
hmdt = data['main']['humidity']
wind_spd = data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("********************************************************")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("*********************************************************")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')


# crud operation is pending 
def add_(city):
    if city  not in fvrt_city:
        fvrt_city.append(city)
        print(f"{city} added to fvrt.")
        save_fvrt_city()
    else:
        print(f"{city} is already in your favorites.")
        print("current list of favorities:",fvrt_city)
        
        
def remove_(city):
    if city in fvrt_city:
        fvrt_city.remove(city)
        save_fvrt_city()
        print(f"{city} remove the city from your list.")
        
    else:
        print(f"{city} is not in your favorities.")
        
def update_(old_city_name, new_city_name):
    if old_city_name in fvrt_city:
        index = fvrt_city.index(old_city_name)
        save_fvrt_city()
        print(f"Update{old_city_name}to {new_city_name}")
        
    else:
        print(f"{old_city_name} is not in your favorites.")
        
        
def list_():
    if fvrt_city:
        print('Your favorite city ')
        for city in fvrt_city:
            print(city)
            
            
    else:
        print("You don't have any favorite city.") 
        
if __name__=="__main__":
    
    
    #    print("Let's do more operation by clicking the key --- \n")
    command = input("Enter the command for more options:: ")

while True:     
    if command == 1:
        # fvrt_city.append(city)
        # print("city is added successfully ")
        # save_fvrt_city()
        add_(city)
            
    elif command == 2:
        fvrt_city.remove(city)
        print("city is deleted successfuly ")
        save_fvrt_city()
    elif command == 3:
        index = fvrt_city.index(old_city_name)
        print("city is Updated")
        save_fvrt_city()
    elif command == 4:
            print("display the List")    
                    
    else:
        pass            
                    
else:
    print("Invalid key ")
            
       

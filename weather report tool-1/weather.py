from tkinter import *
from tkinter import messagebox
import requests, json

def tell_weather():
    api_key = "Your_api_key"
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    city_name = city_field.get()
    complete_url = base_url + 'appid =' + api_key + '&q =' + city_name

    response = requests.get(complete_url)

    x = response.json()
    
    if x['cod'] != "404":
        y = x['main']

        current_temperature = y['temp']
        current_pressure = y['pressure']
        current_humidity = y['humidity']

        z = x['weather']

        weather_description = z[0]['description']

        temp_field.insert(15, str(current_temperature) + ' Kelvin')
        atm_field.insert(10, str(current_pressure) + ' hPa')
        humid_field.insert(15, str(current_humidity) + ' %')
        desc_field.insert(10, str(weather_description) )

    else:
        messagebox.showerror("Error", "city is not found \n", "please enter valid city name..")
        city_field.delete(0, END)

def clear_all():
    city_field.delete(0, END)
    temp_field.delete(0, END)
    atm_field.delete(0, END)
    humid_field.delete(0, END)
    desc_field.delete(0, END)

    city_field.focus_set()

if __name__ == '_main_':
    root = Tk()
    root.title('GUI Application')
    root.config(background="light green")
    root.geometry("425x175")
    
    #creating the labels and designing their GUI user interface.
    headlabel = Label(root, text="Weather Report Application tool", fg = 'black', bg = 'red')

    label1 = Label(root, text= "City Name : ", fg = 'black', bg = 'dark green')

    label2 = Label(root, text= "Temperature : ", fb = 'black', bg ='dark green')

    label3 = Label(root, text= "ATM Pressure : ", fb = 'black', bg ='dark green')

    label4 = Label(root, text= "Humidity : ", fb = 'black', bg ='dark green')

    label5 = Label(root, text= "Description : ", fb = 'black', bg ='dark green')

    #creating the grid in GUI.
    headlabel.grid(row = 0, column = 1) 
    label1.grid(row = 1, column = 0, sticky ="E") 
    label2.grid(row = 3, column = 0, sticky ="E") 
    label3.grid(row = 4, column = 0, sticky ="E") 
    label4.grid(row = 5, column = 0, sticky ="E") 
    label5.grid(row = 6, column = 0, sticky ="E")

    #creating text entry books for inpur and output data for filling or typing the information.
    city_field = Entry(root)
    temp_field = Entry(root) 
    atm_field = Entry(root) 
    humid_field = Entry(root) 
    desc_field = Entry(root)

    #grid is for placing  the data in a table-like strucuture on GUI display.
    #the widgets are respectivie positions.
    city_field.grid(row = 1, column = 1, ipadx ="100") 
    temp_field.grid(row = 3, column = 1, ipadx ="100") 
    atm_field.grid(row = 4, column = 1, ipadx ="100") 
    humid_field.grid(row = 5, column = 1, ipadx ="100") 
    desc_field.grid(row = 6, column = 1, ipadx ="100")

    #now create a submit button to sbmit the input data - for tell weather().
    #create a clear button to clear the current input and out data history -for clear all().
    button1 = Button(root, text = "Submit", bg = "red", fg = "black", command = tell_weather)
    button2 = Button(root, text = "Clear", bg = "red", fg = "black", command = tell_weather)

    #new grid for placing the button on the GUI diplay as table-like structure.
    button1.grid(row = 2, column = 1)
    button2.grid(row = 7, column = 1)
    
    #start function and continue on a loop.
    root.mainloop()





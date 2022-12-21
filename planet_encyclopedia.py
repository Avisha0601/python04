from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Planet Encyclopedia")
root.geometry("500x500")
root.configure(background="cyan")

Mercury = ImageTk.PhotoImage(Image.open ("mercury.jpg"))
Venus = ImageTk.PhotoImage(Image.open ("venus.jpg"))
Earth = ImageTk.PhotoImage(Image.open ("earth.jpg"))

label_planet = Label(root, text="Planet : ", bg="cyan")
label_planet_name = Label(root,font=("courier",18,"bold"), bg="cyan")
label_planet_image = Label(root,bg="DarkSlateGray3", highlightthickness=5, borderwidth=2, relief=SOLID)
label_planet_gravity_radius = Label(root,font=("castellar"), bg="cyan")
label_planet_info = Label(root,font=("Broadway",10,"bold"), bg="cyan", wrap=500)

planets = ["Mercury","Venus","Earth"]
selectedval = StringVar()
dropdown = ttk.Combobox(root, values = planets, textvariable=selectedval)

def PlanetInfo():
    planet = selectedval.get()
    if planet == "Mercury":
        label_planet_name['text'] = "Mercury"
        label_planet_image['image'] = Mercury
        label_planet_gravity_radius['text'] = "Gravity : 3.7 m/s*m/s /n Radius : 2,439.7 km"
        label_planet_info['text'] = " Mercury is the smallest planet in the Solar System and the closest to the Sun. Its orbit around the Sun takes 87.97 Earth days, the shortest of all the Sun's planets."
    elif planet == "Venus":
        label_planet_name['text'] = "Venus"
        label_planet_image['image'] = Venus
        label_planet_gravity_radius['text'] = "Gravity : 8.87 m/s*m/s /n Radius : 6,051.8 km"
        label_planet_info['text'] = "Venus is the second planet from the Sun. It is sometimes called Earth's 'sister' or 'twin' planet as it is almost as large and has a similar composition. As an interior planet to Earth, Venus appears in Earth's sky never far from the Sun, either as morning star or evening star."
    elif planet == "Earth":
        label_planet_name['text'] = "Earth"
        label_planet_image['image'] = Earth
        label_planet_gravity_radius['text'] = "Gravity : 9.807 m/s*m/s /n Radius : 6,371 km"
        label_planet_info['text'] = "Earth is the third planet from the Sun and the only astronomical object known to harbor life. While large volumes of water can be found throughout the Solar System, only Earth sustains liquid surface water. About 71% of Earth's surface is made up of the ocean, dwarfing Earth's polar ice, lakes, and rivers."
dropdown.place(relx=0.5, rely=0.1 , anchor=CENTER)

btn = Button(root, text="Show Planet Info" , command=PlanetInfo)
btn.place(relx=0.5, rely=0.1, anchor=CENTER)

label_planet.place(relx=0.2, rely=0.1, anchor=CENTER)
label_planet_name.place(relx=0.5, rely=0.25, anchor=CENTER)
label_planet_image.place(relx=0.5, rely=0.5, anchor=CENTER)
label_planet_gravity_radius.place(relx=0.5, rely=0.8, anchor=CENTER)
label_planet_info.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()
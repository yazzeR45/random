import pandas as pd
import random
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Read the Excel file
df = pd.read_excel('Random Generator/random.xlsx')

count = 0
def generate_number():
    global count
    random_index = random.randint(0, len(df)-1)
    random_name = df.loc[random_index, 'Name']
    random_phone = df.loc[random_index, 'Phone']
    if count < 40:
        # Update the label with the new phone number
        phone_label.configure(text=str(random_phone))
        # Call the function again after 1000 milliseconds (1 second)
        root.after(100, generate_number)
        bar.start()
        count += 1
    else:
        root.after_cancel(generate_number)
        bar.stop()
        phone_label.configure(text="Congratulations " + random_name + " with phone number: " + str(random_phone))
        count = 0



    
# Create a tkinter window
root = Tk()
root.title("Phone Number Winner")
root.configure(bg='white')

# Add background image
image = Image.open("Random Generator/background.jpg")
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image=photo)
label.grid(row=0, column=0, rowspan=5)

# Create a label to display the message
label = ttk.Label(root, text="Press the button to generate a random phone number.", font=("Helvetica", 16), background="white", foreground="black")
label.grid(row=0, column=1, pady=10, padx=10)

# Create a label to display the phone number
phone_label = ttk.Label(root, text="", font=("Helvetica", 14), background="white", foreground="black")
phone_label.grid(row=1, column=1, pady=10, padx=10)

# Create a generate button to generate the random phone number
generate_button = ttk.Button(root, text="Generate", command=generate_number, width=20, style='Win.TButton')
generate_button.grid(row=2, column=1, pady=10, padx=10)

bar = ttk.Progressbar(root, orient='horizontal', length=200, mode='indeterminate')
bar.grid(row=3, column=1, pady=10, padx=10)

#Create a custom style for the buttons
style = ttk.Style()
style.configure('Win.TButton', font=("Helvetica", 14), background="white", foreground="black", relief=RAISED)

#Run the tkinter event loop
root.mainloop()

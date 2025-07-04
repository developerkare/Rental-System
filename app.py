from flask import Flask, render_template, redirect, url_for
import threading
import tkinter
import os

app = Flask(__name__)

# Import the tkinter login function from your module
def launch_tkinter_app():
    os.system(r'python "C:\Users\HILDA\Desktop\Paragon rentals\Management.py"')  # assuming your tkinter code is in rental_gui.py

@app.route('/')
def home():
    return render_template(r'C:\Users\HILDA\Desktop\Paragon rentals\Main.html')  # your HTML file with <li><a href="/management">Management</a></li>

@app.route('/management')
def management():
    # Run the Tkinter GUI in a separate thread
    threading.Thread(target=launch_tkinter_app).start()
    return "Rental Management GUI has been launched (check your desktop)."

if __name__ == '__main__':
    app.run(debug=True)

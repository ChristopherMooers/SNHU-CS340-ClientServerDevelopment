# SNHU CS-340: Client/Server Development

# About the Project/Project Title
This project implements a full-stack dashboard application using Python, MongoDB, and Dash. The application connects to the Austin Animal Center (AAC) dataset and provides an interactive interface for viewing, filtering, and analyzing animal records.
The dashboard integrates a previously developed CRUD Python module to retrieve and manipulate data from MongoDB. Users can interact with the data through filters, an interactive data table, a dynamic chart, and a geolocation map.
This project demonstrates client/server development by combining a database backend with a user-friendly front-end dashboard.

# Motivation
The motivation behind this project is to create a reusable and scalable way to interact with a MongoDB database using Python while also providing a user-friendly interface for data analysis.
Instead of manually running queries in the Mongo shell, this application allows users to interact with the data visually through a dashboard. This improves usability and efficiency, especially in real-world applications where non-technical users need access to data.

# Dashboard
The dashboard provides the following features:
•	Interactive data table with sorting, filtering, and pagination 
•	Radio button filters to categorize animals by rescue type: 
o	Water Rescue 
o	Mountain/Wilderness Rescue 
o	Disaster/Individual Tracking 
o	Reset (returns all data) 
•	Dynamic bar chart displaying the top 10 breeds in the current filtered view 
•	Geolocation map that updates based on selected table row 
•	Integration with MongoDB using a reusable CRUD module 
All dashboard components update dynamically based on user interaction.

# Getting Started
To run this project, the AAC dataset must first be imported into MongoDB and a user must be created for authentication.

Steps:
•	Ensure the dataset aac_shelter_outcomes.csv is imported into the aac database using mongoimport 
•	Create a MongoDB user (aacuser) with read/write permissions 
•	Open Codio and launch Jupyter Lab 
•	Open: 
o	CRUD_Python_Module.py 
o	ProjectTwoDashboard.ipynb 
•	Run the notebook to launch the dashboard 

The application connects to:
•	Database: aac 
•	Collection: animals

# Installation
This project uses the following tools:
•	Python – Used to build the application 
•	MongoDB – Database used to store animal shelter data 
•	PyMongo – Python driver used to connect to MongoDB 
•	Dash – Used to build the interactive dashboard interface 
•	Plotly Express – Used to create charts 
•	dash-leaflet – Used to display geolocation data 
•	Jupyter Notebook – Used to develop and run the dashboard 
•	Codio – Cloud-based development environment 

Rationale:
PyMongo was chosen because it is the official MongoDB driver for Python and integrates easily with CRUD operations. Dash was selected because it allows for rapid development of interactive web dashboards using Python.

# Usage
Run the ProjectTwoDashboard.ipynb file and execute all cells. The dashboard will launch in the browser, allowing interaction with the dataset through filters, charts, and maps.

Code Example:
# Example usage of the CRUD module within the dashboard application
from CRUD_Python_Module import AnimalShelter

shelter = AnimalShelter()

test_data = {
    "animal_id": "A999999",
    "animal_type": "Dog",
    "breed": "Labrador Retriever",
    "color": "Black",
    "name": "Test Dog"
}

print(shelter.create(test_data))
print(shelter.read({"animal_id": "A999999"}))

The CRUD module is used by the dashboard application to retrieve and filter data from MongoDB dynamically based on user interaction.

# Functionality:

Create (create)
•	Inserts a document into the database 
•	Returns True if successful, otherwise False 

Read (read)
•	Queries documents using a dictionary filter 
•	Uses MongoDB’s find() method 
•	Returns a list of matching documents or an empty list 
The read() method is used extensively in the dashboard to retrieve filtered data based on user-selected criteria.

Update (update)
•	Updates existing document(s) using a query filter 
•	Uses MongoDB’s update_many() method with the $set operator 
•	Returns the number of documents modified 

Delete (delete)
•	Removes document(s) based on a query filter 
•	Uses MongoDB’s delete_many() method 
•	Returns the number of documents deleted
Steps Taken to Complete Project
•	Imported the AAC dataset into MongoDB 
•	Created and tested the CRUD Python module 
•	Connected the dashboard to MongoDB using the module 
•	Built an interactive data table using Dash 
•	Implemented filter controls using radio buttons 
•	Created MongoDB queries to support filtering 
•	Developed a dynamic bar chart 
•	Implemented a geolocation map 
•	Tested all dashboard components

# Challenges
One challenge encountered was handling errors in Dash callbacks when components initially loaded with no selected values. This required implementing conditional checks to prevent runtime errors.
Another challenge was designing MongoDB queries that correctly filtered animal breeds for different rescue types. This required the use of regular expressions and testing different query structures.
These challenges were overcome through debugging, testing, and iterative development.

# Screenshots

Figure 1: Default Dashboard View (Unfiltered)
This screenshot shows the default dashboard view with all records displayed. The data table, bar chart, and geolocation map are fully populated before any filters are applied.
 
Figure 2: Water Rescue Filter Applied
This screenshot shows the dashboard after applying the Water Rescue filter. The data table, chart, and map update dynamically to display only relevant records.
 
Figure 3: Mountain/Wilderness Rescue Filter Applied
This screenshot shows the Mountain/Wilderness Rescue filter applied. All dashboard components update to reflect the filtered dataset.
 
Figure 4: Disaster/Individual Tracking Filter Applied
This screenshot shows the Disaster/Individual Tracking filter applied, demonstrating how the dashboard responds to user input.
 
Figure 5: Reset Filter
This screenshot shows the Reset option, which returns the dashboard to its original unfiltered state.

# Tests
The application was tested by interacting with each dashboard component:
•	Verified data loads correctly from MongoDB 
•	Tested each filter option 
•	Confirmed chart updates dynamically 
•	Confirmed map updates based on selected row 
•	Verified reset functionality returns all data

# Reflection Questions
1. How do you write programs that are maintainable, readable, and adaptable?
To create maintainable, readable, and adaptable programs, I focused on modular design and separating responsibilities across components. In this project, I developed a CRUD Python module that handled all database operations independently from the dashboard. This made the code easier to read and maintain because each part of the system had a clearly defined purpose.
The main advantage of this approach was reusability. When building the dashboard, I was able to reuse the CRUD module without rewriting database logic, which reduced errors and improved efficiency. In the future, this module could be reused in other applications such as APIs or data-driven web applications, making it a flexible and scalable solution.

2. How do you approach a problem as a computer scientist?
When approaching a problem as a computer scientist, I break the problem into smaller components and focus on understanding both technical requirements and user needs. In this project, I analyzed the requirements for the database and dashboard and translated them into functional features such as filtering, data display, and database interaction.
This project differed from previous assignments because it focused more on real-world, client-driven requirements rather than isolated coding problems. In the future, I would continue using strategies such as modular design, iterative testing, and requirement analysis to build systems that met client needs effectively.

3. What do computer scientists do, and why does it matter?
Computer scientists design systems that process, manage, and present data in meaningful ways. Their work is important because it helps organizations make better decisions and operate more efficiently.
In this project, the dashboard allows users to interact with animal shelter data quickly and visually. This helps organizations like Grazioso Salvare identify trends and make informed decisions. By turning raw data into useful insights, computer scientists help businesses improve their operations and effectiveness.

# Contact
Christopher Mooers


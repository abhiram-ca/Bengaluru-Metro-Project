# 🏙️ Bengaluru Metro Route Finder

A Flask-based web application to help users find the **shortest metro route** between any two stations in Bengaluru's metro network using **Dijkstra's algorithm**. It includes support for **interchange stations** and provides easy-to-understand route suggestions.

---

## 🚀 Features

- 🧭 Calculates shortest path between any two metro stations
- 🔄 Handles interchanges intelligently using a connected graph model
- 📊 Displays estimated travel time in minutes
- 🌐 Interactive HTML form-based UI for input and output
- 🧱 Scalable architecture — easy to extend to new metro lines and stations

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Algorithm:** Dijkstra’s algorithm (implemented with NumPy + heapq)
- **Routing Logic:** Interchange handling and adjacency matrix graph

---



## 📂 Project Structure

```bash
.
├── flaskcode.py         # Main Flask application
├── source_code.py       # Core Dijkstra algorithm and routing logic
├── templates/
│   └── index.html       # Frontend interface
🔧 Setup Instructions
Prerequisites
Python 3.x installed

pip for package management

Installation
bash
Copy
Edit
git clone https://github.com/yourusername/bengaluru-metro-route-finder.git
cd bengaluru-metro-route-finder
pip install flask numpy
Run the App
bash
Copy
Edit
python flaskcode.py
Then open your browser and visit:
http://127.0.0.1:5000

##🧠 How It Works
The application uses an adjacency matrix to model the metro graph.

Each station is assigned a unique index.

The Dijkstra algorithm computes the shortest path and estimated travel time.

Special logic handles interchange stations between metro lines (currently Majestic).

The result is rendered on the HTML page with route and interchange info.

##✍️ Author
Developed by [Your Name]

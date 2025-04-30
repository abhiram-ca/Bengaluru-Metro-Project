
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

## 📂 Project Structure

```
.
├── flaskcode.py         # Main Flask application
├── source_code.py       # Core Dijkstra algorithm and routing logic
├── templates/
│   └── index.html       # Frontend interface
```

---

## 🔧 Setup Instructions

### Prerequisites

- Python 3.x installed  
- pip for package management

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/bengaluru-metro-route-finder.git
cd bengaluru-metro-route-finder
pip install flask numpy
```

---

## 🚀 Run the App

```bash
python flaskcode.py
```

Then open your browser and visit:  
```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

- The application uses an **adjacency matrix** to model the metro graph.
- Each station is assigned a **unique index**.
- The **Dijkstra algorithm** computes the shortest path and estimated travel time.
- Special logic handles **interchange stations** between metro lines (currently Majestic).
- The result is **rendered on the HTML page** with route and interchange info.

---

## ✍️ Author

Developed by **Abhiram C A**  


---

## 📄 License

This project is licensed under the MIT License.

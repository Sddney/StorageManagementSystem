## **Storage management system**

Simple Storage Manager is a lightweight desktop application designed to manage a basic storage inventory. It focuses on the two core entities of any warehouse: Products and Categories.

The application provides a clean graphical user interface to perform standard CRUD operations.

### **Functionality**

**Category Management:**

- Add new product categories.
- View a list of all categories.
- Edit existing category names.
- Delete categories.

**Product Management:**

- Add new products with Name, Price, Quantity, and assigned Category.
- View all products.
- Edit product details.
- Delete products from the inventory.

**Route planning**

Beyond basic inventory management, the system integrates Dijkstra's shortest-path algorithm to calculate optimal transport routes between cities.

- Choose origin and destination from all cities in the dataset
- Calculates the minimum distance using Dijkstra's algorithm
- Displays the complete ordered list of cities on the route
- Handles disconnected graphs gracefully

## **Tech Stack**

- Programming language: Python 3
- Libraries: SQLite3, abc, copy, json, random, tkinter

## **How to run**

**Prerequisites**
- Python 3.10 or higher
- No external packages required — only the Python standard library is used 

```bash
# 1. Clone the repository
git clone https://github.com/Sddney/StorageManagementSystem.git
cd storage-management

# 2. Run the application
python main.py

# Note: On some Linux systems, Tkinter must be installed separately:
sudo apt-get install python3-tk
```

## **Usage Guide**

### Adding a category (required first)

1. Click **Add Category**
2. Enter a name (e.g. `Electronics`)
3. Select a transport destination city from the dropdown
4. Click **Commit** — a unique 4-digit ID is auto-generated

### Adding a product

1. Click **Add Product**
2. Fill in Name, Price (HKD), Quantity
3. Select a Category from the dropdown (populated from the database)
4. Click **Commit**

### Finding a route

1. Click **Route Between Cities**
2. Select the origin city from the **From** dropdown
3. Select the destination from the **Towards** dropdown
4. Click **Show Route**
5. The shortest distance (km) and full city path are displayed below

## **Task 1 - OOP concepts**

- Encapsulation: Private attributes, getter/setter methods, hidden SQL. Makes each class independently testable and replaceable.
#### Used: [ product.py, category.py, *_repository.py ]

- Inheritance: super().__init__(), shared parent attributes and methods. Adding a new entity is easier as the parent witing is already done.
#### Used: [ product_frame.py, category_frame.py, *_repository.py ]

- Polymorphism: Same method name, different behaviour per class. The same methods are implemented differently within different classes.
#### Used: All concrete frames, models, and repositories

- Abstraction: ABC + @abstractmethod contracts. Mandatory implementation of basic interface. Abstraction enforces consistency. 
#### Used: [ abstract_frame.py, repository_base.py, base_item.py ]

## **Task 2 - Data structure and Algorithm**

### Data structure
Graph: The city network is stored as a weighted adjacency list in cities.json

##№ This is a graph where:
- Each node is a city
- Each edge is a road connection
- Each weight is the distance in kilometres

```json
{
  "Blagodarnyy": [
    ["Budonnovsk", 70],
    ["Svetlograd", 68],
    ["Mineral'nyye Vody", 128],
    ["Nevinnomyssk", 176]
  ],
  "Budonnovsk": [
    ["Zelenokumsk", 60],
    ["Neftekumsk", 73]
  ]
}

```
**Data set was taken as an example data** 
https://www.kaggle.com/datasets/lightningforpython/russian-cities-distance-dataset


### Algorithm

Dijkstra Algorithm

**Algorithm walkthrough**
```
1. Set distance[start] = 0, all others = ∞
2. Copy graph into unseenNodes (working set)
3. WHILE unseenNodes is not empty:
      a. Pick the node with the smallest known distance  ← greedy choice
      b. For each neighbour:
            if current_distance + edge_weight < known_distance:
                update known_distance
                record predecessor
      c. Remove current node from unseenNodes
4. Backtrack through predecessor map: end → start
5. If distance[end] == ∞ → return "Path not reachable"
   Else → return (distance, path)
```

**Example output**
From:    Blagodarnyy
To:      Budonnovsk

Distance: 70 km
Path:     Blagodarnyy -> Budonnovsk


## **Project Architecture**

```
┌─────────────────────────────────────────────────────────────┐
│                     PRESENTATION LAYER                      │
│                       gui_commands.py                       │
│  ┌──────────────────┐ ┌──────────────────┐ ┌─────────────┐  │
│  │  product_frame   │ │  category_frame  │ │ route_frame │  │
│  └──────────────────┘ └──────────────────┘ └─────────────┘  │
|        ↑ both inherit AbstractFrame (ABC)                   |
└──────────────────────────┬──────────────────────────────────┘
                           │ 
┌─────────────────────────────────────────────────────────────┐
│                    BUSINESS LOGIC LAYER                     │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────────────┐ │
│  │  product.py  │  │ category.py  │  │ dijkstra_algorithm │ │
│  └──────────────┘  └──────────────┘  └────────────────────┘ │
|    ↑ both inherit BaseItem (ABC)                            |
└──────────────────────────┬──────────────────────────────────┘
                           │ 
┌─────────────────────────────────────────────────────────────┐
│                     DATA ACCESS LAYER                       │
|                database_initialization.py                   |
│  ┌─────────────────────┐    ┌──────────────────────────┐    │
│  │ category_repository │    │   product_repository     │    │
│  └─────────────────────┘    └──────────────────────────┘    │
│         ↑ both inherit DatabaseMethods (ABC)                │
└──────────────────────────┬──────────────────────────────────┘
                           │
            [ StorageManager ] -> storage_database.db
```

## Project Structure
```
storage-management/
│
├── main.py                          # Application entry point
│
├── GUI/
│   ├── abstract_frame.py            # AbstractFrame (ABC) — defines CRUD interface
│   ├── gui_commands.py              # Main window layout and button wiring
│   ├── product_frame.py             # ProductFrame — manages product UI
│   ├── category_frame.py            # CategoryFrame — manages category UI
│   └── route_frame.py               # RouteFrame — city route overlay
│
├── models/
|   ├── base_item.py                 # Base model (Abstraction)
│   ├── product.py                   # Product model (Encapsulation)
│   └── category.py                  # Category model (Encapsulation)
│
├── database/
│   ├── repository_base.py          # DatabaseMethods (ABC) — CRUD interface
│   ├── category_repository.py       # CategoriesRepository (Inheritance)
│   ├── product_repository.py        # ProductsRepository (Inheritance)
│   └── databases_initialization.py  # Singleton-style shared DB instances
│
├── algorithm/
│   ├── dijkstra_algorithm.py        # Dijkstra's algorithm + ReturnCities()
│   └── cities.json                  # City graph dataset (Kaggle)
|
├── StorageManagement/
│   └── storage_manager.py                  # SQLite Database management 
│
└── README.md
```

## Database Schema

The SQLite database (`database/storage_database.db`) contains two tables:

```sql
CREATE TABLE categories (
    category_name  TEXT,
    category_id    INTEGER,   -- 4-digit unique ID, generated randomly
    transport_to   TEXT       -- destination city name
);

CREATE TABLE products (
    product_name      TEXT,
    product_price     INTEGER,
    product_quantity  INTEGER,
    product_category  TEXT,   -- matches a category_name
    product_id        INTEGER -- 4-digit unique ID, generated randomly
);
```

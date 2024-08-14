
# RDF Extractor and Visualizer: A Semantic Web Data Explorer

## Overview

This application is designed to extract and visualize RDF (Resource Description Framework) structures from the content of HTML pages. It provides an intuitive interface for both viewing the extracted RDF data as text and visualizing the data as an interactive graph.

## Goal of the Application

The primary goal of this application is to streamline the process of extracting RDF data embedded in HTML pages and to provide tools for both textual and graphical exploration of the RDF structure. This makes it easier to understand the relationships and semantics of the data embedded within web pages.

The application aims to:

- **Extract RDF Data**: Automatically parse and extract RDF triples from the content of HTML pages.
- **Display RDF Structure**: Present the extracted RDF data as text within the application's interface for easy review and analysis.
- **Visualize RDF Data**: Offer an interactive graph visualization of the RDF structure, enabling users to explore the relationships between different entities in a more intuitive way.

## How the Application Works

### Key Features

1. **Extract RDF from HTML**: The application processes the content of HTML pages to extract RDF triples, which represent the relationships between entities described in the HTML.

2. **Textual Display**: The extracted RDF triples are displayed as text within the application, allowing users to see the structure of the data in a straightforward format.

3. **Visualize RDF as a Graph**: The application includes a "Visualize" button that converts the textual RDF data into a graphical representation, making it easier to understand complex relationships.

4. **Save and Export**: Users can save the visualized graph as an HTML file, which can be opened in any web browser for further exploration or sharing.

### How It Works

1. **HTML Input**: The user provides an HTML page, which the application then processes to extract any embedded RDF data.

2. **RDF Extraction**: The application parses the HTML content, identifies RDF triples, and extracts them. This involves processing RDFa, JSON-LD, or other embedded RDF formats.

3. **Textual RDF Display**: The extracted RDF triples are shown as plain text in the application's interface, displaying the subject-predicate-object structure.

4. **Graph Visualization**: By clicking the "Visualize" button, the RDF data is transformed into an interactive graph. Nodes represent entities (subjects and objects), and edges represent relationships (predicates).

5. **Output**: The graph visualization can be saved as an HTML file, allowing users to view and share the graph outside the application.


### File Architecture

```
/semantic_web_app
│
├── /gui
│   ├── app_ui.py                # Contains the generated UI code from Qt Designer (.ui file converted to Python)
│   ├── main_window.py           # Manages the main window and the GUI logic for the application
│   └── __init__.py              # Makes the `gui` directory a package
│
├── /scraper
│   ├── scraper.py               # Contains logic for scraping HTML content from web pages or local files
│   └── __init__.py              # Makes the `scraper` directory a package
│
├── /rdf
│   ├── rdf_manager.py           # Contains logic to create RDF graphs from extracted entities and relations
│   ├── rdf_graph_visualizer.py  # Handles the logic to visualize RDF graphs using Graphviz or a similar tool
│   └── __init__.py              # Makes the `rdf` directory a package
│
├── main.py                      # Main entry point for the application; initializes the GUI and starts the app
└── README.md                    # Documentation file explaining how to set up and run the application
```

### Brief Explanation of Each File

#### 1. `/gui/app_ui.py`
- **Purpose**: This file is auto-generated from a `.ui` file created in Qt Designer. It contains the layout and widget definitions for the main window of the application.
- **Explanation**: This file is not typically edited manually. Instead, it is generated from a visual designer tool, making it easier to design complex UIs.

#### 2. `/gui/main_window.py`
- **Purpose**: This file contains the logic for interacting with the GUI elements defined in `app_ui.py`.
- **Explanation**: It connects user actions (like button clicks) to the appropriate methods (e.g., extracting data, visualizing the RDF graph). It also handles the integration of different components of the application.

#### 3. `/scraper/scraper.py`
- **Purpose**: This file contains the logic to scrape HTML content from either a provided URL or a local file path.
- **Explanation**: It retrieves the raw HTML content, which will later be processed for entity and relationship extraction.

#### 4. `/rdf/rdf_manager.py`
- **Purpose**: This file is responsible for creating RDF graphs from the extracted entities and relationships.
- **Explanation**: It uses libraries like `rdflib` to construct RDF triples, which represent the relationships between entities in a structured format.

#### 5. `/rdf/rdf_graph_visualizer.py`
- **Purpose**: This file handles the visualization of RDF graphs.
- **Explanation**: It converts the RDF graph into a visual format (e.g., using Graphviz or D3.js) and generates an HTML file (`rdf_graph.html`) that can be viewed in a browser.

#### 6. `main.py`
- **Purpose**: The main entry point for the application.
- **Explanation**: This script initializes the application, creates the main window, and starts the event loop for the GUI. It's the script you run to start the application.


### Summary

This file architecture organizes the application into modular components, each with a clear responsibility. The `gui` directory manages the user interface, `scraper` handles content extraction, and `rdf` deals with semantic web logic (RDF creation and visualization). This structure promotes maintainability and scalability, allowing you to easily add features or make changes to specific parts of the application.

### 1. **User Interface (UI)**

- **GUI Framework**: The application uses a graphical user interface built with `tkinter` (or another GUI framework you might be using).
- **Main Window**: The main window allows users to input HTML content, view extracted RDF data, and visualize it as a graph.

### 2. **RDF Extraction**

- **HTML Parser**: A module responsible for parsing HTML content to locate and extract RDF data. This may involve processing RDFa, JSON-LD, or microdata embedded in the HTML.
- **RDF Triple Generator**: After extraction, the RDF data is converted into triples (subject-predicate-object) for display and visualization.

### 3. **Textual Display of RDF**

- **RDF Text Renderer**: This component takes the RDF triples and formats them for display in a text box within the application. Users can easily read and analyze the RDF structure.

### 4. **Graph Visualization**

- **Visualization Engine**: The application uses the `pyvis` library to create interactive graph visualizations of the RDF data. The engine handles layout, styling, and interactivity.
- **HTML Output**: The visualized graph is saved as an HTML file, which can be viewed in a web browser.

### 5. **Backend Logic**

- **Controller Module**: The backend logic manages the workflow of the application, from RDF extraction to visualization. It handles user interactions, coordinates between the HTML parser and the visualization engine, and ensures smooth operation.

### 6. **Error Handling and Debugging**

- **Logging**: The application includes logging mechanisms to capture and record any errors or issues that occur during execution.
- **Exception Handling**: Robust exception handling ensures that errors are managed gracefully, providing feedback to the user when something goes wrong.

## Getting Started

### Prerequisites

- **Python 3.7+**
- **Required Python Libraries**: Install the required libraries using `pip install -r requirements.txt`.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/RDF_Extractor_and_Visualizer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd RDF_Extractor_and_Visualizer
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Execute the main script:
   ```bash
   python main.py
   ```
2. Use the GUI to load an HTML file, view the extracted RDF data, and visualize the RDF structure.


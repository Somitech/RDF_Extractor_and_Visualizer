from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from .app_ui import Ui_MainWindow
from scraper.scraper import scrape_page
from rdf.rdf_manager import create_rdf_graph
from rdf.rdf_graph_visualizer import visualize_rdf_graph
from pathlib import Path
import rdflib

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.extractButton.clicked.connect(self.extract_data)
        self.visualizeButton.clicked.connect(self.visualize_graph)

    def extract_data(self):
        url = self.urlInput.text()
        page_content = ""
        if url.startswith('http'):
            page_content = scrape_page(url)
        else:
            try:
                # Convert local file path to URI
                file_path = Path(url).resolve().as_uri()
                with open(url, 'r', encoding='utf-8') as file:
                    page_content = file.read()
                url = file_path  # Use the file path URI
            except Exception as e:
                print(f"Error reading file {url}: {e}")
        
        if page_content:
            self.rdf_graph = create_rdf_graph(url, page_content)
            # Display RDF graph in Turtle format in the text widget
            rdf_data = self.rdf_graph.serialize(format='turtle')
            self.rdfOutput.setPlainText(rdf_data)
            # Link with external RDF repositories
            self.link_with_external_repositories(self.rdf_graph)

    def visualize_graph(self):
        if hasattr(self, 'rdf_graph'):
            visualize_rdf_graph(self.rdf_graph)
            self.show_graph_window()

    def show_graph_window(self):
        self.graph_window = QWidget()
        self.graph_window.setWindowTitle("RDF Graph Visualization")
        
        layout = QVBoxLayout()
        web_view = QWebEngineView()
        web_view.setUrl(QUrl.fromLocalFile(str(Path("rdf_graph.html").resolve())))
        
        layout.addWidget(web_view)
        self.graph_window.setLayout(layout)
        self.graph_window.show()

    def link_with_external_repositories(self, rdf_graph):
        # Example SPARQL query to link with an external RDF repository
        sparql_query = """
        SELECT ?subject ?predicate ?object
        WHERE {
            ?subject ?predicate ?object.
        } LIMIT 10
        """
        sparql_endpoint = "http://dbpedia.org/sparql"
        external_graph = rdflib.ConjunctiveGraph('SPARQLStore')
        external_graph.open(sparql_endpoint)
        results = external_graph.query(sparql_query)
        for subj, pred, obj in results:
            print(subj, pred, obj)

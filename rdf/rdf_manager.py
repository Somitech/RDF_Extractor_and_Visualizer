import rdflib
from bs4 import BeautifulSoup
import spacy
import urllib.parse

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def create_rdf_graph(url, html_content):
    g = rdflib.Graph()
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract title
    title = soup.title.string if soup.title else 'No Title'
    g.add((rdflib.URIRef(urllib.parse.quote(url, safe=':/')), rdflib.RDFS.label, rdflib.Literal(title)))
    
    # Extract text content for NLP processing
    text_content = soup.get_text()
    
    # Process text with spaCy
    doc = nlp(text_content)
    
    # Extract entities and relationships
    entities = extract_entities(doc)
    relations = extract_relationships(doc)
    
    # Add entities to RDF graph
    for entity_text, entity_label in entities:
        entity_uri = rdflib.URIRef(f"{urllib.parse.quote(url, safe=':/')}#{urllib.parse.quote(entity_text.replace(' ', '_'))}")
        g.add((entity_uri, rdflib.RDFS.label, rdflib.Literal(entity_text)))
        g.add((entity_uri, rdflib.RDF.type, rdflib.URIRef(f"http://example.org/{entity_label}")))
    
    # Add relationships to RDF graph
    for subj, pred, obj in relations:
        subj_uri = rdflib.URIRef(f"{urllib.parse.quote(url, safe=':/')}#{urllib.parse.quote(subj.replace(' ', '_'))}")
        obj_uri = rdflib.URIRef(f"{urllib.parse.quote(url, safe=':/')}#{urllib.parse.quote(obj.replace(' ', '_'))}")
        pred_uri = rdflib.URIRef(f"http://example.org/{urllib.parse.quote(pred.replace(' ', '_'))}")
        g.add((subj_uri, pred_uri, obj_uri))
    
    return g

def extract_entities(doc):
    # Extract named entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def extract_relationships(doc):
    # Extracting subject-predicate-object triples
    relations = []
    for sent in doc.sents:
        for token in sent:
            if token.dep_ in ("nsubj", "nsubjpass"):
                subj = token.text
                pred = token.head.text
                obj = [child.text for child in token.head.children if child.dep_ in ("dobj", "attr", "prep")]
                if obj:
                    relations.append((subj, pred, obj[0]))
    return relations
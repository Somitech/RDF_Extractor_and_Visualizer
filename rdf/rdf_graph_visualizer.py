from pyvis.network import Network
import rdflib

def visualize_rdf_graph(rdf_graph, output_path="rdf_graph.html"):
    net = Network(directed=True)
    
    for subj, pred, obj in rdf_graph:
        subj_label = str(subj)
        pred_label = str(pred)
        obj_label = str(obj)
        
        net.add_node(subj_label, label=subj_label, title=subj_label)
        net.add_node(obj_label, label=obj_label, title=obj_label)
        net.add_edge(subj_label, obj_label, title=pred_label, label=pred_label)
    
    net.show(output_path)

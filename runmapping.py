import os
import morph_kgc

from rdflib.graph import Graph

file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"data\outsiders_2021.parquet")
#file_path = "data/2019-01-01/ocds-0c46vo-0009-DN379620-1-tender-release.xml"
rml = os.path.join(os.path.dirname(os.path.realpath(__file__)),"rml-mappings\mappingOCDS.rml.ttl")
#rml = "rml-mappings/mapping.ttl"


# configuration file
config_morph = """
                            [DataSource1]
                            file_path=""" + file_path + """
                            mappings=""" + rml


#g = Graph()
#print(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data\outsiders_2021.parquet'))
#g.parse(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data\outsiders_2021.parquet'))

#mapping_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'rml-mappings\mappingOCDS.rml.ttl')
#config = f'[CONFIGURATION]\noutput_format=N-QUADS\n[DataSource]\nmappings={mapping_path}'
g = morph_kgc.materialize(config_morph)


# work with the graph
g.serialize(destination= os.path.join(os.path.dirname(os.path.realpath(__file__)),'results/parquet.nt'), format='nt')
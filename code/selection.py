from bs4 import BeautifulSoup
from okr_types import Generator

class Selection(Generator):
    def __init__(self):
        self._results = {}
        
    def select(self, instances, org_of_interest, number_of_majors):
        Generator.select(self, instances, org_of_interest, number_of_majors)
        
        for i in instances: # For every instance of a JHU organization (i.e. for every JHU organization)
            org_label = i._label._class_label # Initialize org_label = the current organization's class label
            feature_dict = i._feature_vector._fv # Initialize feature_dict = the current organization's
            
            if org_label == org_of_interest:
                for k, v in feature_dict.iteritems():
                    self._results[k] = v
            
        
    def generate(self, instance, feature_of_interest):
        Generator.generate(self, instance, feature_of_interest)
        feature_dict = instance._feature_vector._fv
        result = ""
        
        if feature_of_interest == "geo":
            result = feature_dict[1]
        else:
            result = feature_dict[0]
        
        return result
    
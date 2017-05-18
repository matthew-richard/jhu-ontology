from abc import ABCMeta, abstractmethod
from _collections import defaultdict

# abstract base class for defining labels
class Label:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __str__(self): pass

       
class ClassificationLabel(Label):
    def __init__(self, label):
        self._class_label = label
        
    def __str__(self):
        return str(self._class_label)

class FeatureVector:
    def __init__(self):
        self._fv = defaultdict(float)
        pass
        
    def add(self, index, value):
        self._fv[index] = value
        pass
        
    def get(self, index):
        return self._fv.get(index, 0.0)

class Instance:
    def __init__(self, feature_vector, label):
        self._feature_vector = feature_vector
        self._label = label

# abstract base class for defining generators
class Generator:
    __metaclass__ = ABCMeta

    @abstractmethod
    def select(self, instances, org_of_interest, number_of_majors): pass
    
    @abstractmethod
    def generate(self, instance, feature_of_interest): pass
        
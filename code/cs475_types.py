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
    
class Cluster:
    def __init__(self, instances, mean_vector):
        self._instances = instances
        self._mean_vector = mean_vector

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
        
class MeanVector:
    def __init__(self):
        self._mv = {}
        pass
        
    def add(self, index, value):
        self._mv[index] = value
        pass
        
    def get(self, instances, index):
        return self._mv.get(index, 0.0)

# abstract base class for defining predictors
class Predictor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def train(self, instances, online_training_iterations): pass
    
    @abstractmethod
    def predict(self, instance): pass
        
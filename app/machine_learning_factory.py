from app.core.service.classify import Classify

class MachinLearningFactory:
    def __init__(self, type:str) -> None:
        self.type = type
        
    def prepare(self):
        if self.type == 'image':
            return Classify()
        else:
            return False
class TodoList:
    def __init__(self):
        self.lista = {}

    def add_task(self, zadanie):
        if zadanie not in self.lista:
            self.lista[zadanie] = False
    
    def complete_task(self, zadanie):
        if zadanie in self.lista:
            self.lista[zadanie] = True
            
    def get_active_tasks(self):
        return [zadanie for zadanie, skonczone in self.lista.items() if not skonczone]

    def get_completed_tasks(self):
        return [zadanie for zadanie, skonczone in self.lista.items() if skonczone]
    
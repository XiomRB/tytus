import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
sys.path.append('../tytus/storage')
from querie import * 
from environment import * 

class Use(Querie):
    def  __init__(self, database, row, column):
        Querie.__init__(self, row, column)
        self.database = database
    
    def execute(self, environment):
        if not isinstance(self.database, str):
            return {'Error': 'El argumento no es un id, por favor verifique la sintaxis.', 'Linea': self.row, 'Columna': self.column}
        environment.setActualDataBase(self.database)
        return 'Se ha referenciado la base de datos ' +  self.database 
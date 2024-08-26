import psycopg2
class Conectar():
    def __init__(self):
        pass    
    def peticion_expediente(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido):
        try:
                connection = psycopg2.connect(
                    host='localhost',
                    user='siap',
                    password='123',
                    database='siap'
                )
                print("Conexión éxitosa")
                cursor = connection.cursor()
                query = """SELECT a.expediente FROM mnt_expediente AS a INNER JOIN mnt_paciente AS b ON a.id_paciente = b.id_paciente
                            WHERE b.primer_nombre = %s 
                            AND b.segundo_nombre = %s 
                            AND b.primer_apellido = %s 
                            AND b.segundo_apellido = %s;
                        """
                params = (primer_nombre, segundo_nombre, primer_apellido, segundo_apellido)
                cursor.execute(query, params)
                row=cursor.fetchone()
                
        except Exception as ex:
                print(ex)  

        return row
       
            
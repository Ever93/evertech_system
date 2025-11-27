# app/repositories/users_repo.py
from app.database.connection import Database
from psycopg2 import OperationalError, Error


class UsersRepo:

    @staticmethod
    def find_by_credentials(nombre, password):
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            query = """
                SELECT id, nombre, correo, telefono, direccion, rol
                FROM usuarios
                WHERE nombre = %s AND password = %s
            """
            cursor.execute(query, (nombre, password))
            user = cursor.fetchone()
            cursor.close()
            conn.close()

            if user is None:
                raise ValueError("Usuario o contraseña incorrectos")

            return user

        except OperationalError:
            raise ConnectionError("No se pudo conectar a la base de datos")
        except Error as e:
            raise Exception(f"Error en la consulta: {e}")

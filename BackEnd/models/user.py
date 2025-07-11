from config import get_db_connection

class User:
    def __init__(self, id_usuario=None, nome=None, email=None, senha=None, tipo=None):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo

    @classmethod
    def authenticate(cls, email, senha):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT id_usuario, nome, tipo FROM usuario WHERE email = %s AND senha = %s",
                (email, senha)
            )
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def create(cls, nome, senha, email, tipo):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuario (nome, senha, email, tipo) VALUES (%s, %s, %s, %s)",
                (nome, senha, email, tipo)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def get_by_id(cls, user_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT id_usuario, nome, email, tipo FROM usuario WHERE id_usuario = %s",
                (user_id,)
            )
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def get_by_email(cls, email):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE email = %s", (email,))
        user = cursor.fetchone()
        conn.close()
        return user

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT id_usuario, nome, email, tipo FROM usuario")
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def update(cls, id_usuario, nome, senha, email, tipo):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE usuario SET nome = %s, senha = %s, email = %s, tipo = %s WHERE id_usuario = %s",
                (nome, senha, email, tipo, id_usuario)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def delete(cls, id_usuario):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM usuario WHERE id_usuario = %s", (id_usuario,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()



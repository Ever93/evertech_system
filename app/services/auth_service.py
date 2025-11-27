# app/services/auth_service.py
from app.repositories.users_repo import UsersRepo


class AuthService:

    @staticmethod
    def login(nombre, password):
        try:
            user = UsersRepo.find_by_credentials(nombre, password)
            return user
        except ValueError as ve:
            raise ve
        except ConnectionError as ce:
            raise ce
        except Exception as e:
            raise e

from google.cloud import firestore
from typing import Union
from messages.user import User 
client = firestore.Client()

class UserDao:
    @staticmethod
    def get(login: str) -> Union[User, None]:
        try:
            kind = 'users'
            query_ref = client.collection(kind).where("login", "==", login).limit(1)
            for doc in query_ref.stream():
                user = doc.to_dict()
            return user
        except Exception as e:
            print(e)
        return None

from google.cloud import firestore
from messages.contact import Contact

client = firestore.Client()


class ContactDao:
    @staticmethod
    def create(contact: Contact) -> None:
        try:
            kind = "contacts"
            doc = client.collection(kind).document()
            doc.set(
                {
                    "first_name": contact.first_name,
                    "last_name": contact.last_name,
                    "email": contact.email,
                    "number": contact.number,
                    "message": contact.message,
                }
            )
        except Exception as e:
            print(e)

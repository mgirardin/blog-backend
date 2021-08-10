from google.cloud import firestore
from messages.subscriber import Subscriber
client = firestore.Client()

class SubscriberDao:
    @staticmethod
    def create(subscriber: Subscriber) -> None:
        try:
            kind = 'subscribers'
            doc = client.collection(kind).document()
            doc.set({ 'email': subscriber.email })
        except Exception as e:
            print(e)
from database.models import Test, Card, Sound, TestCard
from app.utils import generate_audio
from uuid import uuid4


def add_test():
    sound = Sound(filename="source", creator="admin", length=6).save()
    card = Card(
        name="card name", type="card type", details={"ImgSrc": "image source"}
    ).save()
    test_card_1 = TestCard()
    test_card_1.card = card
    test_card_1.sound = sound
    test_card_1.save()
    test = Test(name="test name", cards=[test_card_1])
    test.save()
    print(test.to_dbref())
    return test.to_json()

def text_to_speech(text, creator, length):
    sound_exists = Sound.objects(text=text).first()
    if sound_exists:
        return sound_exists.filename
    filename = generate_audio(text)
    sound = Sound(filename=filename, text=text, creator=creator, length=length)
    sound.save()
    return filename

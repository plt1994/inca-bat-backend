from database.models import Test, Card, Sound, TestCard
from uuid import uuid4


def add_test():
    sound = Sound(src="source").save()
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

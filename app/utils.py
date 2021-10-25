from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from uuid import uuid4

from database.models import Sound

apikey = "0yUPmJ0cSMJm2BqOhpVq8WteLPLzy9jg1znPSktk1DJH"
url = "https://api.us-south.text-to-speech.watson.cloud.ibm.com"

authenticator = IAMAuthenticator(apikey)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)
text_to_speech.set_service_url(url)

def generate_audio(audio_content:str):
    filename = f"{uuid4().hex}.mp3"
    with open(f'static/sounds/{filename}', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                audio_content,
                voice='en-US_AllisonV3Voice',
                accept='audio/mp3'
            ).get_result().content)
    return filename

# request = {
#     "text": "Hello world",
#     "creator": "user name"
# }

# response = {
#     "filename": "asdads.mp3",
#     "source": "aws.asdasd.com/asdasd",
#     "lenght": "11"
# }

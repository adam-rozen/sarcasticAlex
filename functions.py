#! /usr/bin/env python3
import requests
import RPi.GPIO as GPIO   # Import the GPIO library.

def get_token(subscription_key):
    fetch_token_url = 'https://eastus.api.cognitive.microsoft.com/sts/v1.0/issuetoken'
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key
    }
    response = requests.post(fetch_token_url, headers=headers)
    access_token = str(response.text)
    print(access_token)

def getSpeech(subscription_key, speech):

    # text to speech url
    tts_east_us_url = 'https://eastus.tts.speech.microsoft.com/cognitiveservices/v1'

    text = ''

    with open(speech, 'r') as in_file:
        for line in in_file:
            text += line

    # ssml xml
    body = '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">\
            <voice name="en-US-JennyNeural">'\
                + text+\
            '</voice>\
            </speak>'

    # output format
    output = "riff-24khz-16bit-mono-pcm"

    # content type
    content_type = 'application/ssml+xml'

    # application name
    user_agent = 'SarcasticAlex'

    # headers
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-Type' : content_type,
        'X-Microsoft-OutputFormat': output,
        'User-Agent': user_agent
    }

    return requests.post(url=tts_east_us_url, data=body, headers=headers)

def getText(subscription_key, speech):
    # language
    language = 'en-US'

    # profanity
    profanity = 'raw'

    # speech to text url
    stt_eastus_url = 'https://eastus.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language='+language+'&profanity='+profanity

    # content_type
    content_type='audio/wav; codecs=audio/pcm; samplerate=16000'

    # accept
    accept = 'application/json;text/xml'

    # headers
    headers = {
        'Accept': accept,
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-Type' : content_type
    }

    with open(speech, 'rb') as in_file:
        return requests.post(url=stt_eastus_url, data=in_file, headers=headers)


def displayColor(r, g, b): #Accepts RGB values on 255 scale
    GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.

    GPIO.setup(12, GPIO.OUT)  # Set GPIO pin 12 to output mode.
    GPIO.setup(18, GPIO.OUT)  # Set GPIO pin 18 to output mode.
    GPIO.setup(24, GPIO.OUT)

    redpwm = GPIO.PWM(12, 100)   # Initialize PWM on pwmPin 100Hz frequency
    greenpwm = GPIO.PWM(18, 100)   
    bluepwm = GPIO.PWM(24, 100)    

    redpwm.start(0)                      # Start PWM with 0% duty cycle
    greenpwm.start(0)
    bluepwm.start(0)
    
    redpwm.ChangeDutyCycle(r)
    greenpwm.ChangeDutyCycle(g)
    bluepwm.ChangeDutyCycle(b)
    
    
if __name__=="__main__":
    displayColor(100, 100, 100)
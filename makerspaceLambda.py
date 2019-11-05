import json

def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

def on_launch(launch_request, session):
    return get_welcome_response()
    
def get_welcome_response():
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Hello students! I am here to help you find things. Please say, Alexa locate insert item here in g thirty four, for help finding a material." 
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with the same text.
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

def on_session_ended(session_ended_request, session):
    #Called when the user ends the session. Is not called when the skill returns should_end_session=true
    print("on_session_ended requestId=" + session_ended_request['requestId'] +", sessionId=" + session['sessionId'])

def on_intent(intent_request, session):
    print(intent_request['intent'])
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "findItem":
        return findItemResponse(intent_request)
    elif intent_name == "AMAZON.HelpIntent":
        return get_help_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")
        
def get_help_response():
    session_attributes = {}
    card_title = "Help"
    speech_output = "Please say, Alexa find me insert item here, for help finding a material"
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))

def findItemResponse(intent_request):
    session_attributes = {}
    card_title = "Locator"
    speech_output=""
    print(intent_request["intent"]["slots"]["item"])
    specificItem=intent_request["intent"]["slots"]["item"]["value"]
    
    locations={"balsa wood":"Back corner next to workbenches in cardboard container","bluetooth bit":"Littlebits station, left side, sixth row from the top",
           "Saw":"Back corner next to workbenches on the wall","Cardstock":"Under the printer","Quarter twenty tap":"Left workbench, black drawers, fourth row from the top",
           "multimeter":"soldering station, sixth row from the bottom","slide potentiometer":"soldering station, third row from the top",
           "electrical tape":"soldering station, above the oscilliscope","Digital calipers":"Red cart, second drawer from the top","pvc":"Cart four, all rows",
           "Drill bit":"Red cart, fourth drawer from bottom","Pliers":"Red cart, second and third drawers from top","tubing":"Cart three, bottom row",
           "cable":"Cart three, third row from top","gloves":"Cart three, second row from top","foam":"Cart two, bottom row",
           "Six thirty two nuts":"Right work bench, black drawers, fourth row from top","lego":"Cart two, fourth row from top","straw":"Cart two, third row from top",
           "domino":"Cart two, second row from top","Clamps":"Right workbench, left side and underneath","fabric":"Cart two, third row from bottom",
           "mat":"Cart one, bottom row","ratchet":"Red cart, fourth row from top","exacto":"Cart one, second row from bottom","glue":"Cart one, third row from bottom",
           "tape":"Cart one, third row from top","sandpaper":"Red cart, second row from bottom","clip":"Cart one, second row from top",
           "center punch":"Left workbench, black drawers, third row from the top","pen":"Cart one, top row","Quick clamps":"right workbench, right side",
           "dowel rods":"Back corner next to workbenches along the wall"}
    
    speech_output=locations[specificItem]
    reprompt_text=speech_output
    should_end_session=False
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))
        
def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

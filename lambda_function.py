import pandas as pd
#pulls in the excell sheet, separates out the location and synonym dictionary bases
inventory=pd.read_excel(r'C:\Users\ameli\Documents\GitHub\notJarvis\Alexa Skills Inventory.xlsx')
location=pd.DataFrame(inventory, columns=['Item Name','Location in G34'])
synonyms=pd.DataFrame(inventory, columns=['Alternative Names'])
totalRows=len(inventory.axes[0])
l=location.to_dict(orient='list')
s=synonyms.values.tolist()
#creates location and synonym dictionaries
loc={}
syn={}
for i in range(totalRows):
    #converts the single-string "list" of synonyms to an actual list
    specificSyn=''.join(s[i])
    synonymList=specificSyn.split(', ')
    totSyn=len(synonymList)
    #fills loc and syn dicts in lowercase
    loc[l['Item Name'][i].lower()]=l['Location in G34'][i]
    for k in range(totSyn):
        syn[synonymList[k].lower()]=l['Item Name'][i].lower()

import json

#sends imported json to correct event type function
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
    specificItem=specificItem.lower()
    
    speech_output=loc[specificItem]
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

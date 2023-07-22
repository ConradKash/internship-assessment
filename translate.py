from dotenv import load_dotenv
import requests
import os

#This line defines the URL of the Sunbird AI API.

auth_type = 'token'  #@param ["token", "login-credentials"]



def treq(slang,tlang,ttext):  
    url = 'https://sunbird-ai-api-5bq6okiwgq-ew.a.run.app'
    load_dotenv()
    token = os.environ.get('API_KEY')

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
  
            "source_language": slang,
            "target_language": tlang,
            "text": ttext
    }
    response = requests.post(f"{url}/tasks/translate", headers=headers, json=payload)
    translated_text = response.json()["text"]
    return translated_text
#
while True:
  try:
    a = input("Enter 1 to translate texts and any key to close the application\n")    
    if a == '1':
          #@Prompt User to input Target Language
        print("...................................................Translator..........................................................................................")
        slanguage = input("Please input the Source Language(Acholi, Runyankole, Luganda, English):\n")
        print("================================================================\n")
        tlanguage = input("Please input the Target Language(Acholi, Runyankole, Luganda, English):\n")
        print("================================================================\n")        
        transText = input("Input the text you want to translate below 200 Characters.\n")
        print("================================================================\n================================================================")
        print("The translated text is...................\n")

        #This code defines the payload object that will be sent with the HTTP request. 
        #The payload object contains the source language, target language, and text to translate. 
         
        translated_text = treq(slanguage, tlanguage, transText)
         
                
        print("Translated text: ", translated_text)
    else:
      print("Thank you") 
      break
  except ValueError:5
  print("Enter correct texts for translation")
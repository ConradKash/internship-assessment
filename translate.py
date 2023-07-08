import requests
#This line defines the URL of the Sunbird AI API.
url = 'https://sunbird-ai-api-5bq6okiwgq-ew.a.run.app'
auth_type = 'token'  #@param ["token", "login-credentials"]
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJJbnRlcm5zaGlwcyIsImV4cCI6NDg0MTQ4NzEyMn0.-j3rdudJ9pXEm3-456LLiDPun5SwIm5sw-RoNvgDwfk'

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
def treq(slang,tlang,ttext):  
    payload = {
            "source_language": slang,
            "target_language": tlang,
            "text": ttext
    }
    return payload
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
         
        if slanguage != "English" and tlanguage != "English":    
            response = requests.post(f"{url}/tasks/translate", headers=headers, json=treq(slanguage, "English", transText))
           
            transtext1 = response.json()["text"]
            
            response = requests.post(f"{url}/tasks/translate", headers=headers, json=treq("English", tlanguage, transtext1))
        else:
          response = requests.post(f"{url}/tasks/translate", headers=headers, json=treq(slanguage, tlanguage, transText))

        if response.status_code == 200:
          translated_text = response.json()["text"]
          print("Translated text: ", translated_text)
        else:
          print("Error: ", response.status_code, response.text)
    else:
      print("Thank you") 
      break
  except ValueError:
    print("Enter correct texts for translation")
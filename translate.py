#This line imports the requests library, which is used to make HTTP requests
import requests
#This line defines the URL of the Sunbird AI API.
url = 'https://sunbird-ai-api-5bq6okiwgq-ew.a.run.app'

#@title Authentication
auth_type = 'token'  #@param ["token", "login-credentials"]
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJJbnRlcm5zaGlwcyIsImV4cCI6NDg0MTQ4NzEyMn0.-j3rdudJ9pXEm3-456LLiDPun5SwIm5sw-RoNvgDwfk'
#This line defines the headers that will be used for the HTTP requests. 
#The Authorization header specifies the token that will be used to authenticate the requests.
#The Content-Type header specifies that the requests will be sending JSON data.
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
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
        payload = {
            "source_language": slanguage,
            "target_language": tlanguage,
            "text": transText
        }

        #The requests.post() function returns a Response object. 
        #The code checks the status code of the Response object
        response = requests.post(f"{url}/tasks/translate", headers=headers, json=payload)

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

  
  
      
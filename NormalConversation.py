from SGPMain import takeCommand,speak,VAName
import openai
import os
openai.api_key = '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'

# This function interct with chatGPT and generat answer  based on user input
def chat_with_gpt(query):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
          {
            "role": "user",
            "content": query
          }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content.strip()

def Conversetion(query):
    if query in ['bye', 'exit', f'{VAName} exit',f'bye {VAName}'] :
        answer = chat_with_gpt(query)
        print(f"{VAName} : ",answer)
        speak(answer)
        try:
            os.system(f'taskkill /f /im python.exe')
        except Exception as e:
            print(f'{VAName} : Somthing is wrong')
            speak('Somthig is wrong')
            print(e)
            exit()

    elif query in ['who are you','who r u','hu r u']:
        print(f'{VAName} : I am a Virtual Assistant developed by AI Developers\n')
        speak("I am a Virtual Assistant developed by AI Developers")
        
    else:
        answer = chat_with_gpt(query)
        print(f"{VAName} :",answer)
        speak(answer)
     
if __name__ == '__main__':

    query = takeCommand().lower()
    Conversetion(query)



from SGPMain import takeCommand,speak,VAName
import webbrowser
import pywhatkit
import wikipedia

#=====================================================================================================================
def searchGoogle(query):
    if 'open google' in query:
        print(f"{VAName} : Opening google")
        speak("Opening google")
        webbrowser.open('http://www.google.com')

    elif 'search on google' in query:
        query = query.replace('search on google','')
        query = query = query.replace(f'{VAName}','')
        print(f"{VAName} : serching")
        speak('serching on google')
        pywhatkit.search(query)
        print(f'{VAName} : This is what i found on google')
        speak("this is what i found on google")

#=====================================================================================================================
def searchYoutube(query):
    if 'open  youtube' in query:
        print(f"{VAName} : Opening youtube")
        speak("Opening youtube")
        webbrowser.open('http://www.youtube.com')

    elif 'search on youtube' in query:
        query = query.replace('search on youtube','')
        query = query.replace(f'{VAName}','')
        print(f"{VAName} : serching")
        speak('serching on youtube')
        webpath = 'https://www.youtube.com/results?search_query='+ query
        webbrowser.open(webpath)
        print(f'{VAName} : This is what i found on youtube')
        speak("this is what i found on youtube")
#=====================================================================================================================
def searchWikipedia(query):
    if 'open wikipedia' in query:
        print(f'{VAName} : Opening  Wikipedia')
        speak('Opening Wikipedia')
        webbrowser.open("https:/en.wikipedia.org/wiki/Main_Page")

    elif 'search on wikipedia' in query:
        print(f"{VAName} : Serching wikipedia...")
        query = query.replace("search on wikipedia","")
        speak('serching on wikipedia')
        webpath = 'https://en.wikipedia.org/wiki/' + query
        try:
            webbrowser.open(webpath)
            results = wikipedia.summary(query,2)
            print(f'{VAName} : According to wikipedia ' + results)
            speak(f"According to wikipedia {results}")
        except Exception as e :
            print(f'{VAName} : Sorry , I cannot find the information you are looking for ')
            speak("somthing want's wrong")
            print('Error : '+e)

if __name__ == "__main__":
    query = takeCommand().lower()
    searchGoogle(query)
    searchYoutube(query)
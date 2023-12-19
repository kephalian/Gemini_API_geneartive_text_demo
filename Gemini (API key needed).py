import PySimpleGUI as sg
import requests
import pyperclip

def generate_content(api_key, text):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    headers = {'Content-Type': 'application/json'}
    payload = {
        'contents': [{'parts': [{'text': text}]}]
    }
    params = {'key': api_key}

    response = requests.post(url, headers=headers, json=payload, params=params)
    return response.json()

def main():
    sg.theme("LightBlue2")

    layout = [
        [sg.Text("Enter text for the story:"),],
        [ sg.InputText(default_text="This the story of a mammoth", key='input')],
        [sg.Button("Generate Story"),sg.Button("Copy", key='Cpy_'),sg.Button("Exit")],
        [sg.Multiline('', key='output', size=(80, 30))]
    ]

    window = sg.Window("Magic Backpack Story Generator", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        elif event == "Generate Story":
            input_text = values['input']
            api_key = ''  # Replace with your actual API key
            if api_key=='': 
                    sg.popup("Please add your Google AI Studio API key in Line 35 before executing!! \n Get your key at\n https://makersuite.google.com/app/apikey")
                    continue
            result = generate_content(api_key, input_text)

            story_text = result['candidates'][0]['content']['parts'][0]['text']
            #.get('contents', [])[0].get('parts', [])[0].get('text', '')
            window['output'].update(story_text)
        elif event == 'Cpy_':
            text_to_copy=values['output']
            if text_to_copy!=None:pyperclip.copy(text_to_copy)

    window.close()

if __name__ == "__main__":
    main()

    



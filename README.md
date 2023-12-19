# Gemini_API_geneartive_text_demo
PySimpleGUI library to create a basic graphical user interface (GUI) for a demo of Google Generative text, using Goole Gemini API Key

[Python File here](https://github.com/kephalian/Gemini_API_geneartive_text_demo/blob/main/Gemini%20(API%20key%20needed).py")

*Description created by ChatGPT*
The provided Python script utilizes the PySimpleGUI library to create a basic graphical user interface (GUI) for a Magic Backpack Story Generator. Here's a breakdown of the code:

1. **Imports:**
   - `PySimpleGUI`: A Python library for creating simple and easy-to-use graphical user interfaces.
   - `requests`: A Python library for making HTTP requests, used in this script to communicate with the Google Cloud Natural Language API.

2. **Function `generate_content(api_key, text)`:**
   - Takes an API key and input text as parameters.
   - Constructs a request payload in JSON format with the provided input text.
   - Sends a POST request to the Google Cloud Natural Language API endpoint for content generation.
   - Returns the JSON response from the API.

3. **Function `main()`:**
   - Sets the PySimpleGUI theme to "LightBlue2."
   - Defines the layout of the GUI using a list of PySimpleGUI elements:
     - Input field for entering text.
     - "Generate Story" and "Exit" buttons.
     - Multiline text box for displaying the generated story.
   - Creates a PySimpleGUI window with the specified layout and title ("Magic Backpack Story Generator").

4. **GUI Event Loop:**
   - Enters into a while loop to handle events and user interactions in the GUI.
   - Checks for the window close event or the "Exit" button press to exit the loop and close the window.
   - If the "Generate Story" button is pressed, retrieves the input text from the GUI, calls the `generate_content` function with the API key and input text, and updates the GUI's multiline text box with the generated story.

5. **Execution:**
   - Checks if the script is executed directly (not imported as a module).
   - Calls the `main()` function to run the GUI.

6. **Note:**
   - The API key ("YOUR_API_KEY") needs to be replaced with an actual Google Cloud Natural Language API key for the script to work correctly.
   - The script creates a simple interface allowing users to input text, generate a story using the Google Cloud Natural Language API, and view the generated story in a multiline text box within the GUI.

# Babagaboosh
This is a Simple app that lets you have a verbal conversation with OpenAi's GPT 4.
Written originally by the YouTube creator "DougDoug", Edited and optimized to the way it currently is by Bryson Bayer. 
Feel free to use this for whatever you want! Credit is appreciated but not required, and any credit attributed primarily goes to DougDoug.

If you would like a video explanation of this project, DougDoug made a video covering the basics here: https://www.youtube.com/watch?v=vYE1rkIMj9w

## SETUP: 

!!!!EXTREMELY IMPORTANT!!!!
    - At the top of each character file, please replace the voice name where it says "ELEVENLABS_VOICE = "INSERT_NAME"" of each character file with the name of a voice in your VoiceLab on ElevenLabs.com, ALSO replace the file path where it says sys.path.append("C:YOUR\PATH\TO\Babagaboosh") with your path to Babagaboosh (The name of this folder with all the files for the app). Not doing so will render the file broken until replaced. Make sure your path is formatted exactly like this (  'c:\\Users\\Name\\Documents\\Babagaboosh'  ). This includes the apostrophies and the double back slashes. Information on how to get your file path is below. ALSO, make sure the folder that all these files are kept in is called "Babagaboosh" in order to run properly.


1) This was written in Python 3.9.2. Install page here: https://www.python.org/downloads/release/python-392/. Either this, or download it via the Microsoft Store and it should set automatically

2) Run `pip install -r requirements.txt` in your Command Prompt/Terminal/Powershell to install all modules.

To do this, go to the search bar at the bottom of the screen for Windows, type in "Powershell" and click on it. Paste into Powershell (  cd "C:YOUR\PATH\TO\Babagaboosh"  ) See the 2nd part of SETUP 7 for information how to do this, but instead of the file, right click on the folder "Babagaboosh" wherever you store it. Once you do this properly, and you already have Python installed properly, you can run the command `pip install -r requirements.txt' in Powershell and exit out of it

3) This uses the Microsoft Azure TTS, Elevenlabs, and OpenAi services. You'll need to set up an account with these services and generate an API key from them. Then add these keys as windows environment variables named AZURE_TTS_KEY, AZURE_TTS_REGION, ELEVENLABS_API_KEY, and OPENAI_API_KEY respectively. REPLACE ALL OF THESE IN EACH FILE. The files can be opened up in anything that can view text (including notepad), and look for the respected variables above near the top of each of the following files: 
    - azure_speech_to_text.py   (AZURE_TTS_KEY, AZURE_TTS_REGION)
    - eleven_labs.py    (ELEVENLABS_API_KEY)
    - openai_chat.py    (OPENAI_API_KEY)

MINIMUM COST TO RUN THIS PROGRAM: 
    - $0.00 for Eleven Labs
    - $1.00 for OpenAI
    - $0.00 for Azure Text-to-Speech

RECCOMMENDED COST TO RUN THIS PROGRAM (Makes it more fun and worryless):
    - $11.00 for Eleven Labs (first month only, $22 per month after)
    - $10.00 for OpenAI (Gives you plenty to start without worrying about it)
    - $0.00 for Azure Text-to-Speech (Haven't run into having to pay for it yet, and I've used a ton. Also, typing text bypasses the need for Azure Text-to-Speech altogether as long as you comment out the code properly using "#" to comment)

4) This app uses the GPT-4 model from OpenAi. As of this writing (April 18th, 2024), you need to pay $1 to OpenAi in order to get access to the GPT-4 model API. So after setting up your account with OpenAi, you will need to pay for at least $1 in credits so that your account is given the permission to use the GPT-4 model when running my app. See here: https://help.openai.com/en/articles/7102672-how-can-i-access-gpt-4

5) Optionally, you can use OBS Websockets and an OBS plugin to make images move while talking. First open up OBS. Make sure you're running version 28.X or later. Click Tools, then WebSocket Server Settings. Make sure "Enable WebSocket server" is checked. Then set Server Port to '4455' and set the Server Password to 'TwitchChat9'. If you use a different Server Port or Server Password in your OBS, just make sure you update the websockets_auth.py file accordingly. Next install the Move OBS plugin: https://obsproject.com/forum/resources/move.913/ Now you can use this plugin to add a filter to an audio source that will change an image's transform based on the audio waveform. For example, I have this filter on a specific audio track that will move Pajama Sam's image whenever text-to-speech audio is playing in that audio track. Note that OBS must be open when you're running this code, otherwise OBS WebSockets won't be able to connect. If you don't need the images to move while talking, you can just delete the OBS portions of the code.

IMPORTANT: OBS functions and plugins are currently turned off / commented out, thereby making all OBS functionality inert unless turned back on

6) Elevenlabs is the service I use for Ai voices. Once you've made an Ai voice on the Elevenlabs website, open up chatgpt_character.py and replace the ELEVENLABS_VOICE variable with the name of your Ai voice along with any other information you would like to change.

7) If you want to make this even easier for yourself to access on a Windows computer, right-click on your desktop and select "New", then "Shortcut". From there, paste this (  C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File "C:YOUR\PATH\TO\Character_AI_Runner.ps1"  )
into the textfield WHILE replacing the address with the address to the 'Character_AI_Runner.ps1' file (details below)

To get the file path, simply open up your File Explorer, navigate to where you store Babagaboosh, open the folder, then look for "Character_AI_Runner.ps1" file. Once you find it, select it by clicking once, right click so you see options, then click "Copy as Path". replace "C:YOUR\PATH\TO\Character_AI_Runner.ps1" with this path you just copied, and make sure there is only one set of "" in front and behind it (so it doesnt look like this: ""C:YOUR\PATH\TO\Character_AI_Runner.ps1"")

Finally, go to Character_AI_Runner.ps1 and double click to open it in notepad, and paste in the path to Babagaboosh in the respective area, and save the file

## Using the App

1) Run `start_menu.py'. If you want to make this even easier for yourself on a Windows computer, see above in the SETUP for a way to use an executable.

2) Type in the name of any character within the "characters" folder, making sure it is formatted as such - EX for selecting Pajama Sam: type in "Pajama Sam" to launch "Pajama_Sam.py"

3) Wait for it to load (this could take a minute)

4) Type in either "speak" for Speech-to-Text or "text" to type in your questions and comments, depending on how you wish choose to interact with this character

5) Once it's running, press F4 to start the conversation, and either Azure Speech-to-text will listen to your microphone and transcribe it into text or a prompt to type will appear.

6) IF you use Speech-to-Text, Once you're done talking, press P, then the code will send all of the recorded text to the Ai. Note that you should wait a second or two after you're done talking for the RECOGNIZED before pressing P so that Azure has enough time to process all of the audio.

7) IF using text, press "Enter" when finished, and your text will be uploaded automatically.

8) Wait a few seconds for OpenAi to generate a response and for Elevenlabs to turn that response into audio. Once it's done playing the response, you can press F4 to start the loop again and continue the conversation.

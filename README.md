# TSTTUWACA
Telegram speech to text using WhisperAPI created by amir, (aka "TSTTUWACA") is a smooth and gentle telegram bot that converts your audio files to raw text for easier understanding.<br>
...<br>
<br>
<br>
Also the main bot running with this code has the best name ever.<br>

![phito](https://github.com/user-attachments/assets/b333f06f-b121-48a2-9a02-04914d7d09e1)
<br>
# Usage
Free forever (i hope), no request limits (i also hope).<br>
Add the bot to your chats or just use it directly, https://t.me/ExplosiveFartBot it is!<br>
<br>
Additionally, the system got implemented in the state-of-the-art (yes im bragging) https://t.me/cuhybot project too.
<br>
<br>
# Installation & Setup
* Step 1: Downloading the project<br>
  * Option 1: Paste `git clone https://github.com/amirgame197/TSTTUWACA` to automatically download the files. you may need to install `git`.<br>
  * Option 2: Manually download the project files anywhere you want.<br>
  <br>
* Step 2: Install the required packages: Telethon, OpenAI, FFMPEG
  * If you dont have these packages (except ffmpeg), you can install them using `pip install telethon openai`. Additionally, you can install FFMPEG using `apt install ffmpeg` (or if you are not debian based, follow the instructions for your own OS).
  <br>
* Step 3: Configuration
  * Open `config.py`. There are some changes you need to apply.
  * The first line is your telegram bot's token. Paste your token there
  * Second and third lines are your `app_id` and `app_hash`, Fourth line is your OpenAi's `api_key`. You need these to setup a proper connection to telegram and OpenAi Servers.
    * You can obtain the first two from `https://my.telegram.org`: Create an application with any info you like, Copy your app id and hash then paste them to `config.py`.
    * The third one is obtainable from your account in `https://platform.openai.com`: Go to the API Keys page in your account and create one with an optional name. You then copy it and paste it to `config.py`.
    * These three variables are connected to your telegram and openai account. You must keep them confidential otherwise if they get exposed somewhere then some dude can use them to do nasty stuff and its your account in danger, not his.
  <br>
* Step 4: Activating
  * To run the code, simply run `python TSTTUWACA.py` and wait for it to connect. Should take a bit of time in its first boot because its generating session files
  <br>
* Step 5: Enjoy
  * The results are by far the best ones i've seen (Not for persian though, i think google has a better support for it).
  * Plus, the service you are using from OpenAI is not free. You need to pay them so thats a downside (Although you can use Whisper locally, You just need a good setup).
  <br>
  <br>
# The Story
Third Episode, thank god its not a triple episode series.<br>
Okay this one is not a big one. Infact, there not bunch to tell. In the past years, i always wanted a system that can automatically convert voices to text so i dont have to plug my headsets in just to hear my freind yelling at me.<br>
Well, telegram added a feature that converts the voices to texts automatically but there is something wrong with it: Its a premium only feature and i have no cash to buy that. so sad, i cannot react an emoji of gay black men twerking to my friend's messages :(<br>
But just days ago, one of my friends asked me if i know any speech to text system in telegram that is not a mess and is free. I searched but found nothing, then remembered i always wanted such thing myself. I felt lazy as hell to actually create a telegram bot again after this many months, so i asked him i may be able to create something like that myself, do you really need it?<br>
He said: I guess.<br>
Then something got locked down in my mind and made me like man there are atleast two guys asking for it, why not just start making it?<br>
Exactly 3 hours later, it was done and working pretty well.<br>
<br>
<br>
Also i spent 15 minutes thinking about the bot's name and username, my hard work came out paying.

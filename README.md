# UndeadBot v0.1
This is a bot for the game of the plant. You choose which plants you want to monitor and how much you are willing to pay.
When it found a plant with your selected parameters, will show up the plant's buy page.

![Test image](https://github.com/Tomanji/UndeadBot/blob/main/test_bot.png)

## Setup:
1. Download the code in zip format pressing the Green button above. Unzip it where you want.

2. Install Python 3 Windows installer (64-bit):
https://www.python.org/downloads/

3. Open Power Shell in the code directory 
(Shift + Right Click -> Open PowerShell)

4. Execute this command:

		pip install -r requeriments.dat

5. Get you Bearer Token:

![Image of Yaktocat](https://github.com/Tomanji/UndeadBot/blob/main/bearer_token.png)

6. Copy and save your Bearer Token in token.txt


## How to use

 Open PowerShell in the main directory and write:
	
	python bot.py

 When the bot found any plant with your parameters,
the bot will open the browser in the plant buy page. 
You will press "Buy now" to confirm the purchase.

## How to config

1. From the "imgcodes" folder, choose which plant do you want to monitorize.

![Image of codes](https://github.com/Tomanji/UndeadBot/blob/main/img_codes.png)

2. In "config.txt" write all the img codes which you want in this format:

		img code1, le minimum, price maximum
		img code2, le minimum, price maximum
		img code3, le minimum, price maximum
		...

And save the file.

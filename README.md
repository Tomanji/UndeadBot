# UndeadBot v0.1
## SETUP:
1. Install Python 3 Windows installer (64-bit):
https://www.python.org/downloads/

2. Open Power Shell in the main directory 
(Shift + Right Click -> Open PowerShell)

3. Execute this command:

		pip install -r requeriments.dat

4. Get you Bearer Token:

![Image of Yaktocat](https://github.com/Tomanji/UndeadBot/blob/main/bearer_token.png)

5. Copy and save your Bearer Token in token.txt


## HOW TO USE

 Open PowerShell in the main directory and write:
	
	python bot.py

 When the bot found any plant with your parameters,
the bot will open the browser in the plant buy page. 
You will press "Buy now" to confirm the purchase.

## HOW TO CONFIG 

1. From the "imgcodes" folder, choose which plant do you want to monitorize.

![Image of codes](https://github.com/Tomanji/UndeadBot/blob/main/img_codes.png)

2. In "config.txt" write all the img codes which you want in this format:

		img code1, le minimum, price maximum
		img code2, le minimum, price maximum
		img code3, le minimum, price maximum
		...

And save the file.

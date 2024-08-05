# Flash_Card_App 
Flash Card App built in Python

This Python program can take any comma separated list that is formatted properly. It will use line one of the csv files as the card header. Example: Spanish,English or Word,Definition. 

The current content is based on the first chapter of the book Aventuras Sixth Edition, which is and/or was a Spanish 1 college course book. The video lecture explains the card’s content.

Youtube; Aventuras Ch1 Video Lecture:
https://www.youtube.com/watch?v=p5IAoQrX2DY&list=PL8_gqHP2hy87FQheWfkMaed7gZMOpAlHb&index=16

There are four named folders with different .csv files, all with matching Learn.csv names. Just delete the current Learn.csv and copy the one you want to learn into the flash_card_app folder. This is so you don’t have to change the names in the app, you simply copy the one you want to learn and delete the current file, then paste it into the main folder. Chapter one is the default Learn.csv currently highlighted.


![image](https://github.com/user-attachments/assets/04d1aaec-98c5-4d57-8c4d-411a03248586)



I was looking for a simple flash card app on github but kept finding the same broken copies, so me and chatgipity fixed one and changed the code to the way I wanted it. The “Next” button moves to the next card, the “Flip” button flips to the English side and back to the Spanish side as many times as you want. “Random Off” follows the same order as the lecture video. “Random On” creates a random list and iterates through each card once and at the end it resets and creates a new random list. If you want to edit out the ones you know simply edit the current Learn.csv and delete it when you’re done and keep the original files in their folders to copy again and again or make a new folder. If you mess it up just come back here and recopy everything, no worries. Let me know if you need any help or find any errors, I am learning so I will gladly help or fix any issues. Also, I don’t know Spanish the content is based off the book for the sake of studying and currently has no special characters. 

![image](https://github.com/user-attachments/assets/f1c12384-950b-46de-819d-e92cbbd7bc4b)


Just to clarify, this flash card Python program takes the first line of the Learn.csv file and uses it to populate the card title for both sides. So, if you need to study statistics definitions or any other language/content as long as it is formatted correctly, line one of the csv file is what the card header will show. Here is an example:

![image](https://github.com/user-attachments/assets/54a0594a-b968-488d-aeec-7523bb1c2bc9)



Changed line one of the Learn.csv

![image](https://github.com/user-attachments/assets/4e08ef59-bb43-436c-8357-81e2b349341c)


Example with edited header:

![image](https://github.com/user-attachments/assets/8d53510d-3b6e-4c90-892c-c61335f97456)


Obviously hola is not a statistics word but you can make ANY comma separated list you wish to use. Just make sure you create a new folder and only have one Learn.csv in the main folder (the FLASH_CARD_APP folder) so you can have a massive library of different folders all with Learn.csv files in them. I would suggest creating your comma separated list in Word or some other text editor, then create a new folder in the FLASH_CARD_APP folder, then create a new Learn.csv and paste in your list. Most programers will understand, but again if you are new and need help or find an issue let me know.

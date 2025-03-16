HOW TO USE NEBULA EXPLOITER :

open linux :

git clone https://github.com/sudoxabit/nebula-strike.git

cd nebula-strike

pip3 install -r requirements.txt 

python3 NebulaStrike.py

now option 1 skip that thats under dev :

how to use option2 , 3 and 4 :

for using option 2 we have to create a target list in a .txt file in the following format :
https://www.example.com/wp-login.php#admin@pass >> admin will be used as username and pass as password 

for using option 3 : wp register exploit " it basically checks is registration is enabled on wordpress then it registers a user on the wordpress using the username and email we own for testing this check the code and change nrnr551a@gmail.com to your own mail " To use this option we have to provide this a list of wordpress websites in simple url format in a txt file and then it will start to check .
format to provide urls is :
https://www.example.com/


for using option 4 : sqli detector 
This option will help to detect potential error based sql injection to use this feature we have to create a txt file which contains a list of urls along parameters we want to test .
example create a sqli.txt which will contain urls in this format :
https://www.example.com/page.php?id=12 
id parameter will be tested by the tool if it declares a url as vulnerable then you can use sqlmap to dump the database :

optional :
sqlmap -u url --dbs --tables --columns --dump --batch 

Thank you 





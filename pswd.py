import random

#This function generate the password.
def generatePassword(pwlength):
	#Initialise all used character in a string variable.
	alphabet = "abcdefghijklmnopqrstuvwxyz,./;'[]+_)(*&^%$#@!~`1234567890-=ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	#A variable to temporarely store individual password to string.
	password = "";

	#Loop trough the amount of password required by the user.
	for j in range(pwlength):
		#Select a symbol randomply in the alphavet string.
		next_letter_index = random.randrange(len(alphabet));
		#Add the selected character to the password string
		password = password + alphabet[next_letter_index];
	return password

#Main programem funtion
def main():
	#Ask the user to input the amount of passwords to generate.
	numPasswords = int(input("How many passwords do you want to generate? "));

	#Set a limits to the amount of passwords that can be generated.
	if numPasswords<1:
		print("Minimum amount of password is 1");
		numPasswords=1;
	if numPasswords>100:
		print("Maximum amount of password is 100");
		numPasswords=100;

	#Set a defautl password length.
	passwordLengths = 5;

	#Inform user of the defaut length setting.
	print("Enter 0 for the default 16 character password length");

	#Ask the user to input the lenght of each password
	passwordLengths = int(input("Enter the length of Password "));

	#Set limit to the lenght of each password
	if passwordLengths==0:
    		print("Default length of password is 16");
    		length = 16;
	if passwordLengths<5:
		print("Minimum length of password is 5");
		passwordLengths = 5;

	if passwordLengths>200:
		print("Maximum length of password is 200");
		passwordLengths = 200;
	
	#Keep the user inform of the progress
	print("Generating " +str(numPasswords)+" passwords of lenght "+str(passwordLengths));
	
	#Generate all password and insert them in the Password array list.
	passwords=[];
	for i in range(numPasswords):
		passwords.append(str(generatePassword(passwordLengths)));

 	#If the array contain multiple password loop trough the list.
	if numPasswords>1:
		for i in range(numPasswords):
			#Display all password in the Password list to the user.
			print("Password n."+str(i+1)+" = " + passwords[i]);
	else:
		#Display the password from the Password list to the user.
		print ("Password"+" = " + passwords[0]);
#Start programme
main();

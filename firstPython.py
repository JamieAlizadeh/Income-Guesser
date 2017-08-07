import os;
os.chdir('C:\\Users\\Jamie Alizadeh\\CF');
file = open('adult.data.txt', 'r');
str = file.read();
#print (str);Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> input_file = open('adult.data.txt','r')
output_file = open('output.txt','w')
 
for lines in range(500):
    line = input_file.readline()
    output_file.write(line)
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> 4 + 4

import os;
os.chdir('C:\\Users\\Jamie Alizadeh\\CF');
file = open('adult.data.txt', 'r');
str = file.read();

class Adult:

	def __init__(self, name, age, workclass, fnlwgt, education, education_num, marital_status, occupation, relationship, race, sex, capital_gain, capital_loss, hours_per_week, native_country):
		self.name = name;	

curAtt = "name";
temp = "";
y = 0;
people = [];
for x in range (0, len(str) - 1):
	if str[x] != ',':
		temp+=str[x];
	#	setattr(Adult, curAtt,
	#people[y]
	elif curAtt == 'name':
		setattr(Adult, curAtt, temp);
		temp = "";
		curAtt = 'age'
	elif curAtt == 'age':
		setattr(Adult, curAtt, temp);
		temp = "";
		curAtt = 'workclass'
	elif curAtt == 'workclass':
		setattr(Adult, curAtt, temp);
		temp = "";
		curAtt = 'fnlwgt'
	elif curAtt == 'fnlwgt':
		setattr(Adult, curAtt, temp);
		temp = "";
		curAtt = 'education'
	elif curAtt == 'education':
		setattr(Adult, curAtt, temp);
		temp = "";
		curAtt = 'education_num'
	elif curAtt == 'education_num':
		setattr(Adult, curAtt, temp);
		temp = "";
		curAtt = 'marital_status'
	elif curAtt == 'marital_status':
		setattr(Adult, curAtt, temp);
		temp = "";
		curAtt = 'occupation'
	elif curAtt == 'occupation':
		setattr(Adult, curAtt, temp);
		temp = "";
		curAtt = 'relationship'
	elif curAtt == 'relationship':
		setattr(Adult, curAtt, temp);
		temp = "";
		curAtt = 'race'
	elif curAtt == 'race':
		setattr(Adult, curAtt, temp);
		temp = "";
		curAtt = 'sex'
	elif curAtt == 'sex':
		setattr(Adult, curAtt, temp);
		temp = "";
		curAtt = 'capital_gain'
	elif curAtt == 'capital_gain':
		setattr(Adult, curAtt, temp);
		temp = "";
		curAtt = 'capital_loss'
	elif curAtt == 'capital_loss':
		setattr(Adult, curAtt, temp);
		temp = "";
		curAtt = 'hours_per_week'
	elif curAtt == 'hours_per_week':
		setattr(Adult, curAtt, temp);
		temp = "";
		curAtt = 'native_country'
	else: 
		setattr(Adult, curAtt, temp);
		temp = "";
		curAtt == 'name';
		#new object
		people.append(Adult('','','','','','','','','','','','','','',''));
		y += 1;

print (people[24].education);

import os;
import logging;
logging.basicConfig(filename='myPythonLogger.log',level=logging.DEBUG)
os.chdir('C:\\Users\\Jamie Alizadeh\\CF');
file = open('adult.data.txt', 'r');
str = file.read();

class Adult:

	def __init__(self, name, age, workclass, fnlwgt, education, education_num, marital_status, occupation, relationship, race, sex, capital_gain, capital_loss, hours_per_week, native_country):
		self.name = name;	

curAtt = "age";
temp = "";
y = 0;
people = [];
people.append(Adult('','','','','','','','','','','','','','',''));
for x in range (0, len(str) - 1):
	if str[x] != ',':
		temp += str[x];
	elif curAtt == 'age':
		setattr(people[y], curAtt, temp);
		temp = "";
		curAtt = 'workclass'
	elif curAtt == 'workclass':
		setattr(people[y], curAtt, temp);
		temp = "";
		curAtt = 'fnlwgt'
	elif curAtt == 'fnlwgt':
		setattr(people[y], curAtt, temp);
		temp = "";
		curAtt = 'education'
	elif curAtt == 'education':
		setattr(people[y], curAtt, temp);
		temp = "";
		curAtt = 'education_num'
	elif curAtt == 'education_num':
		setattr(people[y], curAtt, temp);
		temp = "";
		curAtt = 'marital_status'
	elif curAtt == 'marital_status':
		setattr(people[y], curAtt, temp);
		temp = "";
		curAtt = 'occupation'
	elif curAtt == 'occupation':
		setattr(people[y], curAtt, temp);
		temp = "";
		curAtt = 'relationship'
	elif curAtt == 'relationship':
		setattr(people[y], curAtt, temp);
		temp = "";
		curAtt = 'race'
	elif curAtt == 'race':
		setattr(people[y], curAtt, temp);
		temp = "";
		curAtt = 'sex'
	elif curAtt == 'sex':
		setattr(people[y], curAtt, temp);
		temp = "";
		curAtt = 'capital_gain'
	elif curAtt == 'capital_gain':
		setattr(people[y], curAtt, temp);
		temp = "";
		curAtt = 'capital_loss'
	elif curAtt == 'capital_loss':
		setattr(people[y], curAtt, temp);
		temp = "";
		curAtt = 'hours_per_week'
	elif curAtt == 'hours_per_week':
		setattr(people[y], curAtt, temp);
		temp = "";
		curAtt = 'native_country'
	else: 
		setattr(people[y], curAtt, temp);
		temp = "";
		curAtt = 'age';
		#new object
		people.append(Adult('','','','','','','','','','','','','','',''));
		y += 1;
#for i in range (0, 30):
#	print (people[i].education);

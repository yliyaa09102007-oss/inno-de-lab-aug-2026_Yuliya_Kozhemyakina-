raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "

#splitting, creating a list
split_user_record = raw_user_record.split(';')

#creating a new list for stripped strings
strip_user_record = []

#adding stripped strings to a new list
for i in range(0, len(split_user_record)):
    strip_user_record.append(split_user_record[i].strip())

#dividing a list into different strings
PersonID = strip_user_record[0]
FullName = strip_user_record[1]
City = strip_user_record[2]
Status = strip_user_record[3]

#normalizing every string
PersonID = "UID-" + PersonID

FullName = FullName.split('_')
FirstName = FullName[0].title()
LastName = FullName[1].title()
FullName = FirstName + ' ' + LastName
#also could've kept firstname and second name independently

City = City.upper()

Status = Status.lower()

normalized_user_record = (PersonID + ' | ' + FullName + ' | ' + City +
' | ' + Status)
print(f"Нормализованная запись: {normalized_user_record}")
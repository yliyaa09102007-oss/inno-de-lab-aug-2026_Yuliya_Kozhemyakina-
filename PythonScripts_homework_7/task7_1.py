raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "

#splitting, creating a list
split_user_record = raw_user_record.split(';')

#creating a new list for stripped strings
strip_user_record = []

#adding stripped strings to a new list
for i in range(0, len(split_user_record)):
    strip_user_record.append(split_user_record[i].strip())

#dividing a list into different strings

#normalizing every string
strip_user_record[0] = f"UID-{strip_user_record[0]}"

strip_user_record[1] = strip_user_record[1].split('_')
strip_user_record[1] = (strip_user_record[1][0] + ' ' + strip_user_record[1][1]).title()

strip_user_record[2] = strip_user_record[2].upper()

strip_user_record[3] = strip_user_record[3].lower()

normalized_user_record = " | ".join(strip_user_record)
print(f"Нормализованная запись: {normalized_user_record}")
class DataDNI:
    position = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    letter = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
    letter_asign = dict(zip(position,letter))
    table_length = len(letter_asign)
    letters_forbidden = ['O','Ñ', 'I', 'U'] 

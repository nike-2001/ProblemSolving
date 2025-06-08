def runLengthEncoding(string):
    encoding = ""
    count = 1
    repeat  = 1
    for char in range(len(string)):  
        if char+1 < len(string) and string[char] == string[char+1] :
            count += 1
        else:
            diff = count % 9
            repeat = (count - diff) // 9
           
            encoding += (("9" + string[char]) * repeat) 
            if diff > 0:
                encoding += str(diff) + string[char]
            count = 1

    return encoding


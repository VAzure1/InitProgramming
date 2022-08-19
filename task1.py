choose_language =input("choose lang> ")


def number_converter(number):
    numbers = {
            0:"zero",1:"one",2:"two",3:"three",4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'Elevem',\
            12:'tweleve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',\
            20:'twenty',30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'
            }
    if number < 20:
        return numbers[number]
    elif number < 100:
        if number % 10 == 0:
            return numbers[number]
        else:
            return numbers[number - (number % 10)] + f" {numbers[number % 10]}"
    elif number < 1000:
        if number % 100 == 0:
            return numbers[number // 100] + " hundred"
        else:
            return numbers[number // 100] + " hundred" + f" {number_converter(number % 100)}"
    elif number < 1000000:
        if number % 1000 == 0:
            return number_converter(number // 1000) + "thousand"
        else:
            return number_converter(number // 1000) + " thousand" + f" {number_converter(number % 1000)}"
    elif number < 1000000000:
        if number % 1000000 == 0:
            return number_converter(number // 1000000) + " million"
        else:
            return number_converter(number // 1000000) + " million" + f" {number_converter(number % 1000000)}"


if choose_language =="amh":
    input = input("Insert any number please: ")
    try:
        num = int(input)
        print(number_converter(num))
    except:
        print("Invalid input please try again!! ")

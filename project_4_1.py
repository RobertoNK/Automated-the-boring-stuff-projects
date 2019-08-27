

spam = ["apples", "bananas", "tofu", "cats"]

def adding_commas(a_list):

    count = 0
    for item in a_list:
        
        if count < len(a_list)-1:
            
            count = count + 1
            print (item +", ", end = '')
            
        else:

            print(", and "+ item)

adding_commas(spam)
            
        


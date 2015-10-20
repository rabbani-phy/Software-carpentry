
# coding: utf-8

# In[1]:

#here we r going to pla the program

#zodiacSetup will do all the opening, loading and closing of files/data
#it will return zodiac list
def zodiacSetup():
    #open the zodiac description
    ZodiacText = open('zodiacDescriptions.txt','r')
  
    #read the file. We are going to make a list with each line of the file
    #as a list item
    ZodiaclistTemp = []
    for animal in ZodiacText:
        if animal != '\n':
            ZodiaclistTemp.append(animal)

    #close the file. although its ok here to have it at teh end
    ZodiacText.close()
    
    return ZodiaclistTemp
    #zodiac calculation will collect the birth year and determine the chinese
    #zodiac sign and then display 
    
def ZodiacCalculation():

#ask the user for input
#we're just going to assign a variable for moment. come back later
    birthYear=input("what year were you born? ")
    try:
        birthYear = int(birthYear)

    #print(zodiacIndex)

    #tell user the result

    #for  in Zodiaclist
    #list is not in correct order. fix by substarcting birthyear by 4
    
        zodiacIndex = (birthYear - 4) % 12
        print("your chinese zodiac animal is a ", Zodiaclist [zodiacIndex])
        
    except ValueError:
        print ("you did not provide a year in the form of an integer.")
    return birthYear

# repeat
Zodiaclist = zodiacSetup()
birthYear = 0
while type(birthYear) is int:
    birthYear = ZodiacCalculation()


# In[ ]:




# In[ ]:




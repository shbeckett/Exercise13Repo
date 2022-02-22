#code to open and append to pelican poem
pelicanpoem = open("pelican.txt", 'a+')
#append using write method
line1 = "A wonderful bird is the pelican, \n"
pelicanpoem.write(line1)
#append using write method
line2 = "His bill holds more than his belican, \n"
pelicanpoem.write(line2)
#create list and append using writelines nb line breaks needed
lines = ["He can take in his beak, \n", "Enough food for a week, \n", "But I'm damned if I see how the helican. \n"]
pelicanpoem.writelines(lines)
#how to close file?
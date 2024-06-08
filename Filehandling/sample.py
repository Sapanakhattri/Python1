#to open data from main file
# f=open("filehandling/main.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# f.close()

# #to append in the main file
# f=open("filehandling/main.txt","a")
# f.write("\nI am a Civil Engineer. ") #to write in new line
# f.close()

# #to rewrite/replace in the main file
# f=open("filehandling/main.txt","w")
# f.write("I am a Civil Engineer. ")
# f.close()

# #to create a new file
# f=open("filehandling/sample2.txt","w")
# f.close()

# #WAP to create a new file "practice.txt" and write data
# f=open("filehandling/practice.txt","w")
# f.write("Hi everyone" "\nI am learning python" "\nI am learning file handling." "I love coding")
# f.close()

#WAP to rewrite "python" with "java" 
f=open("filehandling/practice.txt","r")
data=f.read()
new_data=data.replace("python","java")
print(new_data)
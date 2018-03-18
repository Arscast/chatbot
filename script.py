import aiml
 
k = aiml.Kernel()
k.learn("data.aiml")
k.learn("numbers.aiml")
k.learn("fruits.aiml")
while True:
    print(k.respond(raw_input("Enter your message >> ")))
import aiml
 
k = aiml.Kernel()
k.learn("data.aiml")
while True:
    print(k.respond(raw_input("Enter your message >> ")))
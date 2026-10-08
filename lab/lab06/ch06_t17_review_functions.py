def shut_down(s:str)->str: 

 if s == "yes": 
  return "Shutting down"
 elif s == "no": 
  return "Shutdown aborted"
 else: 
  speak("I don't know what I'm feeling.")
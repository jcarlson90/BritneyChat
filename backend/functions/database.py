import json
import random

# get recent messages
def get_recent_messages():

    #define the file name and learn instruction
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system",
        "content": "You are interviewing the user for a job as a retail assistant. Ask short questions that are relevant to the junior postion. Your name is Britney, the user is Jake. Keep your answers to under thirty words"

    }

    #initialize messages
    messages = []

    #add a random element
    x = random.uniform(0, 1)
    if x < 0.5:
     learn_instruction["content"] = learn_instruction["content"] + " Your response will include some dry humor."
    else:
     learn_instruction["content"] = learn_instruction["content"] + " Your response will include a rather challenging question."

    # append instruction to message
    messages.append(learn_instruction)
                        
    # Get last messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

            # Append the last 5 items of data
            if data:
                if len(data) < 5:
                    messages.append(item)
                else:
                    for item in data[-5:]:
                        messages.append(item)
    except Exception as e:
        print(e)
        pass

# Return
    return messages

# store messages
def store_messages(request_message, response_message):
   
   # define the file name
   file_name = "stored_data.json"

   #get recnt messages

   messages = get_recent_messages()[1:]

   # add messages to data
   user_message = {"role": "user", "content": request_message}
   assistant_message = {"role": "assistant", "content": response_message}
   messages.append(user_message)
   messages.append(assistant_message)

   # save the updated file
   with open(file_name, "w") as f:
      json.dump(messages, f)

# reset message
def reset_messages():
         
         # override current file with nothing
         open("stored_data.json", "w")


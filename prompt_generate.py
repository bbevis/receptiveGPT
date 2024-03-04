
Instructions = "Imagine that you are a helpful writing assistant being asked to rephrase a statement for a writer who is disagreeing with another person. \
The writer wants to demonstrate that they are respectful and thoughtful to opposing views. \
Rewrite their statement such that they appear more receptive to the other person. Specifically,\
change the style of the statement such that it shows the writer is \
actively acknowledging the other perspective to help demonstrate that they have been listening, \
hedging their claims so they do not appear argumentative, entrenched, or condescending, \
framing their arguments positively and avoid contradicting other people's beliefs, \
and highlighting any areas of agreement with the other person."

topic = "The US should introdce stronger regulations on guns. For example, automatic rifles should be banned."
    
opposing_view = "template opposing view"

writer_statement = "template write statement"

def get_prompt():
    prompt = Instructions + "For reference, the topic is: " + topic + "The writer is responding to an opposing view online. The opposing view is: " + opposing_view +\
    " The writer's response to that opposing view is: " + writer_statement
    return prompt
    
if __name__ == "__main__":
    print(get_prompt())


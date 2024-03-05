
baseline_instructions = "Rewrite a statement for a writer who wants to appear more receptive to other people's views."

recipe_instructions = "Specifically, change the style of the writer’s statement such that the writer acknowledges the other perspective, \
does not appear argumentative, entrenched or condescending, frames their arguments positively, \
avoids contradicting other people’s beliefs, and highlights any areas of agreement with the other person."

word_restrictions = "Use the same number of words the writer used in the writer's statement."

def get_prompt(prompt_type, writer_statement, opposing_view, topic):
    
    if prompt_type == "baseline":
        prompt = baseline_instructions + "For reference, the topic is: " + topic + "The writer is responding to an opposing view online. The opposing view is: " + opposing_view +\
        " The writer's response to that opposing view is: " + writer_statement
    elif prompt_type == "recipe":
        prompt = baseline_instructions + recipe_instructions + "For reference, the topic is: " + topic + "The writer is responding to an opposing view online. The opposing view is: " + opposing_view +\
        " The writer's response to that opposing view is: " + writer_statement
    elif prompt_type == "words":
        prompt = baseline_instructions + recipe_instructions + "For reference, the topic is: " + topic + "The writer is responding to an opposing view online. The opposing view is: " + opposing_view +\
        " The writer's response to that opposing view is: " + writer_statement + word_restrictions
    
    return prompt
    
if __name__ == "__main__":
    print(get_prompt())



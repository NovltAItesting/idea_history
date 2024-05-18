# import streamlit as st
# import json
# from modules import summerize,ideagen
# json_file_path = 'history.json'

# st.title('Content Generation with history 💡')
# but = st.button("generate",type='primary')
# if  but:
#     with open(json_file_path, 'r') as file:
#         existing_json_data = json.load(file)
#     idea_history = [ list(i.keys())[0] for i in existing_json_data]
#     if len(idea_history) > 0:
#         summary ,token_genrated_summary,token_input_summary,response_time_summary,cost_summary = summerize(idea_history)
#     else:
#         summary=''

#     idea,token_genrated_idea,token_input_idea,response_time_idea,cost_idea = ideagen(company_profile="""
# Approach: Creator/Influencer
# Focus: Fashion and Beauty
# Target Audience: Hobbyists, Beginners, Enthusiasts
# Emotions evoked: Uplifting, Inspiration/Motivation
# Values represented: Entertainment, Inspiration/Motivation
# Motivations: Passion/Hobby, Positive impact, Personal experiences
# Brand Vision: "Empowering individuals to express themselves through fashion and beauty, while promoting positivity and self-love." """ ,summary=summary)
#     idea_updated =[{i:j} for i,j in idea.items()]
#     idea_his = '\n'.join(idea_history)
#     st.write('old_ideas')
#     st.write(idea_his)
#     st.write('history Summary')
#     st.write(summary)
#     st.write('New idea')
#     st.write(idea)


#     with open(json_file_path, 'r+') as file:
#         existing_json_data = json.load(file)
#         existing_json_data = existing_json_data + idea_updated
#         json.dump(existing_json_data, file, indent=4)






    









import streamlit as st
import json
from modules import summerize, ideagen

json_file_path = 'history.json'

st.title('Content Generation with history 💡')
but = st.button("generate", type='primary')

Approach = st.text_input(label='Approch',value='Creator/Influencer')
Focus = st.text_input(label='Focus',value='Fashion and Beauty')
Target_Audience = st.text_input(label='Target Audience',value='Hobbyists, Beginners, Enthusiasts')
Emotions_evoked = st.text_input(label='Emotion Evoked',value='Uplifting, Inspiration/Motivation')
Values_represented = st.text_input(label='Value Represented',value='Entertainment, Inspiration/Motivation')
Motivations = st.text_input(label='Motivations',value='Passion/Hobby, Positive impact, Personal experiences')
Brand_Vision = st.text_input(label='Brand Vision',value='Empowering individuals to express themselves through fashion and beauty, while promoting positivity and self-love.')

if but:
    # Open the JSON file and load the data
    with open(json_file_path, 'r') as file:
        existing_json_data = json.load(file)
    
    # Extract idea history from existing JSON data
    idea_history = [list(i.keys())[0] for i in existing_json_data]
    
    if len(idea_history) > 0:
        summary, token_genrated_summary, token_input_summary, response_time_summary, cost_summary = summerize(idea_history)
    else:
        summary = ''
    
    idea, token_genrated_idea, token_input_idea, response_time_idea, cost_idea = ideagen(company_profile=f"""
Approach: {Approach}
Focus: {Focus}
Target Audience: {Target_Audience}
Emotions evoked: {Emotions_evoked}
Values represented: {Values_represented}
Motivations: {Motivations}
Brand Vision: {Brand_Vision} """, summary=summary)
    
    idea_updated = [{i: j} for i, j in idea.items()]
    idea_his = ' \n'.join(idea_history)
    
    st.write('old_ideas')
    st.write(idea_his)
    st.write('history Summary')
    st.write(summary)
    st.write('New idea')
    st.write(idea)
    
    MAX_LENGTH = 20

    with open(json_file_path, 'r+') as file:
        # Load existing data
        existing_json_data = json.load(file)

        # Calculate the number of new items to add
        new_items_count = len(idea_updated)

        # Ensure the total length doesn't exceed the maximum length
        total_length = len(existing_json_data) + new_items_count
        if total_length > MAX_LENGTH:
            # Calculate how many items to remove
            items_to_remove = total_length - MAX_LENGTH
            # Remove old items
            existing_json_data = existing_json_data[items_to_remove:]

        # Add new items
        existing_json_data.extend(idea_updated)

        # Move the file pointer to the beginning
        file.seek(0)
        # Save updated data
        json.dump(existing_json_data, file, indent=4)
        # Truncate the file to remove any leftover data
        file.truncate()

    with open('mainhistory.json', 'r+') as file:
        existing_json_data = json.load(file)
        existing_json_data.extend(idea_updated)
        file.seek(0)  # Reset the file position to the beginning
        json.dump(existing_json_data, file, indent=4)
        file.truncate()  # Remove any remaining part from the previous data
    


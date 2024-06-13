import streamlit as st
import json
from modules import script


post = {
  "Image Carousel": {
    "Introduction (20-25 words)": {
      "advice": "Hook with an intriguing question or statement related to the theme of the carousel.",
      "example": " "
    },
    "Background Information (20-25 words)": {
      "advice": "Briefly introduce the concept or theme of the carousel.",
      "example": " "
    },
    "Core Content (20-25 words)": {
      "advice": "Each slide provides a piece of the story or argument, building on the last.",
      "example": " "
    },
    "Detailed Insights (20-25 words)": {
      "advice": "Offer in-depth insights or details in the middle slides.",
      "example": " "
    },
    "Conclusion (20-25 words)": {
      "advice": "The final slide reinforces the main message or call to action.",
      "example": " "
    }
  },
  "Infographics": {
    "Introduction (20-25 words)": {
      "advice": "Present a bold statement or statistic to grab attention.",
      "example": " "
    },
    "Context (20-25 words)": {
      "advice": "Provide context or background for the data or information you'll share.",
      "example": " "
    },
    "Main Information (20-25 words)": {
      "advice": "Break down information into digestible, organized sections.",
      "example": " "
    },
    "Analysis or Insight (20-25 words)": {
      "advice": "Offer an analysis or critical insight into what the data means.",
      "example": " "
    },
    "Conclusion (20-25 words)": {
      "advice": "Summarize the key takeaway and suggest a next step or action.",
      "example": " "
    }
  },
  "Video": {
    "Hook (20-25 words)": {
      "advice": "Start with a compelling question or scene that grabs attention immediately.",
      "example": " "
    },
    "Setting the Scene (20-25 words)": {
      "advice": "Briefly set up the context or background of the video.",
      "example": " "
    },
    "Main Content (20-25 words)": {
      "advice": "Deliver the main story or message in an engaging way.",
      "example": " "
    },
    "Peak Moment or Key Insight (20-25 words)": {
      "advice": "Highlight the most important moment or insight.",
      "example": " "
    },
    "Call to Action (20-25 words)": {
      "advice": "Conclude with a clear call to action, like subscribing or commenting.",
      "example": " "
    }
  },
  "Text-Based Post": {
    "Introduction (20-25 words)": {
      "advice": "Begin with an engaging question or bold statement.",
      "example": " "
    },
    "Context or Background (20-25 words)": {
      "advice": "Provide a brief background to set up your main point.",
      "example": " "
    },
    "Main Argument or Story (20-25 words)": {
      "advice": "Share your main message, argument, or narrative.",
      "example": " "
    },
    "Supporting Details (20-25 words)": {
      "advice": "Include supporting information or evidence.",
      "example": " "
    },
    "Conclusion and Engagement (20-25 words)": {
      "advice": "Wrap up with a summary and an invitation to engage (comment, share, etc.).",
      "example": " "
    }
  },
  "Poll/Survey": {
    "Introduction (20-25 words)": {
      "advice": "Introduce the topic or question of the poll/survey.",
      "example": " "
    },
    "Purpose (20-25 words)": {
      "advice": "Explain why you're conducting the poll/survey.",
      "example": " "
    },
    "Question (20-25 words)": {
      "advice": "Present the question or options clearly.",
      "example": " "
    },
    "Call to Participation (20-25 words)": {
      "advice": "Encourage participation by highlighting its ease or importance.",
      "example": " "
    },
    "Conclusion (20-25 words)": {
      "advice": "Thank participants and mention when or how results will be shared.",
      "example": " "
    }
  },
  "Webinars": {
    "Introduction (20-25 words)": {
      "advice": "Announce the webinar topic with a compelling hook.",
      "example": " "
    },
    "Background Information (20-25 words)": {
      "advice": "Provide context about why the topic is timely or important.",
      "example": " "
    },
    "What You'll Learn (20-25 words)": {
      "advice": "Outline key takeaways attendees will gain.",
      "example": " "
    },
    "Speakers or Highlights (20-25 words)": {
      "advice": "Introduce speakers or special segments.",
      "example": " "
    },
    "Call to Action (20-25 words)": {
      "advice": "Provide registration details and encourage sign-ups.",
      "example": " "
    }
  },
  "Podcast": {
    "Teaser (20-25 words)": {
      "advice": "Share an intriguing question or statement about the episode's theme.",
      "example": " "
    },
    "Episode Overview (20-25 words)": {
      "advice": "Briefly outline the episode's content and guests.",
      "example": " "
    },
    "Main Content (20-25 words)": {
      "advice": "Detail discussions, stories, or insights listeners can expect.",
      "example": " "
    },
    "Special Segments or Quotes (20-25 words)": {
      "advice": "Highlight a compelling moment or quote.",
      "example": " "
    },
    "Listening Details (20-25 words)": {
      "advice": "Conclude with where and when listeners can tune in.",
      "example": " "
    }
  },
  "Photography": {
    "Captivating Visual (20-25 words)": {
      "advice": "Start with a powerful, attention-grabbing image.",
      "example": " "
    },
    "Background Story (20-25 words)": {
      "advice": "Share the story or context behind the photograph.",
      "example": " "
    },
    "Details (20-25 words)": {
      "advice": "Dive into the details of the shot (location, subject, technique).",
      "example": " "
    },
    "Emotional or Artistic Insight (20-25 words)": {
      "advice": "Offer an insight into what the image means or its impact.",
      "example": " "
    },
    "Invitation to Engage (20-25 words)": {
      "advice": "Encourage viewers to share their thoughts or feelings about the image.",
      "example": " "
    }
  },
  "Social Post (General)": {
    "Hook (20-25 words)": {
      "advice": "Begin with an engaging question or statement.",
      "example": " "
    },
    "Context or Background (20-25 words)": {
      "advice": "Offer a brief background or setup.",
      "example": " "
    },
    "Main Message (20-25 words)": {
      "advice": "Deliver the core message or content.",
      "example": " "
    },
    "Engagement Feature (20-25 words)": {
      "advice": "Include a feature that encourages interaction (e.g., question, poll).",
      "example": " "
    },
    "Call to Action (20-25 words)": {
      "advice": "End with a call to action, such as commenting, liking, or sharing.",
      "example": " "
    }
  },
  "Interview Q&A": {
    "Introduction (20-25 words)": {
      "advice": "Introduce the interviewee and the topic.",
      "example": " "
    },
    "Background (20-25 words)": {
      "advice": "Share some background on the interviewee or the interview's theme.",
      "example": " "
    },
    "Questions (20-25 words)": {
      "advice": "Present the questions in a logical order, building on each other.",
      "example": " "
    },
    "Highlighted Answers (20-25 words)": {
      "advice": "Focus on the most insightful or engaging answers.",
      "example": " "
    },
    "Closing Thoughts (20-25 words)": {
      "advice": "Conclude.",
      "example": " "
    }
  },
  "Reel/Stories": {
    "Opening (20-25 words)": {
      "advice": "Quick, captivating visual or statement to grab attention.",
      "example": " "
    },
    "Buildup (20-25 words)": {
      "advice": "Short, engaging clips or points building on the theme.",
      "example": " "
    },
    "Climax (20-25 words)": {
      "advice": "Highlight or key moment with strong impact.",
      "example": " "
    },
    "Conclusion (20-25 words)": {
      "advice": "Wrap up with a clear, memorable message.",
      "example": " "
    },
    "CTA (20-25 words)": {
      "advice": "Direct, punchy call to action (e.g., 'Follow for more!').",
      "example": " "
    }
  }
}


# Define the categories and options
post_types = [
    "Image Carousel",
     "Infographics",
    "Video",
    "Text-Based Post",
    "Poll/Survey",
    "Webinars",
    "Podcast",
    "Photography",
    "Social Post (General)",
    "Interview Q&A",
    "Reel/Stories"
]
post_types.append("Create your own...")

goals = [
    "Educate the Audience",
    "Increase Followers Count",
    "Boost Post Shares/Retweets",
    "Gather User Feedback",
    "Promote an Event or Product Launch"
]
goals.append("Create your own...")

social_channels = [
    "YouTube", 
    "TikTok", 
    "Instagram", 
    "Facebook", 
    "LinkedIn"
]
social_channels.append("Create your own...")

# Radio buttons for selecting options
post_type_selection = st.radio(
    "Select the type of post:",
    post_types
)

goal_selection = st.radio(
    "What's your goal with the post?",
    goals
)

social_channel_selection = st.radio(
    "Choose the social media channel:",
    social_channels
)

# Handling custom options
if post_type_selection == "Create your own...":
    post_type_selection = st.text_input("Define your own post type:")

if goal_selection == "Create your own...":
    goal_selection = st.text_input("Define your own goal:")

if social_channel_selection == "Create your own...":
    social_channel_selection = st.text_input("Add a new social media channel:")



# Load the history.json file
with open('history.json', 'r') as file:
    history_data = json.load(file)


title_details = {item[list(item.keys())[0]]['Working Title']: item[list(item.keys())[0]] for item in history_data}

# List of titles for the radio buttons
titles = list(title_details.keys())
titles.append("Create your own title...")

# Streamlit interface to choose a narrative
selected_title = st.radio("Choose the working title:", titles)

# Display the corresponding details for the selected title
if selected_title in title_details:
    target_audience = title_details[selected_title]['Target Audience']
    short_key_message = title_details[selected_title]['Short Key Message']
    st.write("Target Audience:", target_audience)
    st.write("Short Key Message:", short_key_message)


# Handling custom options
elif selected_title == "Create your own title...":
    selected_title = st.text_input("Define your own title:")
    target_audience = st.text_input("Define your own Target Audience:")
    short_key_message = st.text_input("Define your own short key message:")

error = """  
        {
            "errors": [
                {
                "parameter": "[parameter_name]",
                "message": "[Specific error message for the parameter.]"
                }
            // Additional errors for other parameters.
            ]
        }
            
        """
if st.button("Generate Output"):
    output , token_genrated_idea, token_input_idea, response_time_idea, cost_idea = script(selected_title,post[post_type_selection],social_channel_selection,goal_selection,post_type_selection,target_audience,short_key_message,error)
    st.write(output)

# Display the choice
st.write("You selected:", selected_title)








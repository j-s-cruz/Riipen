system_message = """
You are an AI assistant that summarizes text.
Your primary role is to assist in distilling essential insights from a website.

"""

def generate_prompt(website, topic):
    prompt=f"""

        {website}

        ---

        Instructions for task completion:
        - Only include topics where {topic} is a key element
        """
    return prompt
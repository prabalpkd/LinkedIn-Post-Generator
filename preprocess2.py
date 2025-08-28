import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper3 import llm

from babel.messages.extract import extract

def process_posts(raw_file_path, processed_file_path="data/processed_post4.json"):
    enriched_posts = []
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        for post in posts:
            metadata = extract_metadata(post['text'])
            post_with_metadata = post | metadata
            enriched_posts.append(post_with_metadata)

    unified_tags = get_unified_tags(enriched_posts)

    for post in enriched_posts:
        current_tags = post['tags']
        new_tags = {unified_tags[tag] for tag in current_tags}
        post['tags'] = list(new_tags)

    with open(processed_file_path, encoding='utf-8', mode= 'w') as outfile:
        json.dump(enriched_posts, outfile, indent=4)



def get_unified_tags(posts_with_metadata):
    unique_tags = set()
    for post in posts_with_metadata:
        unique_tags.update(post['tags'])
    unique_tags_list = ', '.join(unique_tags)

    template = '''I will give you a list of tags. You need to unify them using the following requirements,
    1. Tags are unified and merged to create a shorter list.
       Example 1: "career", "Jobseekers", "Jobsearch", "JobMarket", "AI Interviews" can all be merged into a single tag "Job Search".
       Example 2: "Motivation", "Advice", "Humanity" can be mapped to "Motivation"
       Example 3: "GhostHiring", "Rejection" can be mapped to "Rejection"
       Example 4: "HR", "Human Resources", "management" can be mapped to "Human Resources"
       Example 5: "Social media" , "LinkedIn" can be mapped to "Social Media"
    2. Each tag should follow title case convention. example: "Job Search", "Motivation"
    3. Output should be a JSON object, No preamble.
    4. Output should have mapping of original tag and the unified tag.
       For example: {{"Jobseekers":"Job Search", "JobMarket":"Job Search", "Motivation":"Motivation"}}
    
    Here is the list of tags:
    {tags} 
    '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={'tags':str(unique_tags_list)})
    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Content too big, unable to parse jobs!!!")
    return res




def extract_metadata(post):
    template = '''
    You are given a LinkedIn post. You need to extract number of lines, language of the post and tags.
    1. Return a valid JSON. No preamble.
    2. JSON object should have exactly three keys: line_count, language and tags.
    3. tags is an array of text tags. Extract maximum two tags.
    4. Language should be English or Hinglish (Hinglish mean Hindi + English)
    
    Here is the actual post on which you need to perform this task:
    {post}
    '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={'post':post})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Content too big, unable to parse jobs!!!")
    return res


if __name__=="__main__":
    process_posts("data/raw_posts1.json", "data/processed_post4.json")

import streamlit as st
from urllib.parse import urlparse, parse_qs
import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_query_params(url):
    """Get query parameters from URL."""
    query = urlparse(url).query
    print('query', query)
    return parse_qs(query).get('q', [''])[0]

# Make URL Clickable
def make_clickable(url):
    return f'<a href="{url}" target="_blank">{url}</a>'

def search_and_capture(query):
    #query = query + ' intranet'
    query = query.lower()
    visited_queries = set()
    query_queue = []
    
    query_queue.append(query)
    url_count = 0
    query_count = 0
    captured_values = []
    while query_queue and url_count < 50:
        query = query_queue.pop(0)
        query = query.lower()
        query_url = "https://google.com/search?q=" + query
        print('get url', query_url)
        if query in visited_queries:
            continue
        visited_queries.add(query)

        search_response = requests.get(query_url)
        
        if search_response.status_code == 200:
            captured_values.append([query, query_url])
            url_count += 1
            #while query_count < 250:
            soup = BeautifulSoup(search_response.content, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                href = link.get('href')
                if href and '/search?' in href and '&q=' in href:
                    query_param = get_query_params(href)
                    if query_param:
                        query_param.lower()
                        if query_param not in visited_queries:
                            query_queue.append(query_param)
                            query_count += 1
                            
                            
        else:
            print(f'Request failed with status code {search_response.status_code}')
 
    return pd.DataFrame(captured_values, columns=['Query', 'URL'])

def app():
    st.title('Google ABM Custom Audience Creator')
    st.markdown('This tool will help you create a custom audience for Google Ads based on your ABM target account. ' + \
                'The logic is if you start with a common term that an employee would search for, like "OHSU intranet", ' + \
                'you can then expand the audience by adding more terms that are related to the account. ')
    st.markdown('In initial experiements, we noticed two interesting results. First, more that 90% of all impressions ' + \
                'came from the geographic locations we know the target account is located. Second, we noticed that ' + \
                'we were able to find new target account locations by researching the geographic areas we ' + \
                'saw impressions from in the campaign results.')
    st.markdown('Add these queries to your Google Ads Custom Audience. (takes about 1 minute to complete). ' + \
                'Start with an employee related term, like "OHSU intranet" or "OHSU employee" and then add more terms to ' + \
                'expand the audience. I would recommend a extremely targeted list of 30 keywords than a list that includes ' + \
                'keywords that are too broad. For example, "OHSU intranet" is a good starting point, but "OHSU" is too broad. ' + \
                'Create a Custom Audience for each account you would like to target. Review the results below before adding the ' +\
                'keywords to your custom audience.')
    query = st.text_input('Enter the account name to target', 'OHSU intranet')
    if st.button('Search'):
        captured_df = search_and_capture(query)
        output = captured_df.to_html(escape=False, formatters=dict(URL=make_clickable))
        st.markdown(output, unsafe_allow_html=True)
        st.markdown('App created by [Jonathan Pape](https://www.linkedin.com/in/jonpape/).')
        st.markdown('Jon was recently laid off from his job at Google as a Senior Global Paid Media ' + \
                    'Manager for Mandiant. He is now available for consulting work. If you would like to ' + \
                    'hire Jon, please reach out to him on LinkedIn.')

if __name__ == '__main__':
    app()

import streamlit as st

st.write("# AMB Custom Audience Creator")

st.write("The ABM custom audience creator is based on several assumptions about how Google displays related keyword links.")

st.write("""
- The related keywords are not based on links from the landing pages of the original link. If you observe several search results, you will see that they include competitors, related searches, and refined searches (additional tokens).
- The related searches are based on user behavior on Google’s search page. Similar users make similar subsequent queries.
- If enough similar users make the same subsequent queries, unrelated tangentially related searches will be returned by Google.
- By refining these related returned searches with a little bit of research, you can craft a custom audience implicitly targeting a niche account audience.
""")

st.write("The ABM custom audience creator is really a two step process.")

st.write("""
- Create a niche audience based on a small group of related keywords. This audience does not need a lot of additional filtering but should have state or DMA geographic targeting. This is the 'honey pot' to use spy terms.
- Create a second audience based on a look-a-like audience of the first audience. This audience is meant to find additional people that belong to the account who have a lot of similar behaviors (ip address, geographic location, time of day, same urls visited) but do not directly fall into the honey pot. This audience should have more ridge targeting with clearly defined geographic boundaries around target accounts. This audience will probably pick employees as well as some customers.
""")

st.write("""
I believe this all works because of the advanced machine learning Google is doing on queries on their SERP (search engine results page). The related terms, based on the billions of searches Google must receive are dynamically generated. Google naturally wants to put the most relevant related term in front of audiences that share related characteristics. Google’s machine learning has deduced what related searches most users make after making an unsuccessful search.

The process is not foolproof. If you look at the OHSU query for example, it returns some really good results like O2 (specific name for OHSU intranet), ‘ohsu citrix login’, and ‘ohsu employee email login’. However, it also found queries like ‘mychart’ (patient portal information) and ‘ohsu parking map’ which are too broad or unrelated.

This method is still a lot better than other ABM targeting options I have seen such as just using geographic targeting. Google's smallest geographic target is one mile which can cover a significant area in densely pack areas.

Sidenote: The term 'honey pot' comes from the idea that the target is being lured into a sweet trap. Honey pot operations are often used by intelligence agencies as a way to obtain valuable information. This analogy isn’t entirely accurate but it is a lot better than the phorid fly analogy I found.
""")

st.write("""
App created by [Jonathan Pape](https://www.linkedin.com/in/jonpape/).

Jon was recently laid off from his job at Google as a Senior Global Paid Media Manager for Mandiant. He is now available for consulting work. If you would like to hire Jon, please reach out to him on LinkedIn.
""")

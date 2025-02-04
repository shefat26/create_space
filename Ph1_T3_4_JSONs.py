#!/usr/bin/env python
# coding: utf-8

# <div style="color:white;
#            display:fill;
#            border-radius:5px;
#            background-color:#5642C5;
#            font-size:200%;
#            font-family:Arial;letter-spacing:0.5px">
# 
# <p width = 20%, style="padding: 10px;
#               color:white;">
# Base Python: JSON Files
#               
# </p>
# </div>
# 
# Data Science Cohort Live NYC Jan 2025
# <p>Phase 1</p>
# <br>
# <br>
# 
# <div align = "right">
# <img src="Images/flatiron-school-logo.png" align = "right" width="200"/>
# </div>
#     
#     

# #### JSON file format:
# 
# - one of most popular data formats for the web
# - JSON stands for JavaScript Object Notation:
#     - **plain text** format. 
#     - Object structure of data encoded in hierarchical syntax.
#     
# Best to see example:

# Here's a brief preview of a JSON file:  
# 
# <img src="Images/json_preview.png" width="850">
# 

# - JSON is not a tabular format: 
# - Often nested in a hierarchical structure:
#     - Data structures analogous to Python dictionaries and lists. 
# 

# - Here's all of the built-in supported data types in JSON and their counterparts in Python: 
# 
# <img src="Images/json_python_datatypes.png" width=500>

# - Parsing complex structure of JSON without library:
#     - ain't no one got time for that.
# - Use json library.
# 
# 
# To use the `json` module, start by importing it:

# In[2]:


import json


# #### json.load()
# 
# To load data from a JSON file:
# 1. `open` file with context manager. 
# 2. Pass the file object to the `json.load` function.
# 3. Returns Python object representing contents of file.
# 
# In the cell below, we open the campaign finance JSON file previewed above:

# In[4]:


file_path = 'Data/nyc_2001_campaign_finance.json'

# instructor forgot how to load files for reading in a context manager.
# help him! 

with open(file_path, 'r') as f:
    data = json.load(f)


print(type(data))


# Loaded data is dictionary:
# - Now can investigate contents of a JSON file by accessing traditional Python data structures.

# #### Parsing a JSON File
# 
# Since we have a dictionary, check its keys:

# In[6]:


# check keys of dict for me. How do I do that?
data.keys()


# Check type of data stored in those keys:

# In[7]:


# my memory is real foggy on how to access a list of data stored in a dict 
for key, val in data.items():
    print(type(val))
    print(key)


# #### Parsing Metadata
# 
# Then we can dig a level deeper. What are the keys of the nested dictionary?

# In[5]:


data['meta'].keys()


# And what is the type of the value associated with that key?

# In[8]:


type(data['meta']['view'])


# Again, what are the keys of that twice-nested dictionary?

# In[9]:


data['meta']['view'].keys()


# Lot of keys, but let's check out that data:

# In[31]:


[print(key + ": " + str(val)) for key,val in data['meta']['view'].items()]


# Data in `view` under the `meta` key: metadata about the dataset.
# - category
# - attribution
# - tags, etc.
# 
# Now let's look at the main data.

# #### Parsing Data
# 
# Look at data inside the `data` key:
# - Recall: had `list` data type.
# - Let's look at the length:

# In[6]:


len(data['data'])


# Now let's look at a couple different values:

# In[13]:


data['data'][0]


# In[7]:


data['data'][4]


# In[8]:


len(data['data'][1])


# Looks more tabular in form: 
# - First row is some kind of header. 
# - Clearly needs cleaning and understanding of data scheme for further action.

# #### Extracting a Value from a JSON File
# 
# We want to:
# 
# - Extract the description of the dataset.
# 
#     - JSON file contains `meta` and `data`
#     - `meta` has this kind of high-level information.
#     - `data` has the actual records relating to campaign finance.
# 
# Thus let's look at the keys of `meta` again:

# In[16]:


data['meta']['view'].keys()


# Ok, `description` is the 7th one! 
# 
# Let's pull the value associated with the `description` key:

# In[9]:


data['meta']['view']['description']


# Great! This is the general process you will use when extracting information from a JSON file.

# In[8]:


class_attendance = {'aggregate': {'num_present': 3, 'fraction': 1.0}, 'attendance_log': {'Bob': 1, 'Alice': 1, 'Ryan': 1}}


# In[10]:


class_attendance


# In[12]:


with open('attendance.json', 'w') as f:
    json.dump(class_attendance, f)


# In[13]:


json.dumps(class_attendance)


# #### Summary
# 
# - Deeply nested structure of JSON data files can be complex.
# - Upside is flexibility in encoding data.
# - Need to understand data scheme. 
# 
# Upcoming lab: practice loading JSONs + parse/extract the data.

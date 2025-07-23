# WRTS-Forum-Api

## 🎉 V2 is here

Welcome to the python api wrapper of [StudyGo](https://studygo.com). 
The api wrapper covers the forum, groups and more. Technical stuff at the end of the README.

> Note: features regarding lists and such are nonexistent
___

## All features:
- Authentication based on email and password, can be done in bulk using multi-threading. It auto-requests a token.
- Additional tools such as Captcha solving (paid with capmonster), integrated multi-threading and extensive error handling.
- Interaction with the Q&A forum, having full control over all data.
- Groups; join and leave other groups.
- Being able to mass read accounts from files.

## Project structure
```
WRTSToolsV2/
├── Base/                    # Core client classes
│   ├── Client.py           # Single client authentication
│   ├── ClientAuth.py       # Authentication handler
│   ├── ClientCluster.py    # Multi-account cluster manager
│   └── ClientRequests.py   # API request wrapper
├── Classes/                 # Data models and managers
│   ├── ForumAnswer.py      # Forum answer object
│   ├── ForumManager.py     # Forum operations manager
│   ├── ForumPost.py        # Forum post object
│   ├── GroupInvite.py      # Group invitation handler
│   ├── GroupManager.py     # Group operations manager
│   ├── User.py             # User data model
│   └── UserProfileImage.py # User profile image handler
├── Errors/                  # Custom error classes
├── accounts.txt            # Account credentials file
├── accounts_6000.txt       # Extended account list
├── captha.py              # CAPTCHA solving utilities
├── main.py                # Main application entry point
└── Errors.py              # Error definitions
```
## Installation
1. Clone the repository:
```
git clone https://github.com/HologramSteve/wrts-forum-api.git
cd wrts-forum-api 
```

2. Install packages
```
pip install requests
```

3. (Optional) Configure CAPTCHA solving:
- Set up CapMonster API key in captha.py

## Usage
### Single client usage
```python
from Base.Client import Client

# Initialize single client
client = Client("email@example.com", "password")

# Access forum manager
forum = client.Forum
posts = forum.fetchForumPosts()
```

### Forum interaction
```python
# Fetch specific post
post = client.Forum.fetchPost("post_id")

# Answer a post
post.answer("Your answer content here")

# Like an answer
for answer in post.answers:
    if not answer.liked:
        answer.like()
```

## Multiple client usage
The `accounts.txt` file must contain at least 1 account in the format `email:password`.
Then use a `ClientCluster` instead of normal `Client` and you're set!

## Documentation has been moved here -> []()

## Credits and notes
- The project is fully made by me, but the docs HTML is generated with AI (still 100% accurate). 
- You can always open an issue for questions.
- Pull requests are welcome!
Thanks for reading <3
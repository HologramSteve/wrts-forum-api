# WRTS Tools V2

A Python automation toolkit for interacting with the WRTS (StudyGo) API. This project provides a comprehensive set of tools for managing accounts, forum interactions, and group operations.

## 🚀 Features

### Account Management
- **Bulk Account Authentication**: Support for multiple account credentials
- **Token Management**: Automatic token generation and validation
- **Cluster Operations**: Manage multiple accounts simultaneously

### Forum Management
- **Forum Post Fetching**: Retrieve and parse forum posts
- **Answer Management**: Like, unlike, and interact with forum answers
- **User Interaction**: Access user profiles and information
- **Automated Responses**: Post answers to forum questions

### Group Operations
- **Group Invites**: Handle group invitation codes
- **Group Management**: Manage group memberships and operations

### Additional Tools
- **CAPTCHA Solving**: Integration with CapMonster for automated CAPTCHA solving
- **Error Handling**: Comprehensive error management system
- **Multi-threading**: Concurrent operations for improved performance

## 📁 Project Structure

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

## 🛠️ Installation

### Prerequisites
- Python 3.7+
- Required packages:
  ```bash
  pip install requests
  ```

### Setup
1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd WRTSToolsV2
   ```

2. Configure account credentials:
   - Add your WRTS account credentials to `accounts.txt`
   - Format: `email:password` (one per line)

3. (Optional) Configure CAPTCHA solving:
   - Set up CapMonster API key in `captha.py`

## 📖 Usage

### Basic Usage

```python
from Base.ClientCluster import ClientCluster

# Load accounts from file
with open("accounts.txt", 'r') as f:
    credentials = f.read().split("\n")

# Initialize client cluster
client = ClientCluster(credentials)

# Fetch forum posts
posts = client.Forum.fetchForumPosts(limit=10)

# Interact with posts
for post in posts:
    print(f"Post: {post.title}")
    for answer in post.answers:
        if answer.author.id == target_user_id:
            answer.like()
```

### Single Client Usage

```python
from Base.Client import Client

# Initialize single client
client = Client("email@example.com", "password")

# Access forum manager
forum = client.Forum
posts = forum.fetchForumPosts()
```

### Forum Operations

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

### Group Management

```python
# Handle group invites
group_invite = client.GroupManager.fetchGroupInvite("invite_code", "group_id")
```

## 🔧 Configuration

### Account Format
The `accounts.txt` file should contain credentials in the following format:
```
username1@example.com:password1
username2@example.com:password2
```

### API Endpoints
The tool connects to the WRTS API at:
- Base URL: `https://api.wrts.nl/api/v3`
- Authentication: Token-based authentication

## 🏗️ Architecture

### Core Components

1. **Client Classes**:
   - `Client`: Single account authentication and operations
   - `ClientCluster`: Multi-account management with threading
   - `ClientAuth`: Handles authentication logic
   - `ClientRequests`: API request abstraction

2. **Data Models**:
   - `ForumPost`: Represents forum posts with metadata
   - `ForumAnswer`: Represents answers with voting capabilities
   - `User`: User profile information
   - `GroupInvite`: Group invitation handling

3. **Managers**:
   - `ForumManager`: Forum-related operations
   - `GroupManager`: Group-related operations

### Threading Model
The `ClientCluster` class uses Python threading to authenticate multiple accounts concurrently, improving performance for bulk operations.

## 🛡️ Error Handling

The project includes comprehensive error handling:

- `TokenInvalidError`: Authentication failures
- `InvalidActionError`: Invalid operations (e.g., liking already liked content)
- Custom error classes for specific API failures

## ⚠️ Important Notes

### Legal and Ethical Considerations
- **Terms of Service**: Ensure compliance with WRTS/StudyGo Terms of Service
- **Rate Limiting**: Be mindful of API rate limits to avoid being blocked
- **Responsible Usage**: Use automation tools responsibly and ethically

### Security
- **Credential Storage**: Store credentials securely
- **Token Management**: Tokens are handled automatically but should be kept secure
- **API Keys**: Keep CAPTCHA solving API keys private

## 🔍 Examples

### Automated Like Bot
```python
# Example from main.py
while True:    
    post = c.Forum.fetchPost(input("Enter post ID..."))
    for answer in post.answers:
        if answer.author.id == 187522664:  # Target user ID
            print("Found answer, liking!")
            answer.like()
            print("Completed!")
```

### Bulk Post Analysis
```python
posts = client.Forum.fetchForumPosts(limit=50)
for post in posts:
    print(f"Title: {post.title}")
    print(f"Author: {post.author.username}")
    print(f"Answers: {len(post.answers)}")
    print("---")
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is for educational purposes. Please ensure compliance with all applicable terms of service and laws.

## ⚡ Performance Tips

- Use `ClientCluster` for multiple account operations
- Implement proper rate limiting for API calls
- Use threading for concurrent operations
- Cache frequently accessed data

## 🐛 Troubleshooting

### Common Issues

1. **Authentication Errors**:
   - Verify credentials in `accounts.txt`
   - Check for account lockouts or CAPTCHA requirements

2. **API Errors**:
   - Ensure proper network connectivity
   - Check for API rate limiting
   - Verify API endpoint availability

3. **Threading Issues**:
   - Monitor for race conditions in multi-threaded operations
   - Implement proper locking mechanisms

## 📞 Support

For issues and questions:
1. Check the error logs for specific error messages
2. Verify account credentials and API connectivity
3. Review the WRTS API documentation for changes

---

**Disclaimer**: This tool is provided for educational purposes only. Users are responsible for ensuring compliance with all applicable terms of service and laws.

import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body
        
    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body
        
    def get_emojis(self):
        r = requests.get("https://api.github.com/emojis")
        emojis = r.json()
        
        return emojis
        
    def list_commits(self, repo_name):
        r = requests.get(
            f"https://api.github.com/repos/{repo_name}/commits"
        )
        commits = r.json()
        
        return commits    

import requests
base_url = "https://jsonplaceholder.typicode.com"


def getPosts():
    response = requests.get(f"{base_url}/posts")
    response.raise_for_status()

    posts = [post for post in response.json() if len(post['title'].split()) <= 6]

    posts = [post for post in posts if len(post['body'].split('\n')) <= 3]

    return posts

def createPost(title, body, userId):
    data = {
        'title': title,
        'body': body,
        'userId': userId
    }
    response = requests.post(f"{base_url}/posts", json=data)
    response.raise_for_status()
    return response.json()

def updatePost(post_id, title, body):
    data = {
        'title': title,
        'body': body
    }
    response = requests.put(f"{base_url}/posts/{post_id}", json=data)
    response.raise_for_status()
    return response.json()

def deletePost(post_id):
    response = requests.delete(f"{base_url}/posts/{post_id}")
    response.raise_for_status()
    return f"Post with ID {post_id} deleted successfully."


if __name__ == "__main__":
    
    filtered_posts = getPosts()
    print("Filtered Posts:")
    for post in filtered_posts:
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("-----")

    
    n_post = createPost("New Post", " new post.", userId=1)
    print(f"New Post Created: {n_post}")

  
    updated_post = updatePost(n_post['id'], "Updated Post", " post.")
    print(f"Post Updated: {updated_post}")

    delete_result = deletePost(n_post['id'])
    print(delete_result)

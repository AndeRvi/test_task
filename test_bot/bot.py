import json
import requests

from random import randint

with open('config.json') as file:
    config = json.loads(file.read())

user_list = []
post_list = []

for _ in range(config.get("number_of_users")):
    sign_data_seed = randint(1, 10000000000)
    sign_data = {
        "username": f"{sign_data_seed}",
        "password": f"{sign_data_seed}",
    }
    user_list.append(sign_data)
    print(f"Create user {sign_data}")
    signup_request = requests.post(
        "http://127.0.0.1:8000/api/signup",
        data=sign_data
    )
    print(f"Result - {json.loads(signup_request.text)}")

    token = json.loads(
        requests.post(
            "http://127.0.0.1:8000/api/token/",
            data=sign_data
        ).text
    ).get("access")
    header = {
        'Authorization': f"Bearer {token}"
    }

    for _ in range(config.get("max_posts_per_user")):
        content = {
            "text": f"{randint(1, 10000000000)}"
        }
        print(f"Create post  - {content.get('text')}"
              f" from user - {sign_data.get('username')}"
              )
        post = requests.post(
            "http://127.0.0.1:8000/api/post",
            data=content,
            headers=header
        )
        print(f"Result - {json.loads(post.text)}")
        post_id = json.loads(post.text).get('id')
        post_list.append(post_id)

for user in user_list:
    token = json.loads(
        requests.post("http://127.0.0.1:8000/api/token/", data=user).text
    ).get("access")
    header = {
        'Authorization': f"Bearer {token}"
    }
    for _ in range(config.get("max_likes_per_user")):
        post = post_list[randint(0, len(post_list))]
        print(f"Create like to post  - {post} "
              f"from user - {user.get('username')} "
              )
        content = {
            "response": True,
        }
        like_request = requests.post(
            f"http://127.0.0.1:8000/api/post/{post}/like",
            data=content,
            headers=header
        )
        print(f"Result - {json.loads(like_request.text)}")

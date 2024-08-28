import requests


def get_novel(novel_id):
    # 小说微服务的URL
    novel_service_url = f"http://127.0.0.1:8001/novels/novels/{novel_id}/"

    try:
        response = requests.get(novel_service_url)
        response.raise_for_status()  # 如果响应状态码不是200，抛出HTTPError异常

        # 返回响应的JSON数据
        return response.json()

    except requests.exceptions.RequestException as e:
        # 处理请求异常并打印错误信息
        print(f"An error occurred while fetching novel info: {e}")
        return None


def get_chapter(chapter_id):
    try:
        response = requests.get(f'http://127.0.0.1:8001/chapters/chapters/{chapter_id}/')
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching chapter data: {e}")
        return {"title": "Unknown"}

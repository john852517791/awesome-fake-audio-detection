from serpapi.google_search import GoogleSearch
import datetime

# 你的 SerpApi Key
API_KEY = "YOUR_SERPAPI_KEY"

# 将关键词组合成 OR 逻辑（Scholar 搜索支持 OR 语法）
keywords = [
    "deepfake speech detection", "audio deepfake", "deepfake audio",
    "fake audio detection", "fake speech detection", "fake music detection",
    "Speech Deepfake Detection", "music deepfake detection", "music antispoof",
    "audio antispoof", "speech antispoof", "speech spoofing detection",
    "audio spoofing detection", "music spoofing detection", "SingFake Detection",
    "Sound Deepfake Detection", "Speech Deception Detection", "Audio Deception Detection",
    "Music Deception Detection"
]

# 示例：我们取前几个作为演示查询
query = " OR ".join([f'"{k}"' for k in keywords[:5]]) 

params = {
    "api_key": API_KEY,
    "engine": "google_scholar",
    "q": query,
    "hl": "en",
    "as_ylo": "2026", # 2026年
    "scisbd": "2",    # 强制按日期排序，获取最新收录
}

search = GoogleSearch(params)
results = search.get_dict()

# 提取并打印近一周的论文
if "organic_results" in results:
    for result in results["organic_results"]:
        title = result.get("title")
        link = result.get("link")
        snippet = result.get("publication_info", {}).get("summary", "No summary")
        print(f"Title: {title}\nLink: {link}\nInfo: {snippet}\n{'-'*50}")
else:
    print("本周暂无相关新论文更新。")

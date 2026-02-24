import arxiv
import json
import datetime
import os
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_weekly_deepfake_papers():
    # 1. 计算时间窗口：获取 7 天前的日期

    new_papers = []
    seen_ids = set() # 用于单次抓取内部去重
    now = datetime.datetime.now(datetime.timezone.utc)
    last_week = now - datetime.timedelta(days=360)
    # print(last_week)
    keywords = [
        "deepfake speech detection",
        "audio deepfake",
        "deepfake audio",
        "fake audio",
        "Speech Deepfake Detection",
        "music deepfake detection",
        "music antispoof",
        "audio antispoof",
        "speech antispoof",
        "SingFake Detection",
        "Sound Deepfake Detection",
    ]
    # 2. 构建搜索查询
    # ti: 标题搜索，abs: 摘要搜索
    for ele in keywords:
        query = f'(ti:"{ele}" OR abs:"{ele}")'
        client = arxiv.Client()
        search = arxiv.Search(
            query = query,
            max_results = 500,
            sort_by = arxiv.SortCriterion.SubmittedDate
        )

        logging.info(f"开始抓取{ele}相关的自 {last_week.date()} 以来的论文...")
        
        for index,result in enumerate(client.results(search)):
            print(index,":::",result)
            # 3. 筛选过去一周内的论文
            if result.published >= last_week:
                paper_id = result.get_short_id()
                if paper_id not in seen_ids:
                    paper_info = {
                        "title": result.title.replace('\n', ' '),
                        "first_author": result.authors[0].name,
                        "url": result.entry_id,
                        "id": paper_id,
                        "published": result.published.strftime("%Y-%m-%d")
                    }
                    new_papers.append(paper_info)
                    seen_ids.add(paper_id)
            else:
                break

    return new_papers

def save_to_jsonl(papers, filename="papers.jsonl"):
    # 4. 去重并保存到 JSONL
    # 读取旧数据用于跨次运行去重
    existing_ids = set()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                existing_ids.add(json.loads(line)['id'])

    with open(filename, 'a', encoding='utf-8') as f:
        for p in papers:
            if p['id'] not in existing_ids:
                f.write(json.dumps(p, ensure_ascii=False) + "\n")
                existing_ids.add(p['id'])

def update_readme(jsonl_file, readme_file="README.md"):
    # 5. 转为 Markdown 格式
    papers = []
    if os.path.exists(jsonl_file):
        with open(jsonl_file, 'r', encoding='utf-8') as f:
            for line in f:
                papers.append(json.loads(line))

    # 按发布时间倒序排列
    papers.sort(key=lambda x: x['published'], reverse=True)

    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write("# Deepfake Speech Detection Papers\n\n")
        f.write(f"> 最后更新时间: {datetime.datetime.now().strftime('%Y-%m-%d')}\n\n")
        f.write("| 发布日期 | 文章名 | 第一作者 | 链接 |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        for p in papers:
            f.write(f"| {p['published']} | **{p['title']}** | {p['first_author']} | [arXiv]({p['url']}) |\n")

if __name__ == "__main__":
    # 执行流程
    papers = get_weekly_deepfake_papers()
    if papers:
        save_to_jsonl(papers,"temp/papers.jsonl")
        update_readme("temp/papers.jsonl")
        logging.info(f"成功更新 {len(papers)} 篇新论文。")
    else:
        logging.info("未发现相关新论文。")
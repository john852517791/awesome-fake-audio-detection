import arxiv
import json
import datetime
import os
import logging
import re

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_weekly_deepfake_papers():
    # 1. 计算时间窗口：获取 7 天前的日期

    new_papers = []
    seen_ids = set() # 用于单次抓取内部去重
    now = datetime.datetime.now(datetime.timezone.utc)
    last_week = now - datetime.timedelta(days=100)
    # print(last_week)
    keywords = [
        "deepfake speech detection",
        "audio deepfake",
        "deepfake audio",
        "fake audio detection",
        "fake speech detection",
        "fake music detection",
        "Speech Deepfake Detection",
        "music deepfake detection",
        "music antispoof",
        "audio antispoof",
        "speech antispoof",
        "speech spoofing detection",
        "audio spoofing detection",
        "music spoofing detection",
        "SingFake Detection",
        "Sound Deepfake Detection",
        "Speech Deception Detection",
        "Audio Deception Detection",
        "Music Deception Detection",
        # "speech language model",
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

def get_paper_key(paper):
    paper_id = str(paper.get('id', '')).strip()
    if paper_id:
        return re.sub(r'v\d+$', '', paper_id)
    return paper.get('url') or paper.get('title')

def get_arxiv_version(paper):
    paper_id = str(paper.get('id', ''))
    match = re.search(r'v(\d+)$', paper_id)
    return int(match.group(1)) if match else 0

def deduplicate_papers(papers):
    unique_papers = {}
    for paper in papers:
        paper_key = get_paper_key(paper)
        if not paper_key:
            continue

        existing_paper = unique_papers.get(paper_key)
        if existing_paper is None or get_arxiv_version(paper) > get_arxiv_version(existing_paper):
            unique_papers[paper_key] = paper

    return list(unique_papers.values())

def load_jsonl_papers(filename):
    papers = []
    if not os.path.exists(filename):
        return papers

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                papers.append(json.loads(line))

    return papers

def write_jsonl_papers(papers, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for paper in papers:
            f.write(json.dumps(paper, ensure_ascii=False) + "\n")

def save_to_jsonl(papers, filename="papers.jsonl"):
    # 4. 去重并保存到 JSONL
    # 读取旧数据并重写文件，清理历史重复项和跨版本重复项
    all_papers = load_jsonl_papers(filename) + papers
    unique_papers = deduplicate_papers(all_papers)
    write_jsonl_papers(unique_papers, filename)

def update_readme(jsonl_file, readme_file="README.md"):
    # 5. 转为 Markdown 格式
    papers = deduplicate_papers(load_jsonl_papers(jsonl_file))

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
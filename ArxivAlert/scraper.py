import arxiv
import json
from datetime import datetime, timedelta

def fetch_arxiv_data(query, days, max_results):
    # 构建默认的 API 客户端。
    client = arxiv.Client()

    # 获取指定天数前的日期
    start_date = datetime.now() - timedelta(days=days)

    # 创建搜索对象
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    results = client.results(search)

    # 用于存储检索到的数据
    data_list = []
    count = 0

    # 逐个迭代检索结果
    for r in results:
        # 检测日期
        if r.updated.date() >= start_date.date():
            entry = {
                "序号": count,
                "标题": r.title,
                "链接": [link.href for link in r.links][0],
                "作者": [author.name for author in r.authors],
                "摘要": r.summary,
                "分类": r.categories,
                "补充信息": r.comment,
                "日期": r.updated.isoformat(),
            }
            data_list.append(entry)
            count += 1
        else:
            # 一旦遇到在限定日期之前的文章，停止检索
            break

    return data_list

if __name__ == "__main__":
    # 指定分类
    # categories = ["cs.CL", "cs.CV", "cs.AI"]
    categories = ["cs.CL"]
    all_data = []

    # 遍历每个分类并检索数据
    for category in categories:
        results = fetch_arxiv_data(query=f"cat:{category}", days=1, max_results=50)
        all_data.extend(results)

    # 将数据写入 JSON 文件
    with open('data/arxiv_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(all_data, json_file, ensure_ascii=False, indent=4)

    print(f"检索到 {len(all_data)} 篇文章，已保存到 data/arxiv_data.json")

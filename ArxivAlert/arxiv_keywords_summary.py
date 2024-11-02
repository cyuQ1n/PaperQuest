import os
import json
import argparse
from datetime import datetime
from scraper import fetch_arxiv_data  
from process import process_papers_in_threads  

def main(keywords, days=1000, max_results=200):
    
    # 获取今天的日期
    today_date = datetime.now().strftime("%Y-%m-%d")
    # 创建data目录
    data_dir = os.path.join('data', today_date)
    os.makedirs(data_dir, exist_ok=True)
    keywords = keywords.replace(" ","")
    # 获取初始数据
    print(f"正在检索 {days} 天内的 {keywords} 类论文...")
    papers = fetch_arxiv_data(query=keywords, days=days, max_results=max_results)

    print(f"共检索到 {len(papers)} 篇论文，开始处理...")
    
    # 处理论文数据
    processed_papers = process_papers_in_threads(papers)

    # 输出结果到对应的JSON文件
    output_file = os.path.join(data_dir, f"{keywords}.json")
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(processed_papers, json_file, ensure_ascii=False, indent=4)

    print(f"处理完成，共生成 {len(processed_papers)} 篇论文的信息，已保存到 {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Arxiv Keywords Paper Summary')
    parser.add_argument('--keywords', required=True, help='检索的关键词，例如 SQL、Ensemble Learning 等')
    parser.add_argument('--days', type=int, default=1000, help='距今天数（默认为1000天）')
    parser.add_argument('--max_results', type=int, default=200, help='最大检索数量（默认为200）')

    args = parser.parse_args()
    
    # 执行主程序
    main(args.keywords, args.days, args.max_results)

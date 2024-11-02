from scholarly import scholarly
import concurrent.futures

# 引用计数函数
def get_citation_count(title):
    try:
        search_query = scholarly.search_single_pub(title)
        return search_query['num_citations'], search_query
    except Exception as e:
        print(f"Error retrieving citation count for '{title}': {e}")
        return -1, {}

# 多线程获取引用计数
def fetch_citation_counts(titles):
    citation_data = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # 为每个标题提交任务
        future_to_title = {executor.submit(get_citation_count, title): title for title in titles}

        for future in concurrent.futures.as_completed(future_to_title):
            title = future_to_title[future]
            try:
                citation_count, citation_info = future.result()
                citation_data.append({
                    "标题": title,
                    "引用计数": citation_count,
                    "引用信息": citation_info
                })
            except Exception as e:
                print(f"Error processing title '{title}': {e}")
                citation_data.append({
                    "标题": title,
                    "引用计数": -1,
                    "引用信息": {}
                })

    return citation_data

if __name__ == "__main__":
    # 示例标题列表
    titles = ["Teaching Embodied Reinforcement Learning Agents: Informativeness and Diversity of Language Use", "P-Masking: Power Law Masking Improves Multi-attribute Controlled Generation", "Length-Induced Embedding Collapse in Transformer-based Models"]
    
    # 获取引用信息
    citation_results = fetch_citation_counts(titles)
    
    # 打印结果
    for result in citation_results:
        print(result)

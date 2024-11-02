import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from template import overview_prompt_template,translation_prompt_template
from llm_utils import call_llm

def process_paper(paper):
    information = f"标题: {paper['标题']};\n摘要: {paper['摘要']}"
    # 生成概述
    overview_prompt = overview_prompt_template.format(information=information)
    overview = call_llm(overview_prompt)
    
    # 翻译摘要
    translation_prompt = translation_prompt_template.format(abstract=paper['摘要'])
    translated_abstract = call_llm(translation_prompt)
    
    # 使用 update 方法更新字典
    paper.update({
        '概述': overview,
        '摘要译文': translated_abstract
    })
    
    return paper

def process_papers_in_threads(papers):
    processed_papers = []
    
    # 使用 ThreadPoolExecutor 创建一个线程池
    with ThreadPoolExecutor(max_workers=5) as executor:
        # 提交所有的论文处理任务
        future_to_paper = {executor.submit(process_paper, paper): paper for paper in papers}
        
        # 收集处理结果
        for future in as_completed(future_to_paper):
            paper = future_to_paper[future]
            try:
                processed_paper = future.result()
                processed_papers.append(processed_paper)
            except Exception as e:
                print(f"处理论文 {paper['标题']} 时发生错误: {e}")
    
    return processed_papers

if __name__ == "__main__":
    # 参考样例
    paper_list = [
        {
        "序号": 9,
        "标题": "Redefining <Creative> in Dictionary: Towards a Enhanced Semantic Understanding of Creative Generation",
        "链接": "http://arxiv.org/abs/2410.24160v1",
        "作者": [
            "Fu Feng",
            "Yucheng Xie",
            "Jing Wang",
            "Xin Geng"
        ],
        "摘要": "Creativity, both in human and diffusion models, remains an inherently\nabstract concept; thus, simply adding \"creative\" to a prompt does not yield\nreliable semantic recognition by the model. In this work, we concretize the\nabstract notion of \"creative\" through the TP2O task, which aims to merge two\nunrelated concepts, and introduce CreTok, redefining \"creative\" as the token\n$\\texttt{<CreTok>}$. This redefinition offers a more concrete and universally\nadaptable representation for concept blending. This redefinition occurs\ncontinuously, involving the repeated random sampling of text pairs with\ndifferent concepts and optimizing cosine similarity between target and constant\nprompts. This approach enables $\\texttt{<CreTok>}$ to learn a method for\ncreative concept fusion. Extensive experiments demonstrate that the creative\ncapability enabled by $\\texttt{<CreTok>}$ substantially surpasses recent SOTA\ndiffusion models and achieves superior creative generation. CreTok exhibits\ngreater flexibility and reduced time overhead, as $\\texttt{<CreTok>}$ can\nfunction as a universal token for any concept, facilitating creative generation\nwithout retraining.",
        "分类": [
            "cs.CV",
            "cs.CL"
        ],
        "补充信息": None,
        "日期": "2024-10-31T17:19:03+00:00"
    }
    ]

    # 处理论文
    processed_data = process_papers_in_threads(paper_list)

    # 将结果写入 JSON 文件
    with open('data/processed_arxiv_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(processed_data, json_file, ensure_ascii=False, indent=4)

    print(f"处理完成，共生成 {len(processed_data)} 篇论文的信息，已保存到 processed_arxiv_data.json")

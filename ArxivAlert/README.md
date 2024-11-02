# ArxivAlert 📬

**ArxivAlert** is the first tool in the **PaperQuest** suite, designed to keep researchers up-to-date with the latest papers from Arxiv. With ArxivAlert, you can automatically retrieve daily or keyword-specific papers, summarize them, and even get citation counts. It's the perfect assistant for staying informed on cutting-edge research!

## Features 🌟

- **Daily Paper Summaries**: Get a daily list of the latest papers based on your chosen categories.
- **Keyword-Based Searches**: Specify keywords to retrieve papers matching your research interests.
- **Email Notifications**: Receive formatted email summaries directly in your inbox (optional configuration).
- **Citation Counts**: Retrieve citation counts for papers via the `cititions.py` module.

## Directory Structure 📁

```plaintext
PaperQuest/
└── ArxivAlert/
    ├── arxiv_daily_summary.py       # Retrieve daily papers based on category
    ├── arxiv_keywords_summary.py    # Retrieve papers based on keywords
    ├── citations.py                 # Fetch citation counts for papers
    ├── config.py                    # Configuration file for LLM and API keys
    ├── daily_arxiv.py               # Format and email daily paper summaries
    ├── llm_utils.py                 # Helper functions to interact with language models
    ├── process.py                   # Processes papers to generate summaries and translations
    ├── scraper.py                   # Core Arxiv data fetching functionality
    ├── template.py                  # Templates for prompts (summaries, translations)
    └── requirements.txt             # List of dependencies
```

## Installation 🔧

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/PaperQuest.git
   cd PaperQuest/ArxivAlert
   ```

2. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Settings**:
   - Update `config.py` with your OpenAI API key and base URL.
   - Optionally, configure email settings in `daily_arxiv.py` for sending summaries.

## Usage 🚀

### 1. Daily Paper Summaries by Category
Fetch the latest papers in a specific category (e.g., `cs.AI`) from Arxiv.

```bash
python arxiv_daily_summary.py --category "cs.AI" --days 1 --max_results 50
```

### 2. Paper Summaries by Keywords
Retrieve papers based on specific keywords (e.g., "Machine Learning").

```bash
python arxiv_keywords_summary.py --keywords "Machine Learning" --days 7 --max_results 100
```

### 3. Get Citation Counts
Fetch citation counts for a list of paper titles.

```bash
python citations.py
```

### 4. Email Daily Summaries
Send daily summaries directly to your email.

```bash
python daily_arxiv.py
```

## Modules 📑

- **arxiv_daily_summary.py**: Retrieves and saves daily Arxiv papers in JSON format.
- **arxiv_keywords_summary.py**: Searches and saves papers based on keywords.
- **citations.py**: Retrieves citation counts using Google Scholar API.
- **scraper.py**: Core data-fetching module for Arxiv.
- **process.py**: Processes and formats paper summaries using language models.
- **template.py**: Contains prompt templates for generating summaries and translations.

## Example Output 🎉

Sample output for a daily paper summary:

```plaintext
# 每日论文速递 - 2024-10-31
以下是今日检索到的论文摘要及相关信息：

## Teaching Embodied Reinforcement Learning Agents
- **作者**: Jiajun Xi, Yinong He, Jianing Yang, Yinpei Dai, Joyce Chai
- **日期**: 2024-10-31
- **分类**: cs.CL, cs.AI
- **概述**: 本文研究了语言多样性在增强学习代理中的作用，发现在多样化语言反馈下代理更易适应新任务。
- **摘要**: 本文提出一种新的实体代理学习方法，强调语言多样性在学习中的重要性...

```

## Contribution 🎉
We welcome feedback and contributions!

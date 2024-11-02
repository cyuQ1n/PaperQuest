# 概述生成模板
overview_prompt_template = """请仔细分析下面文章的信息，然后用100字左右的中文概述这项工作。
文章信息如下：
{information}
- 注意：
1) 概述中需要阐述论文研究的动机、解决的问题、方法、结果等内容。
"""

# 摘要翻译模板
translation_prompt_template = """请将下面的摘要翻译成中文：
{abstract}
- 注意：仅输出翻译后的文本
"""
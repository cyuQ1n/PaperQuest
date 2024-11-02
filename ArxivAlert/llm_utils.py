# llm_utils.py

import json
import re
from openai import OpenAI
from config import model_name, openai_api_key, openai_api_base

# 初始化 OpenAI 客户端
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

def call_llm(prompt):
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content

def extract_json(llm_response: str) -> dict:
    try:
        json_content = re.findall(r"```json(.*?)```", llm_response, re.DOTALL)
        if not json_content:
            raise ValueError("No JSON content found within the markdown code block.")
        json_str = json_content[0].strip()
        return json.loads(json_str)
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Error! 解析失败: {str(e)}")
        return None
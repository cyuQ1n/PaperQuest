import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Markdown格式输出
def parse_paper_to_markdown(papers):
    markdown_lines = []

    # 添加标题
    markdown_lines.append("# 每日论文速递 - {}".format(datetime.now().strftime("%Y-%m-%d")))
    markdown_lines.append("\n以下是今日检索到的论文摘要及相关信息：\n")

    for paper in papers:
        # 添加论文信息
        markdown_lines.append("## {} [{}]({})".format(paper["标题"], paper["作者"][0], paper["链接"]))
        markdown_lines.append("- **作者**: {}".format(", ".join(paper["作者"])))
        markdown_lines.append("- **日期**: {}".format(paper["日期"].split("T")[0]))
        markdown_lines.append("- **分类**: {}".format(", ".join(paper["分类"])))
        markdown_lines.append("- **概述**: \n  > {}".format(paper["概述"]))
        markdown_lines.append("- **摘要**: \n  > {}".format(paper["摘要译文"]))
        markdown_lines.append("\n---\n")

    return "\n".join(markdown_lines)

# 邮件发送函数
def send_email(subject, body, recipient_email):
    # 配置邮件服务器
    smtp_server = 'smtp.gmail.com'  # Gmail的SMTP服务器
    smtp_port = 587  # TLS端口
    sender_email = 'your_mail'  # 替换为您的Gmail地址
    sender_password = 'your_password'  # 使用生成的应用密码


    # 创建邮件
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # 添加邮件正文
    msg.attach(MIMEText(body, 'plain'))

    # 发送邮件
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # 启用TLS
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("邮件发送成功！")
    except Exception as e:
        print(f"发送邮件时出错: {e}")

# 格式化邮件内容
def format_email_content(data): 
    body = parse_paper_to_markdown(data)
    print(body)
    return body


if __name__ == "__main__":
    # 示例数据
    data = [
    {
        "序号": 3,
        "标题": "Multi-Attribute Linguistic Tuning for Controlled Paraphrase Generation",
        "链接": "http://arxiv.org/abs/2410.24199v1",
        "作者": [
            "Mohamed Elgaar",
            "Hadi Amiri"
        ],
        "摘要": "We present a novel approach to paraphrase generation that enables precise\ncontrol and fine-tuning of 40 linguistic attributes for English. Our model is\nan encoder-decoder architecture that takes as input a source sentence and\ndesired linguistic attributes, and produces paraphrases of the source that\nsatisfy the desired attributes. To guarantee high-quality outputs at inference\ntime, our method is equipped with a quality control mechanism that gradually\nadjusts the embedding of linguistic attributes to find the nearest and most\nattainable configuration of desired attributes for paraphrase generation. We\nevaluate the effectiveness of our method by comparing it to recent controllable\ngeneration models. Experimental results demonstrate that the proposed model\noutperforms baselines in generating paraphrases that satisfy desired linguistic\nattributes.",
        "分类": [
            "cs.CL"
        ],
        "补充信息": None,
        "日期": "2024-10-31T17:55:27+00:00",
        "概述": "该研究提出了一种新的多属性语义调整方法，旨在生成具有精准控制的英语同义句。研究采用编码-解码架构，输入源句子和所需的语言属性，生成符合要求的同义句。方法中引入质量控制机制，确保生成高质量的同义句。实验表明，该模型在生成满足需求语言属性的同义句方面优于现有可控生成模型。",
        "摘要译文": "我们提出了一种新颖的同义句生成方法，能够精确控制和调整40种语言属性以适用于英语。我们的模型采用了编码器-解码器架构，输入为源句子和所需的语言属性，输出满足所需属性的同义句。为确保推理时生成高质量的输出，我们的方法配备了一种质量控制机制，该机制逐步调整语言属性的嵌入，以找到最接近且最容易实现的目标属性配置，用于同义句生成。我们通过将该方法与近期可控生成模型进行比较来评估其有效性。实验结果表明，所提出模型在生成满足所需语言属性的同义句方面优于基线模型。"
    },
    {
        "序号": 0,
        "标题": "Teaching Embodied Reinforcement Learning Agents: Informativeness and Diversity of Language Use",
        "链接": "http://arxiv.org/abs/2410.24218v1",
        "作者": [
            "Jiajun Xi",
            "Yinong He",
            "Jianing Yang",
            "Yinpei Dai",
            "Joyce Chai"
        ],
        "摘要": "In real-world scenarios, it is desirable for embodied agents to have the\nability to leverage human language to gain explicit or implicit knowledge for\nlearning tasks. Despite recent progress, most previous approaches adopt simple\nlow-level instructions as language inputs, which may not reflect natural human\ncommunication. It's not clear how to incorporate rich language use to\nfacilitate task learning. To address this question, this paper studies\ndifferent types of language inputs in facilitating reinforcement learning (RL)\nembodied agents. More specifically, we examine how different levels of language\ninformativeness (i.e., feedback on past behaviors and future guidance) and\ndiversity (i.e., variation of language expressions) impact agent learning and\ninference. Our empirical results based on four RL benchmarks demonstrate that\nagents trained with diverse and informative language feedback can achieve\nenhanced generalization and fast adaptation to new tasks. These findings\nhighlight the pivotal role of language use in teaching embodied agents new\ntasks in an open world. Project website:\nhttps://github.com/sled-group/Teachable_RL",
        "分类": [
            "cs.CL",
            "cs.AI",
            "cs.CV",
            "cs.LG",
            "cs.RO"
        ],
        "补充信息": "EMNLP 2024 Main. Project website:\n  https://github.com/sled-group/Teachable_RL",
        "日期": "2024-10-31T17:59:52+00:00",
        "概述": "本文旨在通过研究不同类型的语言输入，探讨其如何优化基于强化学习的实体代理的学习和推理能力。研究动机在于现有方法多采用简单低级指令，未能充分利用自然语言的丰富性。研究通过分析语言反馈的详尽度（包括对过去行为的反馈和未来指导）和多样性（语言表达的变异性）对代理学习的影响，发现在四个强化学习基准上，接受多样且详尽语言反馈的代理表现出更好的泛化能力和更快的新任务适应速度。",
        "摘要译文": "在现实世界的应用场景中，希望具备实体能力的代理能够利用人类语言来获得显式的或隐含的知识，从而辅助学习任务。尽管近期取得了进展，但大多数之前的方法采用简单的低级指令作为语言输入，这可能无法反映自然的人类交流方式。尚不清楚如何整合丰富的语言使用来促进任务学习。为了解决这一问题，本文研究了不同类型的语言输入如何在增强学习（RL）实体代理方面起促进作用。更具体地说，我们考察了不同语言信息量（即对过去行为的反馈和未来指导）和多样性（即语言表达的变化）如何影响代理学习和推理。基于四个RL基准的实证结果表明，用多样化和信息丰富的语言反馈训练的代理可以实现更好的泛化和快速适应新任务的能力。这些发现强调了在开放环境下通过语言使用向实体代理教授新任务的关键作用。项目网址：\nhttps://github.com/sled-group/Teachable_RL"
    }
]

    # 发送邮件
    subject = "arXiv论文速递"
    recipient_email = "XXXXX@163.com"  # 替换为接收者的邮箱
    email_body = format_email_content(data)
    send_email(subject, email_body, recipient_email)

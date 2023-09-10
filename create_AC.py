from flask import Flask, render_template, request
import openai
import requests

app = Flask(__name__)

"用来写用户故事标题&验收标准"
# OpenAI API 访问凭证
openai.api_key = '请输入你的OpenAI Key'

# 根据用户输入生成用户故事标题和用户故事验收标准
def generate_user_story(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # 可以选择 GPT-3.5 或 GPT-4.0 引擎
        prompt=prompt,
        max_tokens=2000,
        n=1,
        stop=None,
        timeout=600,
        temperature=0.8
    )
    return response.choices[0].text.strip()


# Flask 路由和视图函数
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])# 这里是输入
def generate():
    background = request.form['product_background']
    requirements = request.form['requirement_description']
    prompt_general = '假设你是一个资深的产品经理，请你根据我的给出的产品概述和用户需求简述，帮我写出用户故事的标题和用户故事的验收标准(每个用户故事的验收标准数量应在5条之内)。\n用户故事标题的基本构成的是：{作为什么用户或者系统角色(Who)，我想要进行什么活动(What)，以便实现什么价值 (Why)。}\n用户故事的验收标准的定义是：验收标准(AC)是要从用户验收的视角出发，由一条条可验证的且相互独立的规则组成，内容: 用户使用系统时的各种场景\nAC是Acceptance Criteria的缩写，即验收准则。每条验收标准以字母AC+一个序数+冒号开始。\nGiven：前提条件，即在执行这个用户故事之前需要满足的条件，或者使用场景。\nwhen：触发时机，描述用户执行操作或触发事件的步骤。\nThen：期望结果，描述用户预期看到的结果或系统行为。\n'
    Prompt_input = f"产品概述：{background}\n用户需求描述：{requirements}\n"
    output_prompt = "我希望你的标准输出内容形式是:\n用户故事标题：作为什么角色的用户,我想要进行什么活动,以便于实现什么价值 。\nAC+ 序数：\nGiven：前提条件，即在执行这个用户故事之前需要满足的条件，或者使用场景。\nwhen：触发时机，描述用户执行操作或触发事件的步骤。\nThen：期望结果，描述用户预期看到的结果或系统行为。\n...\n每条AC下只有一组Given、When、Then。请按以上内容形式输出！谢谢！\n"
    acceptance_criteria = generate_user_story(prompt_general + Prompt_input + output_prompt)
    # print(acceptance_criteria)# 打印一个输出结果

    return render_template('index.html', acceptance_criteria=acceptance_criteria)


if __name__ == '__main__':
    app.run(debug=True)

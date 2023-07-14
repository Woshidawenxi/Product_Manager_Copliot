from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# OpenAI API 访问凭证
openai.api_key = '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'


# 根据用户输入生成用户故事标题和用户故事验收标准
def generate_user_story(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # 可以选择 GPT-3.5 或 GPT-4.0 引擎
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8
    )
    return response.choices[0].text.strip()


# Flask 路由和视图函数
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    background = request.form['background']
    scenario = request.form['scenario']
    requirements = request.form['requirements']

    user_story_prompt = f"产品背景：{background}\n业务场景：{scenario}\n需求简述：{requirements}\n\n生成用户故事标题：[作为什么角色(Who),要进行什么活动(What),才能实现什么商业价值 (Why)]"
    acceptance_criteria_prompt = "生成用户故事的验收标准 (AC)：\n【Given】 (发生场景，在什么样的情景或条件下)\n【When】 (触发时机，做了什么操作，采取了什么行动)\n【Then】 (期望结果，得到了什么结果)"

    user_story_title = generate_user_story(user_story_prompt)
    acceptance_criteria = generate_user_story(acceptance_criteria_prompt)
    print(acceptance_criteria)
    return render_template('result.html', user_story_title=user_story_title, acceptance_criteria=acceptance_criteria)


if __name__ == '__main__':
    app.run(debug=True)

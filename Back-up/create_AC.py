from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# OpenAI API 访问凭证
openai.api_key = ''

# Flask 路由和视图函数
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    # 获取用户输入
    openai_key = request.form['openai_key']
    background = request.form['background']
    scenario = request.form['scenario']
    requirements = request.form['requirements']

    # 设置 OpenAI API 访问凭证
    openai.api_key = openai_key

    # 根据用户输入生成用户故事标题和用户故事验收标准
    user_story_prompt = f"产品背景：{background}\n业务场景：{scenario}\n需求简述：{requirements}\n\n生成用户故事标题：[作为什么角色(Who),要进行什么活动(What),才能实现什么商业价值 (Why)]"
    acceptance_criteria_prompt = "生成用户故事的验收标准 (AC)：\n【Given】 (发生场景，在什么样的情景或条件下)\n【When】 (触发时机，做了什么操作，采取了什么行动)\n【Then】 (期望结果，得到了什么结果)"

    response_user_story = openai.Completion.create(
        engine='text-davinci-003',
        prompt=user_story_prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8
    )
    user_story_title = response_user_story.choices[0].text.strip()

    response_acceptance_criteria = openai.Completion.create(
        engine='text-davinci-003',
        prompt=acceptance_criteria_prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8
    )
    acceptance_criteria = response_acceptance_criteria.choices[0].text.strip()

    return render_template('result.html', user_story_title=user_story_title, acceptance_criteria=acceptance_criteria)


if __name__ == '__main__':
    app.run(debug=True)

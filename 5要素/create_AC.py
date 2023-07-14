from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# 设置 OpenAI API 密钥
openai.api_key = 'YOUR_OPENAI_API_KEY'

# 根据用户输入调用 OpenAI API 生成 Epic 的五要素分析
def generate_epic_analysis(product_info, user_info, scenario_description):
    # 构建输入文本
    prompt = f"产品名称及介绍：{product_info}\n产品用户：{user_info}\n业务场景：{scenario_description}\n"

    # 调用 OpenAI API 生成 Epic 的五要素分析
    response = openai.Completion.create(
        engine='text-davinci-003',  # 根据实际情况选择合适的模型引擎
        prompt=prompt,
        max_tokens=300,  # 根据需要调整生成的文本长度
        n=1,  # 生成一个回答
        stop=None,  # 不设置停止条件，生成完整的回答
        temperature=0.7  # 根据需要调整生成文本的创造力，范围从0.2到1.0
    )

    # 提取生成的 Epic 五要素分析
    epic_analysis = response.choices[0].text.strip()

    return epic_analysis

# 定义主页路由
@app.route('/')
def home():
    return render_template('index.html')

# 定义生成 Epic 五要素分析的路由
@app.route('/generate_epic_analysis', methods=['POST'])
def generate_epic_analysis_route():
    product_info = request.form['product_info']
    user_info = request.form['user_info']
    scenario_description = request.form['scenario_description']

    epic_analysis = generate_epic_analysis(product_info, user_info, scenario_description)

    return render_template('index.html', epic_analysis=epic_analysis)

if __name__ == '__main__':
    app.run(debug=True)

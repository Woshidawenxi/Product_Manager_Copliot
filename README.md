# AI产品助手
<br>  在AI大预言模型时代，AI产品助手是一个致力于通过应用大语言模型来协助产品经理完成日常工作，提升产品经理的工作效率的独立开发项目。开发者是一个半路出家的产品经理，写过一些简单的代码，项目本身也是在LLM的协助下逐步推进的，欢迎大家试用并给出反馈。本项目聚焦于赋能产品经理日常的文字工作，如敏捷故事验收、prd、brd、mrd书写等场景。逐步完成这些场景的赋能。
用户故事及验收标准 - create_AC
<br>  敏捷开发是一种常见的软件开发迭代方式，敏捷开发以其快速调整的灵活性&适应性、开发过程中客户参与度高、可以持续交付价值等优势获得了大多数公司的青睐。在敏捷开发中，产品经理需要处理的日常工作主要包括：市场调研、产品愿景和战略梳理、需求管理、用户故事&验收标准编写、开发迭代管理&验收、用户反馈迭代等多个任务。其中占据大量时间的工作是：用户故事&验收标准编写，这部分需要严格遵循用户故事&验收标准的“八股文”格式，占据大量的时间在机械性工作上。
针对这样的现状，我们设计了一种基于产品背景概述和用户需求作为输入，快速生成符合敏捷开发要求的用户故事标题和用户故事验收标准的生成式AI应用插件-AI产品助手。
# 环境准备
python     3.11<br>
flask   2.3.3<br>
openai 0.27.10<br>
# 使用教程
<br>  访问：[https://github.com/Woshidawenxi/AI_Product_Manager--Based-on-GPT-api-](https://github.com/Woshidawenxi/Product_Manager_Copliot)
<br>  **1.下载程序包**
<br>  ![1](https://github.com/Woshidawenxi/Product_Manager_Copliot/assets/72373043/c6ee37ef-dafc-492e-bcc2-7a88817e8268)
<br>  **2.打开"create_AC.py"，添加Openai_key**
<br>  ![2](https://github.com/Woshidawenxi/Product_Manager_Copliot/assets/72373043/315931d5-e051-45a1-947b-1cad255149bc)
<br>  **3.运行程序，点击地址，跳转到用户页面**
<br>  ![3](https://github.com/Woshidawenxi/Product_Manager_Copliot/assets/72373043/87325f08-33bb-459d-9aa1-9a26974f0017)
<br>  **4.页面输入框中会给出一个产品概述的提示和一个用户产品需求的描述的示例，根据示例修改适应您产品的内容。**
<br>  ![4](https://github.com/Woshidawenxi/Product_Manager_Copliot/assets/72373043/f161060c-9ea5-4b50-9038-0b9ba73e6336)
<br>  **5.点击生成，对应的答案将生成在故事验收标准处。**
<br>  ![5](https://github.com/Woshidawenxi/Product_Manager_Copliot/assets/72373043/e260f34d-dbc8-49c0-b853-9b22f03e6b2c)
<br>  返回的用户故事标题及验收标准如下：
<br>  用户故事标题：作为产品经理，我想要使用AI产品助手输入产品背景描述和用户需求描述，以便于自动生成高质量的用户故事标题和验收标准。
<br>  AC1: 
<br>    Given: 产品经理输入正确的产品背景描述和用户需求描述
<br>    When: 产品经理点击“生成故事”按钮
<br>    Then: AI产品助手正确生成用户故事标题
<br>  AC2: 
<br>    Given: 产品经理输入正确的产品背景描述和用户需求描述
<br>    When: 产品经理点击“生成故事”按钮
<br>    Then: AI产品助手正确生成用户故事的验收标准
<br>  AC3: 
<br>    Given: 产品经理输入正确的产品背景描述和用户需求描述
<br>    When: 产品经理点击“生成故事”按钮
<br>    Then: AI产品助手生成的用户故事标题和验收标准数量较多
<br>  AC4: 
<br>    Given: 产品经理输入正确的产品背景描述和用户需求描述
<br>    When: 产品经理点击“生成故事”按钮
<br>    Then: AI产品助手生成的用户故事标题和验收标准内容规范
<br>  AC5: 
<br>    Given: 产品经理输入正确的产品背景描述和用户需求描述
<br>    When: 产品经理点击“生成故事”按钮
<br>    Then: AI产品助手生成的用户故事标题和验收标准格式合理
# 联系我们
<br>  扫码添加社群，欢迎一起交流讨论有关AI的想法。
<br>  ![6](https://github.com/Woshidawenxi/Product_Manager_Copliot/assets/72373043/ad4842ff-ce12-42c0-8543-3c294e77714d)



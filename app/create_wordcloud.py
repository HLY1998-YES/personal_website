from wordcloud import WordCloud
import matplotlib.pyplot as plt

# # 定义关键词
# keywords = [
#     "Python", "Robot Framework", "CAN", "FlexRay", "LIN",
#     "Automatic Testing", "Mechanical Arm", "Screen Control", "Test Cases",
#     "Interface Files", "Algorithms", "Automation", "Equipment", "Execution",
#     "File Management", "Geely", "BMW"
# ]
#
# # 拼接成词云输入文本
# text = " ".join(keywords)
#
# # 生成词云
# wordcloud = WordCloud(width=800, height=400, background_color="white", colormap="viridis").generate(text)
#
# # 保存图片
# image_path = "../static/automatic_testing_wordcloud.png"
# wordcloud.to_file(image_path)
#
# # 显示预览
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()

# # Text for second project: Ring Web Extractor
# text = """
# Python Crawling Framework, Web Crawler, Distributed Cluster, Cloud Task Management,
# XML Scripts, Middleware, Anti-Crawling, Proxy IP, Unit Testing, System Testing,
# Integration Testing, Pressure Testing, JD, Taobao, Meituan, Ele.me, Jingdong,
# Visualized Crawling, Request Scheduling, Pipeline Storage, Crawling Functions
# """
#
# # Generate word cloud
# wordcloud = WordCloud(width=1000, height=600, background_color='white', colormap='plasma').generate(text)
#
# # Save the word cloud image
# image_path = "../static/ring_web_extractor_wordcloud.png"
# wordcloud.to_file(image_path)
#
# # Display the image
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()

# # 定义第三个项目关键词：Social Science Database Platform
# text = """
# social science, database, CNKI, crawling, anti-crawling, law, policy, regulation,
# data cleaning, Chinese news, high-quality papers, verification code, frequency restriction,
# data collection, accuracy, comprehensiveness, auxiliary platform, retrieval, data processing
# """
#
# # 创建词云对象
# wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
#
# # 显示词云图
# plt.figure(figsize=(10, 5))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.tight_layout()
# plt.show()

# 新的、更加突出项目专业性与深度的关键词列表
keywords = [
    "Data Collection", "Custom Scraping", "Public Opinion", "WeChat", "Bilibili", "Twitter", "NetEase",
    "Policy Monitoring", "COVID-19", "Two Sessions", "Phoenix App", "Government Data", "Special Topic Reports",
    "News Crawling", "Information Extraction", "Real-time Data", "Temporary Data Services", "Topic Analysis",
    "Database Support", "Content Aggregation"
]

# 生成词云
text = " ".join(keywords)
wordcloud = WordCloud(width=800, height=400, background_color="white", colormap="plasma").generate(text)

# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout()
plt.show()

# 保存词云图
wordcloud_path = "../static/additional_data_collection_wordcloud.png"
wordcloud.to_file(wordcloud_path)
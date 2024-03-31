from langchain_core.prompts import PromptTemplate

SYSTEM_PROMPT='''Create structured and digestible summaries for YouTube videos, focusing on capturing the main objectives, significant insights, and unique aspects of the video content. These summaries should provide a clear and engaging overview for the reader, incorporating visual elements and structured information to enhance readability and interest.
Markdown File Format Guide:

* 		Emphasize key points with emojis and bold text to add visual interest and clearly distinguish different sections of the summary.
* 		Organize content in a way that makes the summary easy to digest, using bullet points or brief paragraphs under flexible headings tailored to the video's content.
* The headings has to start with emoji 

The below headings are optional and these are just examples. To give you examples on categories of video for structuring the summary, it could be 

Product Reviews
* Optional Headings: 📦 Features, 👍 Pros, 👎 Cons, 🔍 Comparison, 💰 Price, 🙋‍♂️ Personal Experience, 🎯 Recommendation.
Cooking Videos
* Optional Headings: 🥘 Ingredients, 📝 How to Cook, 🍽 Final Presentation.
Vlogs
* Optional Headings: 🌟 Place, Main Events, 💭 Personal Insights, 🚀 Unique Experiences, 💌 Key Messages.
Educational Videos
* Optional Headings: 📚 Main Topic, 📊 Important Facts, 🧠 Concept Explanations, 🖼 Visual Aids, 📝 Summary.
Tutorials
* Optional Headings: 🎯 Objective, 🛠 Step-by-Step Instructions, 📋 Materials, ✅ Tips for Success, ⚠️ Common Mistakes.
Gaming Videos
* Optional Headings: 🎮 Game Played, 🕹 Strategy, 🌟 Highlights, 💬 Commentary, 🎉 Experience.
Tech Reviews
* Optional Headings: 💻 Technical Specifications, 🎨 Design and Usability, ⚡ Performance, 💸 Price Comparison, 🏆 Verdict.
Documentary/Investigative
* Optional Headings: 🎥 Main Topic, 🧐 Background, 🔍 Key Findings, 🗣 Interviews, 📌 Conclusion.
Fitness and Health
* Optional Headings: 💪 Exercise Routines, 🌟 Benefits, 📊 Difficulty Level, 🎯 Target Audience, 🛡 Safety.
Travel Videos
* Optional Headings: ✈️ Destinations, 🏞 Attractions, 🍜 Cultures and Cuisines, 🧳 Travel Tips, ❤️ Personal Experiences.
Productivity
* Optional Headings: 🚀 Techniques, 📈 Efficiency Tools, ⏱ Time Management, 🎯 Goal Setting.
Entrepreneurship Teaching
* Optional Headings: 💼 Business Strategies, 🌱 Growth Tactics, 💡 Startup Insights, 🤝 Networking.
Insightful Advice
* Optional Headings: 💭 Life Lessons, 🌟 Personal Growth, 🔑 Key Principles, 🛣 Path to Success.


Flexible Summary Structure:
For videos that do not fit into conventional categories (Product Reviews, Cooking Videos, etc.), adopt a versatile approach that best captures the video's essence


Adaptive Content Strategy:
* Use flexible headings that best match the video’s content, avoiding limitations imposed by fixed categories.
* Ensure each section adds value to the summary, offering clear, informative insights into the video’s content and significance.
* Highlight engaging elements to draw in the reader, such as surprising facts, emotional moments, or key discoveries.
Summary Tips:
* Exclude non-essential sections, such as purely musical interludes without significant action or content.
* Base summaries on the video transcript and content without incorporating external information, ensuring accuracy and relevance.
* Prioritize clarity and engagement, using structured formatting to make the summary accessible and appealing to a broad audience.

Important Note:
* Respond in markdown format.
* Highlight the heading in bold.
'''

USER_PROMPT='''Here is the transscript:\n{transcript}\nHere is the title: {title}'''

MAP_PROMPT = """Write a concise summary of the following:
"{text}"
CONCISE SUMMARY:
"""
MAP_PROMPT_TEMPLATE = PromptTemplate(template=MAP_PROMPT, input_variables=["text"])

COMBINE_PROMPT = SYSTEM_PROMPT+"""
Here is the transscript:
```{text}```
"""
COMBINE_PROMPT_TEMPLATE = PromptTemplate(template=COMBINE_PROMPT, input_variables=["text"])


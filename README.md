# 🚀 LinkedIn Post Generator  

A **Generative AI-powered tool** that helps LinkedIn influencers and content creators generate posts tailored to their **topics, style, and language preferences**.  

This project uses **LangChain, Llama-3.3-70B, Groq Cloud, and Streamlit** to provide an intuitive UI where users can select topics, length, and language — and instantly get a LinkedIn-style post.

---
## 🔗 Live Demo

Check out the live Streamlit app here: [LinkedIn Post Generator](https://linkedin-post-generator-hsbgnj9hjraguwgpp7encp.streamlit.app/)

---

## ✨ Features  

- ✅ Generate professional **LinkedIn posts** in seconds.  
- ✅ Choose post **length** → Short, Medium, Long.  
- ✅ Select **language** → English or Hinglish.  
- ✅ Uses **few-shot influencer examples** for style-matching.  
- ✅ **Streamlit-based UI** for easy interaction.  
- ✅ Powered by **Groq Cloud** for ultra-fast inference.  

---
## 💡Project Architecture

(https://github.com/prabalpkd/LinkedIn-Post-Generator/blob/main/Project%20Archtecture.png)

---

## ⚙️ Working Structure  

### **1. Preprocessing**  
- Raw posts of renowned LinkedIn influencers are collected.  
- Each post is enriched using an LLM to extract:  
  - **Tags** (topics covered)  
  - **Language** (English/Hinglish)  
  - **Line Count** (for categorizing post length).  
- Enriched posts are stored in a JSON file (`processed_post4.json`).  

### **2. Post Generation**  
- Unique topics, lengths, and languages are extracted from the enriched data.  
- A **Streamlit UI** allows users to select:  
  - Topic  
  - Post Length  
  - Language  
- A **dynamic prompt** is generated and passed to the Llama-3.3 model via Groq Cloud.  
- The LLM outputs a **LinkedIn-style post** tailored to the selections.  

---

## 🛠️ Tech Stack  

- **LangChain** → for prompt orchestration  
- **Llama-3.3-70B Versatile** → large language model for generation  
- **Groq Cloud** → high-speed inference  
- **Streamlit** → real-time user interface  
- **Pandas** → data handling and preprocessing  
- **dotenv** → environment variable management  

---

## 📂 Project Structure  

├── .env                  
├── requirements.txt      # Dependencies
├── main.py               # Streamlit UI
├── post_generator.py     # Prompt builder + post generation
├── few_shot5.py          # Few-shot examples handler
├── llm_helper3.py        # LLM configuration (Groq + LangChain)
├── preprocess2.py        # Preprocessing pipeline
├── data/
│   ├── raw_posts1.json   # Raw influencer posts
│   ├── processed_post4.json # Enriched posts with metadata

##🖥️ Usage

1. Open the Streamlit app in your browser.
2. Choose:

    ● Topic → e.g. AI, Motivation, Career Growth

    ● Post Length → Short, Medium, Long

    ● Language → English or Hinglish

3. Click Generate → The app instantly generates a LinkedIn post.
4. Copy & share your post on LinkedIn 🚀

##🔮 Future Enhancements

●🌍 Multi-language post generation.
●📝 Save user writing styles for consistency.
●📊 Engagement prediction analytics.
●📅 Batch post generation for scheduling.
●🔗 Integration with LinkedIn API for auto-publishing.

## Author:
Prabal Kumar Deka
Future Ready Data Scientist/GenAI Engineer



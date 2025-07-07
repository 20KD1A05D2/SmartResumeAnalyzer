# 🧠 Smart Resume Analyzer + Role Predictor

An AI-powered web app that analyzes `.docx` resumes and predicts the best-fit IT job roles based on the candidate’s skills.

---

## 🚀 Features

- 📄 Upload resume (.docx)
- 🤖 Automatically extracts skills
- 🎯 Predicts top 3 IT job roles using AI (TF-IDF + Cosine Similarity)
- 📈 Match percentage display with colored progress bars
- 📂 Shows uploaded resume name
- 🔁 "Back to Home" navigation
- 🌈 Clean, responsive UI using Bootstrap

---

## 💡 Technologies Used

| Frontend              | Backend         | AI/NLP & Logic                  | Hosting        |
|-----------------------|------------------|----------------------------------|----------------|
| HTML, CSS, Bootstrap  | Python, Flask     | docx2txt, sklearn (TF-IDF + Cosine) | GitHub + Render |

---

## 🛠️ Installation & Running (Localhost)

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/SmartResumeAnalyzer.git
cd SmartResumeAnalyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py

# 4. Visit in browser
http://127.0.0.1:5000

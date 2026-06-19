# 🧠 Adaptive Socratic AI Tutor

> An adaptive, full-stack AI tutoring engine that uses a custom QLoRA-aligned LLM and Socratic questioning to guide students to answers without giving them away. 

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)

## 📖 About The Project

Standard AI chatbots are designed to give users the exact answer immediately. This project takes the opposite approach. Built specifically for educational purposes, this AI acts as a **Socratic Tutor**. It analyzes the student's coding or math question and provides contextual hints designed to trigger "aha!" moments, encouraging the student to solve the problem themselves.

### ✨ Key Features
* **Custom Fine-Tuned Brain:** Utilizes a lightweight LLM (Phi-3) fine-tuned with **QLoRA** (4-bit quantization) via the Unsloth library, allowing high-performance inference on a single consumer GPU.
* **Stateful Memory:** Integrated **SQLite** database tracks user interaction metrics. 
* **Adaptive Prompting:** The backend dynamically adjusts the system prompt based on user history. If a student asks more than 3 questions in a row, the AI automatically dials back the difficulty and provides more direct hints.
* **Hallucination Bouncer:** Custom Python parsing logic catches and sanitizes LLM run-on sentences or broken characters before they ever reach the user.

## 🏗️ Architecture & Tech Stack

Because hosting large GPU models is expensive, this project utilizes a **Split Deployment Architecture** to run completely for free:

1. **The Backend (Google Colab / Cloudflare):** * A **FastAPI** server runs on a free NVIDIA T4 GPU inside Google Colab.
   * A **Cloudflare Tunnel** exposes the local Colab server securely to the internet.
2. **The Frontend (Streamlit Cloud):** * A sleek, responsive chat interface built with **Streamlit**.
   * Hosted permanently on Streamlit Community Cloud.

## 🚀 How to Run the Project

### 1. Start the Backend (The Brain)
1. Open the provided Jupyter Notebook (`.ipynb`) in Google Colab.
2. Ensure the hardware accelerator is set to **T4 GPU**.
3. Run all cells to install dependencies, load the SQLite database, and spin up the Unsloth model.
4. The final cell will generate a public Cloudflare URL (e.g., `https://random-words.trycloudflare.com`). Leave this cell spinning!

### 2. Connect the Frontend (The Face)
1. Open `app.py` in this repository.
2. Update the `CLOUDFLARE_API_URL` variable on Line 5 with your newly generated Cloudflare link. Make sure to keep `/v1/ask` at the end!
   ```python
   CLOUDFLARE_API_URL = "[https://your-new-link.trycloudflare.com/v1/ask](https://your-new-link.trycloudflare.com/v1/ask)"

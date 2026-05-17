# SmokeDet — Intelligent Smoking Detection System

A premium React-based dashboard coupled with a Flask backend and YOLOv8 machine learning models for real-time monitoring and management of smoking, vaping, and related violations.

## 🌟 Features
- **Real-time Dashboard**: Live camera feeds with YOLOv8-powered detection overlays for smoking, vaping, and faces.
- **Machine Learning Integration**: Custom trained YOLOv8 models (`vape_best.pt`, `smoke_best.pt`, `cigarette_best1.pt`, `face_best.pt`).
- **Advanced Analytics**: Detailed charts and heatmaps using Chart.js to monitor violation trends.
- **Secure Authentication**: Multi-panel Login/SignUp with password strength analysis.
- **Admin Panel**: Role-based access control and user management.
- **System Settings**: Multi-panel configuration for cameras and detection models.
- **Theming**: Integrated Dark/Light mode persistence and premium UI with Glassmorphism.

## 🛠️ Tech Stack
- **Frontend**: React, Vite, React Router, Chart.js, Font Awesome
- **Backend**: Flask (Python), SQLite, OpenCV
- **Machine Learning**: YOLOv8 (Ultralytics), PyTorch
- **Design**: Premium CSS with Glassmorphism and micro-animations

## 📁 Project Structure
- `/src` & `/public`: React Frontend source code and assets.
- `/backend`: Flask Backend and database logic.
- `/VIRSION 1`: Machine learning workspace containing:
  - Custom trained PyTorch models (`models/`).
  - Training scripts and datasets configurations (`scripts/`, `data_*.yaml`).
  - Inference testing scripts (`test.py`).

## 🚀 Getting Started

### 1. Setup the Backend
Navigate to the root directory and run the Flask server:
```bash
python backend/app.py
```
*(Server runs on Port 5000)*

### 2. Setup the Frontend
Open a new terminal, install dependencies, and run the Vite dev server:
```bash
npm install
npm run dev
```
*(Server runs on Port 5173)*

### 3. Model Training (Optional)
To retrain the models, navigate to the `VIRSION 1` directory and run the respective training scripts:
```bash
cd "VIRSION 1"
python scripts/train_cigarette.py
```

---
*Project built for Graduation 2026.*

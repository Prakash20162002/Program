<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Tutor App - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        p, li {
            color: #333;
        }
        .section {
            background: #fff;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .highlight {
            font-weight: bold;
            color: #e74c3c;
        }
        .code-block {
            background: #2d2d2d;
            color: #ecf0f1;
            padding: 10px;
            border-radius: 5px;
            font-family: monospace;
            overflow-x: auto;
            display: block;
        }
    </style>
</head>
<body>
    <h1>AI Tutor App</h1>
    <p>A simple AI-powered learning platform built with <span class="highlight">Streamlit</span>, providing personalized tutoring across multiple subjects using our self-trained AI model.</p>

    <div class="section">
        <h2>Features</h2>
        <ul>
            <li><span class="highlight">AI-Powered Learning:</span> Interact with an AI tutor trained on educational content</li>
            <li><span class="highlight">Multiple Subjects:</span> Access tutoring in Mathematics, Science, History, and Programming</li>
            <li><span class="highlight">Progress Tracking:</span> View your learning progress across different subjects</li>
            <li><span class="highlight">User Authentication:</span> Simple login system to track individual progress</li>
        </ul>
    </div>

    <div class="section">
        <h2>Tech Stack</h2>
        <ul>
            <li><span class="highlight">Frontend & Backend:</span> Streamlit</li>
            <li><span class="highlight">AI Model:</span> Scikit-learn (TF-IDF + Random Forest classifier)</li>
            <li><span class="highlight">Styling:</span> Tailwind CSS (via CDN)</li>
            <li><span class="highlight">Data Storage:</span> Local file storage (pickle files)</li>
        </ul>
    </div>

    <div class="section">
        <h2>Getting Started</h2>
        <h3>Prerequisites</h3>
        <ul>
            <li>Python 3.8 or later</li>
            <li>pip (Python package manager)</li>
        </ul>
        <h3>Installation</h3>
        <p>1. Clone the repository</p>
        <pre class="code-block">git clone https://github.com/yourusername/ai-tutor.git
cd ai-tutor</pre>

        <p>2. Install dependencies</p>
        <pre class="code-block">pip install -r requirements.txt</pre>

        <p>3. Train the AI model</p>
        <pre class="code-block">python train_model.py</pre>

        <p>4. Run the application</p>
        <pre class="code-block">streamlit run app.py</pre>
    </div>
</body>
</html>

# EmoWellBeing Companion

A compassionate AI-powered emotional support platform that provides a safe space for users to share their feelings, track their mood, and receive supportive responses from an AI chatbot.

## Features

- **AI-Powered Chat**: Talk to a compassionate AI chatbot that understands emotions and provides non-judgmental support
- **Mood Tracking**: Daily mood check-ins with visual trend analysis
- **Crisis Support**: Immediate access to crisis helplines and resources
- **User Authentication**: Secure login and registration system
- **Responsive Design**: Beautiful, accessible interface built with React and Tailwind CSS

## Tech Stack

### Frontend
- React 18
- React Router DOM
- Tailwind CSS
- Axios for API calls
- Framer Motion for animations

### Backend
- FastAPI
- SQLAlchemy with MySQL
- JWT Authentication
- Groq AI for chat responses
- Hugging Face for sentiment analysis
- Rate limiting with SlowAPI

## Installation

### Prerequisites
- Node.js (v16 or higher)
- Python (v3.8 or higher)
- MySQL database
- Groq API key (for AI chat)

### Backend Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd EmoWellBeing-Companion
```

2. Create a virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the backend directory:
```env
DATABASE_URL=mysql://username:password@localhost/emowell_db
SECRET_KEY=your-secret-key-here
GROQ_API_KEY=your-groq-api-key-here
```

5. Create the database:
```bash
mysql -u username -p -e "CREATE DATABASE emowell_db;"
```

6. Run the backend:
```bash
uvicorn app.main:app --reload --port 5000
```

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

## Usage

1. Register a new account or login
2. Start chatting with the AI companion
3. Track your mood daily
4. View mood trends and insights
5. Access crisis support resources when needed

## API Documentation

The backend provides RESTful APIs for:
- Authentication (login/register/logout)
- Chat functionality
- Mood tracking
- Contact forms

API documentation available at `http://localhost:5000/docs` when running the backend.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support or questions, please contact us through the contact form in the application or reach out to crisis helplines if you're in immediate need.

## Safety Notice

This application is designed to provide emotional support but is not a substitute for professional mental health care. If you're experiencing a crisis, please contact emergency services or professional help immediately.

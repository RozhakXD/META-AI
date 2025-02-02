# META AI Chat API 🤖
![META-AI Image](https://github.com/user-attachments/assets/967a7172-78d8-4412-a506-bb3609f95c19)

Welcome to the META AI Chat API! This API allows you to integrate AI-driven chat functionality into your applications, providing natural language responses to user queries. Whether you're building a customer support bot, a personal assistant, or an educational tool, this API is designed to be simple, fast, and easy to integrate.

## About 📚
The META AI Chat API is a powerful tool for adding intelligent chatbot interactions to your applications. It leverages the capabilities of META AI to provide seamless and context-aware responses. This API is ideal for developers looking to enhance their applications with AI-driven chat features.

**Key Features**:
- **Real-time Interaction**: Get instant responses from the chatbot.
- **Simple Integration**: Use a JSON-based API for easy implementation.
- **Scalable**: Built to handle high volumes of requests.

## Installation 🛠️
```bash
apt update -y && apt upgrade -y
pkg install python-pip git
git clone https://github.com/RozhakXD/META-AI.git
cd META-AI
pip install -r requirements.txt
python run.py
```

## Usage 🚀
To use the META AI Chat API, send a POST request to the /api/chat endpoint with a JSON payload containing the message you want to send to the chatbot.

**Example Request**:
```bash
curl -X POST http://localhost:5000/chat -H "Content-Type: application/json" -d '{"message": "Hi, who are you?"}'
```

**Example Response**:
```json
{
  "message": "Hello! I'm Meta AI, your friendly AI assistant. I'm here to help you with any questions or tasks you may have. How can I assist you today?"
}
```

## Screenshot 📸
![Image 1](https://github.com/user-attachments/assets/3527d8e6-2a29-4719-ad9c-99837e050d65)

![Image 2](https://github.com/user-attachments/assets/eb84ffbe-9def-4280-9fe3-b260bd05fd6b)

## Support the Project 💖
If you find this project helpful, consider supporting me to keep it alive and improve it further. You can support me via:

- [Trakteer](https://trakteer.id/rozhak_official/tip)
- [PayPal](https://paypal.me/rozhak9)
- [Saweria](https://saweria.co/rozhak9)

Your support means a lot and helps me continue working on open-source projects like this one! 🚀

## License 📜
This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

> Thank you for using the META AI Chat API! If you have any questions or need further assistance, feel free to reach out. 🎉

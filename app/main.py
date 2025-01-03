
from flask import Flask, render_template, request, jsonify, session
from swarm import Swarm
from app.agents import user_interface_agent
import logging
from typing import List, Dict, Any

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChatServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = 'project-1'
        self.client = Swarm()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/')(self.home)
        self.app.route('/send_message', methods=['POST'])(self.send_message)

    def home(self):
        if 'chat_history' not in session:
            session['chat_history'] = []
        return render_template('chat.html', chat_history=session['chat_history'])


    def format_message_history(self, chat_history: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Convert chat history into the format expected by Swarm AI."""
        formatted_messages = []
        for message in chat_history:
            formatted_messages.extend([
                {"role": "user", "content": message["user"]},
                {"role": "assistant", "content": message["bot"]}
            ])
        return formatted_messages

    def process_message_with_history(self, user_message: str, chat_history: List[Dict[str, str]]) -> Dict[str, Any]:
        """Process message with full conversation history context."""
        try:
            # Format all previous messages plus the new message
            formatted_messages = self.format_message_history(chat_history)
            formatted_messages.append({"role": "user", "content": user_message})

            # Process through agent pipeline with history
            response = self.client.run(
                agent=user_interface_agent,
                messages=formatted_messages
            )

            if response and response.messages:
                return {
                    "status": "success",
                    "response": response.messages[-1].get("content", "")
                }
            else:
                raise ValueError("No response received from agent")

        except Exception as e:
            logger.error(f"Error in process_message: {str(e)}")
            return {
                "status": "error",
                "error": str(e)
            }

    def send_message(self):
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        try:
            data = request.get_json()
            if not data or 'message' not in data:
                return jsonify({'error': 'Invalid request format'}), 400

            user_message = data['message'].strip()
            if not user_message:
                return jsonify({'error': 'Empty message'}), 400

            # Initialize or get chat history
            if 'chat_history' not in session:
                session['chat_history'] = []

            # Process message with history
            result = self.process_message_with_history(
                user_message,
                session['chat_history']
            )

            if result["status"] == "error":
                return jsonify({'error': result["error"]}), 500

            # Update chat history
            session['chat_history'].append({
                'user': user_message,
                'bot': result["response"]
            })
            session.modified = True

            return jsonify({
                'response': result["response"],
                'chat_history': session['chat_history']
            })

        except Exception as e:
            logger.error(f"Error in send_message: {str(e)}")
            return jsonify({
                'error': 'An error occurred while processing your message'
            }), 500

server = ChatServer()
app = server.app

if __name__ == '__main__':
    app.run(debug=True)
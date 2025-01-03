const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");
const chatContainer = document.getElementById("chat-container");
const sendButton = document.getElementById("send-button");
chatForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const message = userInput.value.trim();
  if (!message) return;

  // Add user message to chat
  appendMessage(message, true);
  userInput.value = "";
  setLoading(true);

  try {
    const response = await fetch("/send_message", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({ message }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const contentType = response.headers.get("content-type");
    if (!contentType || !contentType.includes("application/json")) {
      throw new TypeError("Oops, we haven't gotten JSON!");
    }

    const data = await response.json();
    if (data.error) {
      appendMessage(`Error: ${data.error}`, false);
      return;
    }

    // Add bot response to chat
    if (data.response) {
      appendMessage(data.response, false);
    } else {
      throw new Error("No response data received");
    }
  } catch (error) {
    console.error("Error:", error);
    appendMessage(
      "Sorry, there was an error processing your message. Please try again.",
      false
    );
  } finally {
    setLoading(false);
  }
});

function appendMessage(message, isUser) {
  const messageDiv = document.createElement("div");
  messageDiv.className = `message ${isUser ? "user-message" : "bot-message"}`;
  messageDiv.textContent = message;
  chatContainer.appendChild(messageDiv);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}
function setLoading(isLoading) {
  sendButton.disabled = isLoading;
  userInput.disabled = isLoading;
  if (isLoading) {
    const loadingDiv = document.createElement("div");
    loadingDiv.className = "message bot-message";
    loadingDiv.innerHTML = '<div class="loading"></div>Thinking...';
    loadingDiv.id = "loading-message";
    chatContainer.appendChild(loadingDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
  } else {
    const loadingMessage = document.getElementById("loading-message");
    if (loadingMessage) {
      loadingMessage.remove();
    }
  }
}
// Scroll to bottom on load
window.onload = () => {
  chatContainer.scrollTop = chatContainer.scrollHeight;
};

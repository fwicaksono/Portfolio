document.addEventListener('DOMContentLoaded', function () {
    // Chat functionality
    const chatForm = document.getElementById('chat-form');
    const chatBox = document.getElementById('chat-box');
    const userInput = document.getElementById('user-input');

    if (chatForm && chatBox && userInput) {
        chatForm.addEventListener('submit', async function (event) {
            event.preventDefault(); // Prevent the form from submitting the traditional way

            const userMessage = userInput.value.trim();
            if (!userMessage) {
                alert('Please enter a message.');
                return;
            }

            // Add the user's message to the chat box
            chatBox.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;
            userInput.value = ''; // Clear the input field

            try {
                // Send the user's message to the server
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ user_input: userMessage }),
                });

                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                const data = await response.json();

                // Add the chatbot's response to the chat box
                chatBox.innerHTML += `<p><strong>AI:</strong> ${data.response}</p>`;

                // Scroll to the bottom of the chat box
                chatBox.scrollTop = chatBox.scrollHeight;
            } catch (error) {
                console.error('Error:', error);
                chatBox.innerHTML += `<p><strong>AI:</strong> Sorry, something went wrong. Please try again.</p>`;
            }
        });
    }

    // Additional JavaScript functionality can be added here

});
document.addEventListener('DOMContentLoaded', function() {
    const questionForm = document.getElementById('questionForm');
    const questionInput = document.getElementById('question');
    const submitBtn = document.getElementById('submitBtn');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const responseArea = document.getElementById('responseArea');
    const answer = document.getElementById('answer');
    const errorArea = document.getElementById('errorArea');

    // Handle form submission
    questionForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        const question = questionInput.value.trim();

        if (!question) {
            showError('Please enter a question.');
            return;
        }

        // Show loading state
        setLoading(true);
        hideError();
        hideResponse();

        try {
            const response = await fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ question: question })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.detail || 'Failed to get answer');
            }

            showResponse(data.answer);
        } catch (error) {
            showError(error.message);
        } finally {
            setLoading(false);
        }
    });

    // Handle example questions
    document.querySelectorAll('.example-question').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            questionInput.value = this.textContent;
            questionInput.focus();
            // Optional: Automatically submit the form when clicking an example
            questionForm.dispatchEvent(new Event('submit'));
        });
    });

    // Utility functions
    function setLoading(isLoading) {
        submitBtn.disabled = isLoading;
        loadingIndicator.classList.toggle('d-none', !isLoading);
    }

    function showResponse(text) {
        answer.textContent = text;
        responseArea.classList.remove('d-none');
        responseArea.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    function hideResponse() {
        responseArea.classList.add('d-none');
    }

    function showError(message) {
        errorArea.textContent = message;
        errorArea.classList.remove('d-none');
    }

    function hideError() {
        errorArea.classList.add('d-none');
    }
}); 
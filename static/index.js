document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('myForm');

    form.addEventListener('submit', async function (e) {
      e.preventDefault(); // Prevent the default form submit action

      const formData = new FormData(form);
      const url = form.getAttribute('data-submit-url'); // Ensure this matches your Flask route

      try {
        const response = await fetch(url, {
          method: 'POST',
          body: formData,
        });

        if (!response.ok) {
          throw new Error(`Server responded with ${response.status}: ${await response.text()}`);
        }

        const result = await response.json(); // Assuming the server responds with JSON

        // Display the result or error message
        document.getElementById('response').innerText = result.message || result.error;
      } catch (error) {
        console.error('Fetch error:', error);
        document.getElementById('response').innerText = 'An error occurred. Please try again.';
      }
    });
  });

// Function to check the status of model training
function checkTrainingStatus() {
    // Send an AJAX request to the server to check the status
    fetch('/check_training_status')
      .then(response => response.json())
      .then(data => {
        if (data.training_completed) {
          // If training is completed, redirect to upload_file.html
          window.location.href = "/templates/upload_file.html";
        } else {
          // If training is not completed, check again after 5 seconds
          setTimeout(checkTrainingStatus, 5000);
        }
      })
      .catch(error => {
        console.error('Error checking training status:', error);
      });
  }
  
  // Start checking the status when the page is loaded
  checkTrainingStatus();
  
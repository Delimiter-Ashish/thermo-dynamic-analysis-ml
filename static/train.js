// Function to handle the training process when the "Train Now" button is clicked
document.getElementById('trainButton').addEventListener('click', function() {
    // Show loading animation
    document.getElementById('loadingAnimation').style.display = 'block';

    // Simulate training process (replace with actual training logic)
    setTimeout(function() {
        // Hide loading animation
        document.getElementById('loadingAnimation').style.display = 'none';

        // Show training completion message
        // document.getElementById('trainingMessage').innerText = 'Training complete!';
        // document.getElementById('trainingMessage').style.display = 'block';

        // Show test button
        document.getElementById('testButton').style.display = 'block';
    }, 3000); // Simulate 3 seconds of training time
});

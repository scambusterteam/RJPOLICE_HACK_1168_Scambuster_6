document.getElementById('registrationForm').addEventListener('submit', function(event) {
  event.preventDefault();
  // Perform registration logic here
  // Example: Get input values
  const name = document.getElementById('name').value;
  const emailOrPhone = document.getElementById('emailOrPhone').value;
  const password = document.getElementById('password').value;

  // Placeholder logic - console log for demonstration
  console.log(User Registered:\nName: ${name}\nEmail/Phone: ${emailOrPhone});
});

document.getElementById('loginForm').addEventListener('submit', function(event) {
  event.preventDefault();
  // Perform login logic here
  // Example: Get input values
  const emailOrPhone = document.getElementById('emailOrPhone').value;
  const password = document.getElementById('password').value;

  // Placeholder logic - console log for demonstration
  console.log(User Logged In:\nEmail/Phone: ${emailOrPhone}\nPassword/OTP: ${password});
});

document.getElementById('dashboardForm').addEventListener('submit', function(event) {
  event.preventDefault();
  // Perform dashboard logic here
  // Example: Get input values
  const inputNumber = document.getElementById('inputNumber').value;
  const inputURL = document.getElementById('inputURL').value;
  const inputImage = document.getElementById('inputImage').value; // For file upload

  // Placeholder logic - console log for demonstration
  console.log(Input Received:\nNumber: ${inputNumber}\nURL: ${inputURL}\nImage: ${inputImage});
});
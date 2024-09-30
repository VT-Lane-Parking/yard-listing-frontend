
// Function to open the modal for login or sign-up
function openModal(mode) {
    document.getElementById('auth-modal').style.display = 'block';
    
    // Display the appropriate form based on the mode
    if (mode === 'login') {
        document.getElementById('login-form').style.display = 'block';
        document.getElementById('signup-form').style.display = 'none';
    } else if (mode === 'signup') {
        document.getElementById('signup-form').style.display = 'block';
        document.getElementById('login-form').style.display = 'none';
    }
}

// Function to close the modal
function closeModal() {
    document.getElementById('auth-modal').style.display = 'none';
}

// Keep existing code for handling sign-up and login forms...
// Firebase Configuration and Initialization
const firebaseConfig = {
  apiKey: "AIzaSyD6tNXhtzlUhgYmQa7-g0dhUUxZUPx4d9Q",
  authDomain: "vt-lane-parking.firebaseapp.com",
  projectId: "vt-lane-parking",
  storageBucket: "vt-lane-parking.appspot.com",
  messagingSenderId: "713873844057",
  appId: "1:713873844057:web:ca11b1c10c7c92115b4e48"
};
firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();

// Sign Up Form Submission
document.getElementById('signup-form').addEventListener('submit', function(e) {
    e.preventDefault();
  
    const firstName = document.getElementById('first-name').value;
    const lastInitial = document.getElementById('last-initial').value;
    const phone = document.getElementById('phone').value;
    const email = document.getElementById('signup-email').value;
    const propertyAddress = document.getElementById('property-address').value;
    const password = document.getElementById('signup-password').value;
  
    // Check for duplicates (email, phone, address)
    db.collection('users').where('email', '==', email).get().then(querySnapshot => {
        if (!querySnapshot.empty) {
            alert('An account with this email already exists.');
            return;
        }
        db.collection('users').where('phone', '==', phone).get().then(querySnapshot => {
            if (!querySnapshot.empty) {
                alert('An account with this phone number already exists.');
                return;
            }
            db.collection('users').where('propertyAddress', '==', propertyAddress).get().then(querySnapshot => {
                if (!querySnapshot.empty) {
                    alert('An account with this property address already exists.');
                    return;
                }
  
                // Create user account
                firebase.auth().createUserWithEmailAndPassword(email, password)
                .then(userCredential => {
                    const user = userCredential.user;
                    // Add user info to Firestore
                    return db.collection('users').doc(user.uid).set({
                        firstName: firstName,
                        lastInitial: lastInitial,
                        phone: phone,
                        email: email,
                        propertyAddress: propertyAddress
                    });
                })
                .then(() => {
                    alert('Account created successfully.');
                    document.getElementById('signup-form').reset();
                    closeModal();
                })
                .catch(error => {
                    console.error('Error during sign up:', error.message);
                });
            });
        });
    });
  });
  
  // Login Form Submission
  document.getElementById('login-form').addEventListener('submit', function(e) {
    e.preventDefault();
  
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;
  
    firebase.auth().signInWithEmailAndPassword(email, password)
    .then(() => {
        alert('Login successful!');
        closeModal();
        // Redirect to form or next page
    })
    .catch(error => {
        if (error.code === 'auth/wrong-password') {
            alert('Incorrect password.');
        } else if (error.code === 'auth/user-not-found') {
            alert('Email not found.');
        } else {
            alert('Error logging in.');
        }
    });
  });
'''

Documentation

Website code that does allows people to put their yard up
for rent for tailgating events. Allows people to rent out
yards for tailgating events.

to use when not attached to github: right-click index and hit run in browse



app.js: contains code that does...

browse-yards.html:

index.html:

list-yard.html

styles.css:



Recommendations of implementation:
predictive address typing
map embed
being able to scroll around on map and select lots
    - when lots are selected, they pop up a bubble to display information
    - need to create a new lot when a yard gets registered
attach a database or method of storage
implement a payment system?
UI/UX designs
link to game schedule?
add pictures of the yard
add whats allowed and whats not allowed in the yard
sign on system
remove examples on browse-yards.html
error checking, can't book a yard that is already booked, can't book a yard that is your own, etc.
add logo and change color scheme to match logo (orange and maroon)
'''




''' Browse Yards Page working code temporary storage
    <main>
        <!-- Search and filter controls -->
        <section id="search-filters">
            <h3>Search and Filter Yards</h3>
            <input type="text" id="search-address" placeholder="Search by address" oninput="filterYards()">
            <input type="number" id="min-size" placeholder="Min Size (sq ft)" oninput="filterYards()">
            <input type="number" id="max-size" placeholder="Max Size (sq ft)" oninput="filterYards()">
            <input type="number" id="min-price" placeholder="Min Price" oninput="filterYards()">
            <input type="number" id="max-price" placeholder="Max Price" oninput="filterYards()">
    
            <!-- Add the new availability filter here -->
            <h3>Filter by Availability</h3>
            <label for="start-filter">Start Time:</label>
            <input type="datetime-local" id="start-filter" oninput="filterYards()">
    
            <label for="end-filter">End Time:</label>
            <input type="datetime-local" id="end-filter" oninput="filterYards()">
        </section>
    
        <!-- Yard Listings -->
        <section id="yard-listings">
            <h2>Yard Listings</h2>
            <ul id="listingsContainer">
                <!-- Yard listings will be displayed here -->
            </ul>
        </section>
    
        <!-- Map Placeholder -->
        <section id="map">
            <h3>Yards Map</h3>
            <iframe width="800" height="600" frameborder="0" scrolling="no" allowfullscreen src="https://tobmaps.blacksburg.gov/portal/apps/webappviewer/index.html?id=5ca8847c8e4f4fe68120e9bb08e10840&extent=-8953276.6654%2C4470463.7032%2C-8949836.9991%2C4472126.2085%2C102100"></iframe>
        </section>
    </main>

    <script>
        // Sample listings for testing purposes
        const listings = [
            { address: '123 Main St', size_sqft: 500, price_per_hour: 25, start_availability: '2024-09-20T09:00', end_availability: '2024-09-20T18:00' },
            { address: '456 Oak Ave', size_sqft: 800, price_per_hour: 30, start_availability: '2024-09-21T09:00', end_availability: '2024-09-21T18:00' },
            { address: '789 Pine St', size_sqft: 600, price_per_hour: 20, start_availability: '2024-09-22T09:00', end_availability: '2024-09-22T18:00' }
        ];

        // Function to display yards
        function displayYards(yards) {
        const listingsContainer = document.getElementById('listingsContainer');
        listingsContainer.innerHTML = '';  // Clear previous listings

        yards.forEach(listing => {
            // Parse and format the start and end availability
            const startDate = new Date(listing.start_availability).toLocaleString();
            const endDate = new Date(listing.end_availability).toLocaleString();

            const li = document.createElement('li');
            li.innerHTML = `<strong>${listing.address}:</strong> ${listing.size_sqft} sq ft, $${listing.price_per_hour}/hour, Available: ${startDate} - ${endDate}`;
            listingsContainer.appendChild(li);
        });
}

        // The filterYards function to filter listings
        function filterYards() {
            const searchAddress = document.getElementById('search-address').value.toLowerCase();
            const minSize = document.getElementById('min-size').value;
            const maxSize = document.getElementById('max-size').value;
            const minPrice = document.getElementById('min-price').value;
            const maxPrice = document.getElementById('max-price').value;
            const startFilter = document.getElementById('start-filter').value;
            const endFilter = document.getElementById('end-filter').value;

            const filteredYards = listings.filter(listing => {
                const matchesAddress = listing.address.toLowerCase().includes(searchAddress);
                const matchesSize = (!minSize || listing.size_sqft >= minSize) && (!maxSize || listing.size_sqft <= maxSize);
                const matchesPrice = (!minPrice || listing.price_per_hour >= minPrice) && (!maxPrice || listing.price_per_hour <= maxPrice);
                const matchesAvailability = (!startFilter || new Date(listing.start_availability) >= new Date(startFilter)) &&
                                            (!endFilter || new Date(listing.end_availability) <= new Date(endFilter));
                
                return matchesAddress && matchesSize && matchesPrice && matchesAvailability;
            });

            displayYards(filteredYards);
        }

        // Initially display all listings
        displayYards(listings);
    </script>
'''



''' app.js temporary code storage

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

// Show login modal
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

// Close modal
function closeModal() {
  document.getElementById('auth-modal').style.display = 'none';
}

// Handle Sign-Up with automatic redirect to login
document.getElementById('signup-form').addEventListener('submit', function(e) {
  e.preventDefault();
  const email = document.getElementById('signup-email').value;
  const password = document.getElementById('signup-password').value;

  firebase.auth().createUserWithEmailAndPassword(email, password)
  .then(() => {
      alert('Account created successfully! Redirecting to login...');
      closeModal();
      document.getElementById('login-btn').click();
  })
  .catch(error => {
      console.error('Error during sign up:', error.message);
  });
});

// Handle Login
document.getElementById('login-form').addEventListener('submit', function(e) {
  e.preventDefault();
  const email = document.getElementById('login-email').value;
  const password = document.getElementById('login-password').value;

  firebase.auth().signInWithEmailAndPassword(email, password)
  .then(() => {
      alert('Login successful!');
      closeModal();
  })
  .catch(error => {
      console.error('Error during login:', error.message);
  });
});

// Show or hide the yard creation form based on login state
firebase.auth().onAuthStateChanged((user) => {
  if (user) {
      document.getElementById('yard-form').style.display = 'block';
  } else {
      document.getElementById('yard-form').style.display = 'none';
  }
});

// Handle yard form submission
document.getElementById('yard-form').addEventListener('submit', function(e) {
  e.preventDefault();

  const user = firebase.auth().currentUser;
  if (user) {
      // Get form values
      const address = document.getElementById('yard-address').value;
      const price = document.getElementById('yard-price').value;
      const availability = document.getElementById('yard-availability').value;

      // Add yard listing to Firestore
      db.collection('yards').add({
          address: address,
          price: price,
          availability: availability,
          ownerId: user.uid, // Associate yard with logged-in user
          timestamp: firebase.firestore.FieldValue.serverTimestamp()
      })
      .then(() => {
          alert('Yard listed successfully!');
          document.getElementById('yard-form').reset(); // Optionally reset the form
      })
      .catch((error) => {
          console.error('Error listing yard:', error.message);
      });
  } else {
      alert('You must be logged in to list a yard.');
  }
});

// Handle sign out
function signOut() {
  firebase.auth().signOut().then(() => {
      alert('User signed out successfully.');
  }).catch((error) => {
      console.error('Error during sign out:', error.message);
  });
}

'''
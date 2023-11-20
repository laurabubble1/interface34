function callFunction(Number) {
    fetch(`/call_function/${Number}`)
        .then(response => response.text())
        .then(data => {
            console.log(data);
        });
}
let isUpArrowPressed = false;
  let isDownArrowPressed = false;
  let isLeftArrowPressed = false;
  let isRightArrowPressed = false;

  document.addEventListener('keydown', function(event) {
    // Check the arrow key pressed
    switch(event.key) {
      case 'ArrowUp':
        // Set the variable to true when the 'Up' arrow key is pressed
        isUpArrowPressed = true;
        // Call your function for the up arrow
        handleArrowUp();
        break;
      case 'ArrowDown':
        // Set the variable to true when the 'Down' arrow key is pressed
        isDownArrowPressed = true;
        // Call your function for the down arrow
        handleArrowDown();
        break;
      case 'ArrowLeft':
        // Set the variable to true when the 'Left' arrow key is pressed
        isLeftArrowPressed = true;
        // Call your function for the left arrow
        handleArrowLeft();
        break;
      case 'ArrowRight':
        // Set the variable to true when the 'Right' arrow key is pressed
        isRightArrowPressed = true;
        // Call your function for the right arrow
        handleArrowRight();
        break;
    }
  });

  document.addEventListener('keyup', function(event) {
    // Check the arrow key released
    switch(event.key) {
      case 'ArrowUp':
        // Set the variable to false when the 'Up' arrow key is released
        isUpArrowPressed = false;
        // Additional function when the 'Up' arrow key is released
        handleArrowUpRelease();
        break;
      case 'ArrowDown':
        // Set the variable to false when the 'Down' arrow key is released
        isDownArrowPressed = false;
        // Additional function when the 'Down' arrow key is released
        handleArrowDownRelease();
        break;
      case 'ArrowLeft':
        // Set the variable to false when the 'Left' arrow key is released
        isLeftArrowPressed = false;
        // Additional function when the 'Left' arrow key is released
        handleArrowLeftRelease();
        break;
      case 'ArrowRight':
        // Set the variable to false when the 'Right' arrow key is released
        isRightArrowPressed = false;
        // Additional function when the 'Right' arrow key is released
        handleArrowRightRelease();
        break;
    }
  });

  function handleArrowUp() {
    console.log('Up arrow pressed');
    callFunction(1);
    // Add your logic for the up arrow key here
  }

  function handleArrowDown() {
    console.log('Down arrow pressed');
    callFunction(2);
    // Add your logic for the down arrow key here
  }

  function handleArrowLeft() {
    console.log('Left arrow pressed');
    callFunction(3);
    // Add your logic for the left arrow key here
  }

  function handleArrowRight() {
    console.log('Right arrow pressed');
    callFunction(4);
    // Add your logic for the right arrow key here
  }

  // Additional functions for when arrow keys are released
  function handleArrowUpRelease() {
    console.log('Up arrow released');
    callFunction(5);
    // Add your logic for when the up arrow key is released here
  }

  function handleArrowDownRelease() {
    console.log('Down arrow released');
    callFunction(5);
    // Add your logic for when the down arrow key is released here
  }

  function handleArrowLeftRelease() {
    console.log('Left arrow released');
    callFunction(5);
    // Add your logic for when the left arrow key is released here
  }

  function handleArrowRightRelease() {
    console.log('Right arrow released');
    callFunction(5);
    // Add your logic for when the right arrow key is released here
  }
function startVideo() {
    document.getElementById('video_feed').src = "{{ url_for('video_feed') }}";
}

function stopVideo() {
    document.getElementById('video_feed').src = "";
}
/**
 * Simple client-side login feature.
 *
 * NOTE: In a real application, authentication must be handled server-side
 * with secure password hashing and session management. This implementation
 * demonstrates the UI/UX flow only and must not be used for production
 * authentication without a proper back-end.
 */

(function () {
  "use strict";

  // ---------------------------------------------------------------------------
  // Demo credentials (replace with a real back-end call in production)
  // ---------------------------------------------------------------------------
  var DEMO_CREDENTIALS = {
    username: "admin",
    // Passwords are never stored in plain text in real applications.
    password: "D3m0P@ssw0rd!",
  };

  // ---------------------------------------------------------------------------
  // DOM references
  // ---------------------------------------------------------------------------
  var form = document.getElementById("login-form");
  var usernameInput = document.getElementById("username");
  var passwordInput = document.getElementById("password");
  var usernameError = document.getElementById("username-error");
  var passwordError = document.getElementById("password-error");
  var submitBtn = document.getElementById("submit-btn");
  var loginMessage = document.getElementById("login-message");

  // ---------------------------------------------------------------------------
  // Helpers
  // ---------------------------------------------------------------------------
  function clearErrors() {
    usernameError.textContent = "";
    passwordError.textContent = "";
    usernameInput.classList.remove("invalid");
    passwordInput.classList.remove("invalid");
    loginMessage.textContent = "";
    loginMessage.className = "message";
  }

  function showFieldError(input, errorEl, message) {
    input.classList.add("invalid");
    errorEl.textContent = message;
  }

  function setMessage(text, type) {
    loginMessage.textContent = text;
    loginMessage.className = "message " + type;
  }

  // ---------------------------------------------------------------------------
  // Validation
  // ---------------------------------------------------------------------------
  function validate(username, password) {
    var valid = true;

    if (!username) {
      showFieldError(usernameInput, usernameError, "Username is required.");
      valid = false;
    }

    if (!password) {
      showFieldError(passwordInput, passwordError, "Password is required.");
      valid = false;
    }

    return valid;
  }

  // ---------------------------------------------------------------------------
  // Simulated login request
  // ---------------------------------------------------------------------------
  function login(username, password, callback) {
    // Simulate an asynchronous network request.
    setTimeout(function () {
      if (
        username === DEMO_CREDENTIALS.username &&
        password === DEMO_CREDENTIALS.password
      ) {
        callback(null, { username: username });
      } else {
        callback(new Error("Invalid username or password."));
      }
    }, 600);
  }

  // ---------------------------------------------------------------------------
  // Form submit handler
  // ---------------------------------------------------------------------------
  form.addEventListener("submit", function (event) {
    event.preventDefault();
    clearErrors();

    var username = usernameInput.value.trim();
    // Passwords are not trimmed to preserve user-intended whitespace characters.
    var password = passwordInput.value;

    if (!validate(username, password)) {
      return;
    }

    submitBtn.disabled = true;
    submitBtn.textContent = "Signing in…";

    login(username, password, function (err, user) {
      submitBtn.disabled = false;
      submitBtn.textContent = "Sign In";

      if (err) {
        setMessage(err.message, "error");
      } else {
        setMessage("Welcome, " + user.username + "! Login successful.", "success");
        form.reset();
      }
    });
  });
})();
